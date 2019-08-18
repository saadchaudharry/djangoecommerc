from django.db import models

# Create your models here.
class product(models.Model):
    product_Id=models.AutoField
    product_Name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    catagory=models.CharField(max_length=400,default="")
    desc=models.CharField(max_length=300)
    product_date=models.DateField()
    prod_img=models.ImageField()


    def __str__(self):
        return self.product_Name