from django.urls import path
from . import views

"""_summary_
第1引数:URIパターンを記載
第2引数:該当するURIがリクエストできた時に実行するviewのメソッド
第3引数(name=の部分):任意、名前つけるだけ
"""
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ReusltsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
