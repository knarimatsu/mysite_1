from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    """Questionのリスト
    Args:
        request (_type_): _description_
    Returns:
        _type_: Questionで新しいものから5個ほど取り出し返す
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    """Questionの詳細を参照
    Args:
        request (_type_): リクエスト
        question_id (_type_): Questionのid
    Returns:
        _type_: 選択されたQuestionの詳細が何かを表示してくれる
    """
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    """Questionの結果を参照
    Args:
        request (_type_): _description_
        question_id (_type_): _description_
    Returns:
        _type_: _description_
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(reqest, question_id):
    """投票
    Args:
        reqest (_type_): _description_
        question_id (_type_): _description_
    Returns:
        _type_: _description_
    """
    return HttpResponse("You're voting on question %s." % question_id)
