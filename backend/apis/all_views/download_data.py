from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataprocessor import settings
from apis.BusinessLogic.ChartGenerationBL import ChartGenerationBL
import traceback
import os

"""
references:
1. Using Django core JsonResponse class:
        https://stackoverflow.com/questions/51511813/in-order-to-allow-non-dict-objects-to-be-serialized-set-the-safe-parameter-to-fa
2. Print exception stack trace in Python
        https://www.geeksforgeeks.org/how-to-print-exception-stack-trace-in-python/
3. Check for file existence in Python
        https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
4. Get base URL in Django
        https://stackoverflow.com/questions/2345708/how-can-i-get-the-full-absolute-url-with-domain-in-django
"""


@csrf_exempt
def process_get_req(request):
# {
    video_file_url_for_resp: str = ""
    data_processing_errors: list = []
    image_full_urls: list = []
    chart_gen_dir: str = "/chart_generation_output/"
    if request.method == 'GET':
        try:
        # {
            video_file_name = settings.VIDEO_FILE_NAME
            full_video_file_path: str = os.path.join(settings.MEDIA_ROOT, video_file_name)
            if (not os.path.isfile(full_video_file_path)):
                data_processing_errors.append("Video file not found in download directory")
            else:
                video_file_url_for_resp = request.build_absolute_uri() + settings.MEDIA_URL + video_file_name
                video_file_url_for_resp = video_file_url_for_resp.replace("/apis/download-data/", "")

            csv_file_name = settings.CSV_FILE_NAME
            full_csv_file_path: str = os.path.join(settings.MEDIA_ROOT, csv_file_name)
            if (not os.path.isfile(full_csv_file_path)):
                data_processing_errors.append("CSV file not found in download directory")
            else:
                output_directory: str = settings.MEDIA_ROOT + chart_gen_dir
                fps: int = settings.FPS
                bl_class_obj = ChartGenerationBL()
                generated_files_list: list = bl_class_obj.generate(full_csv_file_path, fps, output_directory)

                if generated_files_list is not None and len(generated_files_list) > 0:
                    for single in generated_files_list:
                        full_url: str = request.build_absolute_uri() + settings.MEDIA_URL + chart_gen_dir + single
                        full_url = full_url.replace("/apis/download-data/", "")
                        image_full_urls.append(full_url)
        # }
        except Exception as ex:
        # {
            print("Exception occurred in API method")
            print(str(ex))
            traceback.print_exc()
            data_processing_errors.append("Exception occurred in API method")
        # }

        response_dict: dict = {
            'errors': data_processing_errors,
            'videoFile': video_file_url_for_resp,
            'images': image_full_urls
        }
        return JsonResponse(response_dict, safe=False)  # ref: https://stackoverflow.com/questions/51511813/in-order-to-allow-non-dict-objects-to-be-serialized-set-the-safe-parameter-to-fa
    else:
        return JsonResponse({"message": "POST / PUT / DELETE / TRACE not allowed, only GET allowed"})
# }