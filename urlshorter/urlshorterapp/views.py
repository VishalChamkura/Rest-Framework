from django.shortcuts import render
from .models import Urlmodel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect

@api_view(["POST"])
def Createshorturl(request):
    longurl = request.data["longurl"]
    urlmodel = Urlmodel(longurl=longurl)
    urlmodel.save()
    shorturl = urlmodel.shorturl
    return Response(shorturl)


@api_view(["GET,POST"])
def RedirectToLongurl(request,shorturl):
    urlmodel = Urlmodel.objeccts.get(shorturl=shorturl)
    return redirect(urlmodel.longurl) 