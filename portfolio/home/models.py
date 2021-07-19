from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_desc
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=600, default="https://s3.amazonaws.com/ODNUploads/532dfdbcc6479placeholder_food_item_2.png") 

    def get_absolute_url(self):
            return reverse("home:detail", kwargs={"pk": self.pk})