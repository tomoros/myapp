from django.db import models

class Kusyokyuu(models.Model):
    kuid = models.IntegerField(primary_key=True)
    kuname = models.CharField(max_length=30)
    question1 = models.CharField(max_length=100)
    question2 = models.CharField(max_length=100)
    question3 = models.CharField(max_length=100)
    question4 = models.CharField(max_length=100)
    syutudai = models.IntegerField()
    seihu = models.IntegerField()
    check = models.IntegerField()
    total = models.IntegerField()
    def __str__(self):
        return self.kuname

class Sisyokyuu(models.Model):
    kuid = models.IntegerField(primary_key=True)
    kuname = models.CharField(max_length=30)
    question1 = models.CharField(max_length=100)
    syutudai = models.IntegerField()
    seihu = models.IntegerField()
    check = models.IntegerField()
    total = models.IntegerField()
    def __str__(self):
        return self.kuname
