from django.db import models

class Biznews(models.Model):
    biz_image=models.ImageField(upload_to='images/', blank=True)
    biz_date=models.DateField(max_length=200)
    biz_title=models.TextField(max_length=200)
    def __str__(self):
        return self.biz_title
class Doler(models.Model):
    do_image=models.ImageField(upload_to='images/', blank=True)
    do_date=models.DateField(max_length=200)
    do_title=models.TextField(max_length=200)
    def __str__(self):
        return self.do_title
class Breaking(models.Model):
    br_title=models.TextField(max_length=200)
    def __str__(self):
        return self.br_title

