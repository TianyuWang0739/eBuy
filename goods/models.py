from django.db import models

# Create the goods category model here.
class GoodsCategory(models.Model):
   # The name of categorary
   gc_name=models.CharField(max_length=50)
   # The sample of categorary
   gc_sam=models.CharField(max_length=50)
   # The picture of categorary
   gc_pic=models.ImageField(upload_to='categorary')

# Create the goods information model here.
class GoodsInfo(models.Model):
   # The name of goods
   gi_name=models.CharField(max_length=50)
   # The proce of goods
   gi_price=models.IntegerField(default=0)
   # The description of goods
   gi_des=models.CharField(max_length=3000)
   # The picture of goods
   gi_pic=models.ImageField(upload_to='goods')
   # The category of goods
   gi_cag=models.ForeignKey('GoodsCategory')
