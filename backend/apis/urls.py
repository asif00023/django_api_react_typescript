from django.urls import path
from apis.all_views import upload_data, download_data

# ref: https://www.django-rest-framework.org/tutorial/1-serialization/
urlpatterns = [
    path('upload-data/', upload_data.process_post_req),
    path('download-data/', download_data.process_get_req),
]