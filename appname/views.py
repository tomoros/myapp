
from django.shortcuts import render
import requests   # Web からデータを取ってくる時に使う
import bs4        # スクレイピング
import re
import xlrd
import random
from django.shortcuts import render
from django.http import HttpResponse
from appname.forms import KakikomiForm
import pygame
from appname.models import Kusyokyuu
from django.db.models import Sum

def appmain(request):
    pygame.mixer.init()
    pygame.mixer.music.load("appname/music/music.mp3")
    pygame.mixer.music.play(-1)
    return render(request, 'myapphome.html', {

    })
def appmain2(request):
    pygame.mixer.init()
    ku=Kusyokyuu.objects
    b=""
    if request.method == 'POST':
        answer = ku.values_list('kuname',flat=True).get(check=1)
        ku.all().update(check=0)
        b=corre(ku,answer,request.POST)
        if ku.aggregate(Sum('syutudai'))['syutudai__sum'] == 23:
            return render(request, 'answer1.html',{
                'word' : ku.aggregate(Sum('seihu'))['seihu__sum'],
                'nanido' : "初級"
            })
        rd = random.randint(1, 23)
        while ku.values_list('syutudai',flat=True).get(kuid=rd) ==  1:
            rd = random.randint(1, 23)
        ku.filter(kuid=rd).update(syutudai=1,check=1)

    else:
        rd=random.randint(1, 23);
        el(ku,rd)
    return render(request, 'syokyuu.html', {
        'answer' : ku.values_list('kuname',flat=True).get(kuid=rd),
        'hint'   : ku.values_list('question1',flat=True).get(kuid=rd),
        'form1': KakikomiForm(),
        'a' : b,
    })
def appmain3(request):
    pygame.mixer.init()
    ku=Kusyokyuu.objects
    b=""
    if request.method == 'POST':
        answer = ku.values_list('kuname',flat=True).get(check=1)
        ku.all().update(check=0)
        b=corre(ku,answer,request.POST)
        if ku.aggregate(Sum('syutudai'))['syutudai__sum'] == 23:
            return render(request, 'answer1.html',{
                'word' : ku.aggregate(Sum('seihu'))['seihu__sum'],
                'nanido' : "中級"
            })
        rd = random.randint(1, 23)
        while ku.values_list('syutudai',flat=True).get(kuid=rd) ==  1:
            rd = random.randint(1, 23)
        ku.filter(kuid=rd).update(syutudai=1,check=1)
    else:
        rd=random.randint(1, 23);
        el(ku,rd)
    return render(request, 'tyuukyuu.html', {
        'answer' : ku.values_list('kuname',flat=True).get(kuid=rd),
        'hint'   : ku.values_list('question2',flat=True).get(kuid=rd),
        'form1': KakikomiForm(),
        'a' : b,
    })
def appmain4(request):
    pygame.mixer.init()
    ku=Kusyokyuu.objects
    b=""
    if request.method == 'POST':
        answer = ku.values_list('kuname',flat=True).get(check=1)
        ku.all().update(check=0)
        b=corre(ku,answer,request.POST)
        if ku.aggregate(Sum('syutudai'))['syutudai__sum'] == 23:
            return render(request, 'answer1.html',{
                'word' : ku.aggregate(Sum('seihu'))['seihu__sum'],
                'nanido' : "上級"
            })
        rd = random.randint(1, 23)
        while ku.values_list('syutudai',flat=True).get(kuid=rd) ==  1:
            rd = random.randint(1, 23)
        ku.filter(kuid=rd).update(syutudai=1,check=1)
    else:
        rd=random.randint(1, 23);
        el(ku,rd)

    return render(request, 'zyoukyuu.html', {
        'answer' : ku.values_list('kuname',flat=True).get(kuid=rd),
        'hint'   : ku.values_list('question3',flat=True).get(kuid=rd),
        'form1': KakikomiForm(),
        'a' : b,
    })
def appmain5(request):
    pygame.mixer.init()
    ku=Kusyokyuu.objects
    b=""
    if request.method == 'POST':
        answer = ku.values_list('kuname',flat=True).get(check=1)
        ku.all().update(check=0)
        b=corre(ku,answer,request.POST)
        if ku.aggregate(Sum('syutudai'))['syutudai__sum'] == 23:
            return render(request, 'answer1.html',{
                'word' : ku.aggregate(Sum('seihu'))['seihu__sum'],
                'nanido' : "超級"
            })
        rd = random.randint(1, 23)
        while ku.values_list('syutudai',flat=True).get(kuid=rd) ==  1:
            rd = random.randint(1, 23)
        ku.filter(kuid=rd).update(syutudai=1,check=1)
    else:
        rd=random.randint(1, 23);
        el(ku,rd)

    return render(request, 'tyoukyuu.html', {
        'answer' : ku.values_list('kuname',flat=True).get(kuid=rd),
        'hint'   : ku.values_list('question4',flat=True).get(kuid=rd),
        'form1': KakikomiForm(),
        'a' : b,
    })
def kakikomi(request):
    f = KakikomiForm()
    return HttpResponse(f)

def corre(ku,answer,a):
    if a["答え"] == answer :
        ku.filter(kuname=answer).update(seihu=1)
        b ="正解"
        pygame.mixer.music.load("appname/music/correct2.mp3")
        pygame.mixer.music.play(1)
    else:
        b ="不正解"
        pygame.mixer.music.load("appname/music/incorrect1.mp3")
        pygame.mixer.music.play(1)
    return b
def el(ku,rd):
    ku.all().update(syutudai=0,seihu=0,check=0)
    pygame.mixer.music.load("appname/music/question1.mp3")
    pygame.mixer.music.play(1)
    ku.filter(kuid=rd).update(syutudai=1,check=1)
