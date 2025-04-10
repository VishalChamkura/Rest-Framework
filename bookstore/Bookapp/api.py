from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,Allowany,IsAdminuser
from rest_framework.decorators import permission_classes

@api_view(["POST"])
def Usercreateapi(request):
    username = request.data["username"]
    password = request.data["password"]

    User.objects.create_user(username=username,password=password)

    return Response({
        "massage":"user created"
    })

# @api_view(["POST"])
# def Userloginapi(request):
#     username = request.data["username"]
#     password = request.data["password"]

#     user = authenticate(username=username,passwoerd=password)

#     if user is not None:
#         login(request.user)

#         token,created = Token.objects.get_or_create(user=user)

#         return Response({
#         "massage":"userlogin in",
#         "Token":token.key
#         })
#     else:
#         return Response({
#             "massage":"Invalid Creaditials"
#         })
    

@api_view(["GET"])  
@permission_classes([IsAuthenticated])   #we can replace isauthenticated with allowany and only for admin user
def protectedView(request):
    if request.user.is_authenticated:
        return Response({
            "massage":"id already authenticated",
            "username":request.user.username
        })
    else:
        return Response({
            "massage":"Please login"
        })
