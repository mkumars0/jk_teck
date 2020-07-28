from django.db import models

# Create your models here.
class RegisteredDetails(models.Model):
    name=models.CharField( max_length=255)
    email= models.EmailField(unique=True)
    poject_domain=models.CharField(max_length=255)
    project_name=models.CharField( max_length=255)
    phone_no=models.IntegerField()

    def __str__(self):
        return(self.name)
