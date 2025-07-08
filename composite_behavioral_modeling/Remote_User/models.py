from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class identity_theft_detection(models.Model):

    Account_Id= models.CharField(max_length=300)
    Trans_Id= models.CharField(max_length=300)
    Age= models.CharField(max_length=300)
    Followers= models.CharField(max_length=300)
    NAME_CONTRACT_TYPE= models.CharField(max_length=300)
    GENDER= models.CharField(max_length=300)
    AMT_INCOME_TOTAL= models.CharField(max_length=300)
    AMT_CREDIT= models.CharField(max_length=300)
    AMT_ANNUITY= models.CharField(max_length=300)
    AMT_GOODS_PRICE= models.CharField(max_length=300)
    NAME_INCOME_TYPE= models.CharField(max_length=300)
    NAME_FAMILY_STATUS= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



