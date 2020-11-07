from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar


def index(request):
    posts=[{
            "post_title":'Man must explore, and this is exploration at its greatest',
            "sub_title":"Problems look mighty small from 150 miles up",
            "posted_by":"Start Bootstrap",
            "posted_date":'on September 25, 2019'
        },{
            "post_title":"I believe every human has a finite number of heartbeats. I don't intend to waste any of mine.",
            "sub_title":"Problems look mighty small from 150 miles up",
            "posted_by":"Start Bootstrap",
            "posted_date":'on September 18, 2019'
        },{
            "post_title":"Science has not yet mastered prophecy",
            "sub_title":"We predict too much for the next year and yet far too little for the next ten.",
            "posted_by":"Start Bootstrap",
            "posted_date":'on August 24, 2019'
        },{
            "post_title":'Failure is not an option',
            "sub_title":"Many say exploration is part of our destiny, but it’s actually our duty to future generations.",
            "posted_by":"Start Bootstrap",
            "posted_date":'on July 8, 2019'
        }]
    
    return render(request, 'blogs/index.html', {"posts":posts})

def about(request):
    return render(request,"blogs/about.html")

def contact(request):
    return render(request,"blogs/contact.html")

def post(request):
    return render(request,"blogs/post.html")