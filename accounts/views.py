from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status

from accounts.serializers import Registrationserializer
# Create your views here.


def __get_token(user):
    return get_object_or_404(Token, user=user).key



@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = Registrationserializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            context=serializer.data
            context['token'] = __get_token(account)
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


