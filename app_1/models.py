from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Book(models.Model):
    book_status=[
        ('availble','availble'),
        ('rented','rented'),
        ('sold','sold')
    ]
    period=[
        ('الساعه','الساعه'),
        ('السنه','السنه'),
        ('اليوم','اليوم')
    ]
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='photos',null=True,blank=True)
    photo_author=models.ImageField(upload_to='photos',null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    retal_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    retal_period_type=models.CharField(null=True,blank=True,max_length=50,choices=period)
    active=models.BooleanField(default=True)
    status=models.CharField(null=True,blank=True,max_length=50,choices=book_status)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self) :
        return self.title