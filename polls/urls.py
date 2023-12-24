from django.urls import path
from . import views

"""_summary_
第1引数:URIパターンを記載
第2引数:該当するURIがリクエストできた時に実行するviewのメソッド
第3引数(name=の部分):任意、名前つけるだけ
"""

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
