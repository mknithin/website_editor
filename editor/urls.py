from django.urls import path
from .views import load_editor, upload_image


urlpatterns = [
    path('', load_editor, name="load-design1"),
    path('upload/', upload_image, name="upload-image"),

]