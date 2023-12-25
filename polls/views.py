from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question


def index(request):
    """Questionのリスト
    Args:
        request (_type_): _description_
    Returns:
        _type_: Questionで新しいものから5個ほど取り出し返す
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    """Questionの詳細を参照
    Args:
        request (_type_): リクエスト
        question_id (_type_): Questionのid
    Returns:
        _type_: 選択されたQuestionの詳細が何かを表示してくれる
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


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
