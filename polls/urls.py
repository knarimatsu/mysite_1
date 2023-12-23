from django.urls import path
from . import views

urlpatterns = [
    # poll配下のviewsのindexを実行
    path("", views.index, name="index"),
]
