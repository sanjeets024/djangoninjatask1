
from django.urls import path

from myapp82.api import api
from django.conf.urls import include

urlpatterns = [

  path("", api.urls),
]