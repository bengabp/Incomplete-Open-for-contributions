from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import random
from ifitx2 import settings
import requests
import json
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import FavouriteMentalItem
from django.db.utils import IntegrityError


API_REQUEST_HEADER = {'X-Api-Key': 'PgFylBH/Hd/eta7EG4joNQ==AtYtFDxo8Jr0vZp9'}

def get_facts(request):
    print("Getting facts..")
    url = "https://api.api-ninjas.com/v1/facts?limit=100"

    response = requests.request("GET", url, headers=API_REQUEST_HEADER)
    print("facts 1")
    response2 = requests.request("GET",url,headers=API_REQUEST_HEADER)
    print("facts2")

    r = []

    for g in [response,response2]:
        try:
            r.extend(g.json())
        except:
            print(r)

    unique_hashes = [favitem.unique_hash for favitem in request.user.favouritementalitem_set.all()]

    return JsonResponse({"results":r,"unique_hashes":unique_hashes},safe=False)


def get_riddles(request):
    url = "https://api.api-ninjas.com/v1/riddles?limit=30"
    response = requests.request("GET", url, headers=API_REQUEST_HEADER)
    response2 = requests.request("GET",url,headers=API_REQUEST_HEADER)

    r = []

    for g in [response,response2]:
        try:
            r.extend(g.json())
        except:
            print(r)

    unique_hashes = [favitem.unique_hash for favitem in request.user.favouritementalitem_set.all()]

    return JsonResponse({"results":r,"unique_hashes":unique_hashes},safe=False)


def get_jokes(request):
    url = "https://api.api-ninjas.com/v1/jokes?limit=30"
    response = requests.request("GET", url, headers=API_REQUEST_HEADER)
    response2 = requests.request("GET",url,headers=API_REQUEST_HEADER)

    r = []

    for g in [response,response2]:
        try:
            r.extend(g.json())
        except:
            print(r)

    unique_hashes = [favitem.unique_hash for favitem in request.user.favouritementalitem_set.all()]
    return JsonResponse({"results":r,"unique_hashes":unique_hashes},safe=False)

def get_quotes(request):
    url = "https://api.api-ninjas.com/v1/quotes?limit=100"
    response = requests.request("GET", url, headers=API_REQUEST_HEADER)
    response2 = requests.request("GET",url,headers=API_REQUEST_HEADER)

    r = []

    for g in [response,response2]:
        try:
            r.extend(g.json())
        except:
            print(r)

    unique_hashes = [favitem.unique_hash for favitem in request.user.favouritementalitem_set.all()]
    return JsonResponse({"results":r,"unique_hashes":unique_hashes},safe=False)

# Create your views here.
def dashboard(request):
    return render(request,"ifit_main/dashboard.html",{
        'iter':[
            "#022B3A",
            "#780000",
            "#00509d",
            "#022B3A",
            "var(--icon-button-bg-color)"
        ]
    })



def fitness(request):
    if request.method == "POST":
        return HttpResponse("Post fitness")

    url = "https://api.pexels.com/videos/search?query=workout&size=small&orientation=square&per_page=50"

    payload={}
    headers = {
    'Authorization': settings.PEXELS_API_KEY,
    'Cookie': '__cf_bm=On7yF39Uz_0bYS0Olw7aOMOEEVpLImEF4_5odaFpcdo-1668961001-0-AclWqFLl3YNbJ33qjQ/2aLFwXtetO+6iBLjuJDQlIL1IS063/0/lsL+XcusBe3YRU0ujjTdhPtDDCJSGr6+P2so='
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response = response.json()

    with open("response.json",'w') as f:
        json.dump(response,f,indent=4)

    context = {
        "categories":['Gym','Fitness','Excercise','Yoga','Running','Weights','Body Building'],
        'range':range(20)
    }

    return render(request,"ifit_main/fitness.html",context)

@csrf_exempt
def favourites(request):
    print(request.user)
    if request.method == "POST":
        category = request.POST.get("category")
        print(request.POST)
        message = "Invalid category"
        print("Category",category)

        if category in ["riddle","fact","joke","quote"]:
            unique_hash = request.POST.get("hash")
            if category == "riddle":
                riddle = request.POST.get("riddle")
                answer = request.POST.get("answer")
                try:
                    new_favourite_riddle = FavouriteMentalItem(riddle=riddle,answer=answer,user=request.user,category=category,unique_hash=unique_hash)
                    new_favourite_riddle.save()
                    return JsonResponse({
                        "message":"Starred successfully !"
                    })

                except IntegrityError:
                    return JsonResponse({
                        "message":"Starred Already !"
                    })


            elif category == "fact":
                fact = request.POST.get("fact")
                try:
                    new_favourite_fact = FavouriteMentalItem(fact=fact,user=request.user,category=category,unique_hash=unique_hash)
                    new_favourite_fact.save()
                    return JsonResponse({
                        "message":"Starred successfully !"
                    })

                except IntegrityError:
                    return JsonResponse({
                        "message":"Starred Already !"
                    })

            elif category == "joke":
                joke = request.POST.get("joke")
                try:
                    new_favourite_joke = FavouriteMentalItem(joke=joke,category=category,user=request.user,unique_hash=unique_hash)
                    new_favourite_joke.save()
                    return JsonResponse({
                        "message":"Starred successfully !"
                    })
                
                except IntegrityError:
                    return JsonResponse({
                        "message":"Starred Already !"
                    })

            elif category == "quote":
                quote = request.POST.get("quote")
                author = request.POST.get("author")
                try:
                    new_favourite_quote = FavouriteMentalItem(quote=quote,author=author,user=request.user,category=category,unique_hash=unique_hash)
                    new_favourite_quote.save()
                    return JsonResponse({
                        "message":"Starred successfully !"
                    })
                
                except IntegrityError:
                    return JsonResponse({
                        "message":"Starred Already !"
                    })

        return JsonResponse({
            "message":message
        })

    context = {
        "favitems":request.user.favouritementalitem_set.all()
    }
    return render(request,"ifit_main/favourites.html")


def receipes(request):
    if request.method == "POST":
        return HttpResponse("Post receipes")

    return render(request,"ifit_main/receipes.html")


def mental(request):
    if request.method == "POST":
        return HttpResponse("Post mental")

    datas = []

    context = {
        "categories":['Jokes',"Riddles",'Facts','Quotes'],
        'range':range(10),
        'datas':datas
    }

    return render(request,"ifit_main/mental.html",context)