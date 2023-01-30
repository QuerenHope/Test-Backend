from django.urls import path
from .views import CnabView

urlpatterns = [path("cnab/", CnabView.as_view(), name="cnab")]
