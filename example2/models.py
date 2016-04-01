from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Questions(models.Model):
    question_txt = models.CharField(max_length=50)
    pub_date = models.DateField()
    def __str__(self):
        return self.question_txt
    def was_published_recently(self):
        return self.pub_date >= timezone.now().date() - datetime.timedelta()

class Choice(models.Model):
    question = models.ForeignKey(Questions , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text