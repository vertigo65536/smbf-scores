from django.db import models

# Create your models here.
class Secret(models.Model):
    name = models.CharField(max_length=100, primary_key = True)
    value = models.CharField(max_length=100)

class Score(models.Model):
    secret = models.CharField(max_length=100, primary_key = True)
    p1_tag = models.CharField(max_length=100)
    p1_name = models.CharField(max_length=100)
    p2_tag = models.CharField(max_length=100)
    p2_name = models.CharField(max_length=100)
    p1_score = models.IntegerField()
    p2_score = models.IntegerField()
    center_text = models.CharField(max_length=100)
    game = models.CharField(max_length=100)
    hidden = models.BooleanField()

class GameStyle(models.Model):
    game = models.IntegerField(primary_key=True)
    style = models.CharField(max_length=300)
