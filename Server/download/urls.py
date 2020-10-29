from django.urls import path
from .views import download, requests_list, download_last_hour



urlpatterns = [
	path("file/link/<int:pk>", download, name="downloads_files"),
	path("requests/link/<int:pk>", requests_list, name="request_list"),
	path("file/link/lasthour/<int:pk>", download_last_hour, name="downloadLastHour"),
	
]