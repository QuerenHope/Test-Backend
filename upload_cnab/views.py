from django.shortcuts import render
from .models import CnabReader, UploadFileForm
from rest_framework.views import APIView


class CnabView(APIView):
    ...
