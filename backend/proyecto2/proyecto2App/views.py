from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

from proyecto2App.serializers import LoginSerializer, RegistroSerializer, DocumentoSerializer
from proyecto2App.db import getLogin, setRegistro, setRegistrarDoc, getValidarDoc

@api_view(["POST"])
def login(request): 
  try:
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data_serializer = LoginSerializer(data=data)
        if data_serializer.is_valid():
            getLogin(data["usuario"], data["clave"])
            return JsonResponse({'response': 'ok'}, status=status.HTTP_201_CREATED) 
        return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except ValueError as e: 
    return Response(e.args[0], status.HTTP_404_NOT_FOUND)  

@api_view(["POST"])
def registro(request): 
  try:
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data_serializer = RegistroSerializer(data=data)
        if data_serializer.is_valid():
            setRegistro(data["nombres"], data["apellidos"], data["usuario"], data["clave"])
            return JsonResponse({'response': 'ok'}, status=status.HTTP_201_CREATED) 
        return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except ValueError as e: 
    return Response(e.args[0], status.HTTP_404_NOT_FOUND)  

@api_view(["POST"])
def registrardoc(request): 
  try:
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data_serializer = RegistroSerializer(data=data)
        if data_serializer.is_valid():
            codigo = setRegistrarDoc(data["dochash"])
            return JsonResponse({'codigo': codigo}, status=status.HTTP_201_CREATED) 
        return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except ValueError as e: 
    return Response(e.args[0], status.HTTP_404_NOT_FOUND)  

@api_view(["POST"])
def validardoc(request): 
  try:
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data_serializer = RegistroSerializer(data=data)
        if data_serializer.is_valid():
            valido = getValidarDoc(data["dochash"], data["codigo"])
            return JsonResponse({'valido': valido}, status=status.HTTP_201_CREATED) 
        return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except ValueError as e: 
    return Response(e.args[0], status.HTTP_404_NOT_FOUND) 


@api_view(["GET"])
def holimundo(self): 
  try:
    response = {
      'response': 'holi mundo desde api'
    }
    return JsonResponse(response)
  except ValueError as e: 
    return Response(e.args[0], status.HTTP_404_NOT_FOUND)
