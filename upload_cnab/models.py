from django.db import models
from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class UploadFile(models.Model):
    file_cnab = models.FileField(upload_to="uploads")


class CnabReader(models.Model):
    tipo = models.CharField(max_length=1)
    data = models.CharField(max_length=8)
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=8)
    dono_loja = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)
    cnab_file = models.ForeignKey(
        UploadFile, on_delete=models.CASCADE, related_name="cnabs"
    )
