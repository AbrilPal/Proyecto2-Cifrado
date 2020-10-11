from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json


@api_view(["GET"])
def holimundo(self): 
  try:
    response = {
      'response': 'holi mundo desde api'
    }
    return JsonResponse(response)
  except ValueError as e: 
    return Response(e.args[0], status.HTTP_404_NOT_FOUND)
