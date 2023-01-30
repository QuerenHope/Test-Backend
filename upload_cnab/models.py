from django.db import models
from django import forms


class UploadCnabFile(models.Model):
    file = models.FileField()


class UploadFileForm(forms.Form):
    file = forms.FileField()


class Cnab(models.Model):
    type = models.CharField(max_length=22)
    date = models.DateField(max_length=8)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    credit_card = models.CharField(max_length=12)
    hour = models.CharField(max_length=8)
    owner_shop = models.CharField(max_length=14)
    shop_name = models.CharField(max_length=19)
    cnab_file = models.ForeignKey(
        UploadCnabFile, on_delete=models.CASCADE, related_name="cnabs", null=True
    )


def __str__(self):
    return f"{self.nome} - {self.get_tipo_display()} - R$ {self.value}"
