from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from apis.forms.UploadDataForm import UploadDataForm
from dataprocessor import settings
import traceback
import os




@csrf_exempt
def process_post_req(request):
# {
    if request.method == 'GET':
        return JsonResponse({"message": "GET not allowed, only POST allowed"})
    elif request.method == 'POST':
        operation_result: bool = False
        operation_details: str = ""

        try:
        # {

            #form = UploadDataForm(request.POST, request.FILES)
            #form.is_valid() and \
            if request.FILES['video_file'] is not None and request.FILES['csv_file'] is not None:
                operation_result = handle_uploaded_file(request.FILES['video_file'], request.FILES['csv_file'])
        # }
        except Exception as ex:
        # {
            print("Exception occurred in API method")
            print(str(ex))
            traceback.print_exc()
            operation_details = "Exception occurred in API method"
        # }

        response_dict: dict = {'message': operation_details, 'uploadSuccessful': operation_result}
        return JsonResponse(response_dict, safe=False)      # ref: https://stackoverflow.com/questions/51511813/in-order-to-allow-non-dict-objects-to-be-serialized-set-the-safe-parameter-to-fa
# }


def handle_uploaded_file(video_file, csv_file):
# {
    try:
    # {
        video_file_name = settings.VIDEO_FILE_NAME
        full_video_file_path : str = os.path.join(settings.MEDIA_ROOT, video_file_name)
        csv_file_name = settings.CSV_FILE_NAME
        full_csv_file_path: str = os.path.join(settings.MEDIA_ROOT, csv_file_name)

        with open(full_video_file_path, 'wb+') as destination1:
            for chunk in video_file.chunks():
                destination1.write(chunk)

        with open(full_csv_file_path, 'wb+') as destination2:
            for chunk in csv_file.chunks():
                destination2.write(chunk)

        return True
    # }
    except Exception as ex:
    # {
        print("Exception in function handle_uploaded_file")
        print(str(ex))
        traceback.print_exc()
        return False
    # }
# }