from django.db import models


# Questionテーブル
class Question(models.Model):
    def __str__(self) -> str:
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


# Choiceテーブル
# 外部キーquestion
class Choice(models.Model):
    def __str__(self) -> str:
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
