from django.db import models

# Create your models here.
        
class Image(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='Image-Galary')
    #type = models.ForeignKey(Catagory, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name


class Personal_information(models.Model):
    name = models.CharField(max_length=50)
    personal_details = models.TextField()
    profile_image = models.ImageField(upload_to='personal_folder')

    def __str__(self):
        return self.name
