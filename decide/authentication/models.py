from django.db import models
from django.contrib.auth.models import User

# Create your models here

class UserDecide(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)
<<<<<<< HEAD
<<<<<<< HEAD

class TwoStepsAuth(models.Model):
    code = models.CharField(max_length = 192, unique = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, unique = True)
=======
>>>>>>> parent of 547151a... Navegabilidad impleentada
=======
>>>>>>> parent of 547151a... Navegabilidad impleentada
