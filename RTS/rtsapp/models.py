from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class VC_Hawks(models.Model):
    user  = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

class Tehsil(models.Model):
    tehsil_id = models.IntegerField(unique=True)
    tehsil_name = models.CharField(max_length=255)
    total_num_tehsil = models.IntegerField()

    def __str__(self):
        return f"{self.tehsil_name} (ID: {self.tehsil_id})"
class UC(models.Model):
    uc_id = models.IntegerField(unique = True)
    uc_name = models.CharField(max_length = 200,)
    totol_num_uc = models.IntegerField()
    tehsil_id = models.ForeignKey(Tehsil, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
class VC(models.Model):
    vc_id = models.IntegerField()
    vc_name = models.CharField(max_length = 200)
    total_num_vc = models.IntegerField()
    uc_id = models.ForeignKey(UC, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

  
