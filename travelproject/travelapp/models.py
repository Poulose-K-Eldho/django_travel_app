from django.db import models

# Create your models here.
class foods(models.Model):
    name=models.CharField(max_length=80)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    img2=models.ImageField(upload_to='picture')
    img3 = models.ImageField(upload_to='picture')
    img4 = models.ImageField(upload_to='picture')
    img5 = models.ImageField(upload_to='picture')
    img6 = models.ImageField(upload_to='picture')
    img7 = models.ImageField(upload_to='picture')