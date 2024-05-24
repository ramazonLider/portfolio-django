from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("projects/", projects, name="projects"),
    path("blogs/", blogs, name="blogs"),
    path("blog/<int:pk>/", detail, name="detail")
]
