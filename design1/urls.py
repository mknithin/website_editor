from django.urls import path
from .views import load_design_1


urlpatterns = [
    path('', load_design_1, name="load-design1")

]