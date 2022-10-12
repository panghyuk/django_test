from django.shortcuts import render
from restaurant import out
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@api_view(['POST'])
@csrf_exempt
def sang1F(request):
    menu = out.sangrok1()
    res = {
        "version" : "2.0",
        "template" : {
            "outputs" : [
                {
                    "simpleText" :{
                        "text" : menu
                    }
                }
            ],
        }
    }
    return JsonResponse(res)


