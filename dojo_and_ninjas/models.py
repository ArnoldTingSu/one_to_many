from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    state = models.CharField(max_length=2)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    name = models.CharField(max_length=225)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

