
from http.client import HTTPResponse
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
# Create your views here.
challenges = {
    "jan": "Jan",
    "feb": "feb",
    "mar": "mar",
    "apr": "apr",
    "may": "may",
    "jun": "jun",
    "jul": "jul",
    "aug": "aug",
    "sep": "sep",
    "oct": "oct",
    "nov": "nov",
    "dec": "dec",
}


def index(request):
    list_items = "<ul>"
    months = list(challenges.keys())
    for month in months:
        redirect_path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href='{redirect_path}'>{month.capitalize()}</a></li>"
    list_items += "</ul>"

    return render(request,'challenges/index.html',{
        'months':challenges,
    })


def monthly_challanges_by_number(request, month):
    months = list(challenges.keys())
    forward_month = None
    try:
        forward_month = months[month-1]
    except:
        return HttpResponseNotFound("Not valid url")

    redirect_path = reverse('month-challenge', args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challanges(request, month):
 
    try:
         
        return render(request, 'challenges/challange.html',{
            'text': challenges[month],
            'month': month
        })
    except:
        raise Http404()
        response = render_to_string('404.html')
        return HttpResponseNotFound(response)
