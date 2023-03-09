from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat (request):
    return HttpResponse('<h1> virat is the best batsman in the world</h1>')

def anjali (request):
    return HttpResponse('<h1><marquee> HI my name is anjali. i am verymuch intersted to read books present i am reading book that is THE GIRL IN ROOM 105 which is written by the famous writter CHETAN BHAGAT</h1></marquee>')