from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Item(models.Model):
    list = models.ForeignKey(List, on_delete = models.CASCADE)
    content = models.CharField(max_length=50)
    is_urgent = models.BooleanField(default=False)

    def __str__(self):
        if self.is_urgent:
            return str(self.list) + ' | ' + self.content + ' | ' + "URGENT"
        else:
            return str(self.list) + ' | ' + self.content
