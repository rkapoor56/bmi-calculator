from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Entry


def home(request):
    context = {"title": "Index", "link": "/home"}
    return render(request, "home/user_input.html", context)


def save_user(request):
    name = request.GET["name"]
    ema = request.GET["email"]
    age1 = request.GET["age"]
    # below line will create and save a row in database
    entry = Entry.objects.create(name=name, email=ema, age=age1)
    return render(request, "home/bmi_input.html", {"id": entry.id})


def calc_bmi(request):
    user_id = int(request.GET["user_id"])
    weight = int(request.GET["weight"])
    height = int(request.GET["height"])
    bmi = float(weight / (height ** 2))
    entry = Entry.objects.get(pk=user_id)
    entry.bmi = bmi
    entry.save()
    return render(request, "home/bmi_result.html", {"bmi": bmi, "entry": entry})


def all_entries(request):
    entries = Entry.objects.all()
    return render(request, "home/entries.html", {"entries": entries})
