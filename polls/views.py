from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

from .models import Question, Choice


def index(request):
    """Questionのリスト
    Args:
        request (_type_): _description_
    Returns:
        _type_: Questionで新しいものから5個ほど取り出し返す
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {"question": question})


def vote(request, question_id):
    """投票
    Args:
        reqest (_type_): _description_
        question_id (_type_): _description_
    Returns:
        _type_: _description_
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponse(reverse("polls:results", args=(question.id)))
