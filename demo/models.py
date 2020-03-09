from django.db import models

# Create your models here.
class image(models.Model):
    # 路径
    file_Path = models.CharField(max_length=32)