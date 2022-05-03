from django.db import models
from django.utils import timezone

# Create your models here.
rating=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

class contact_us(models.Model):
    name=models.CharField(verbose_name='Name',max_length=50)
    email=models.EmailField(verbose_name='Email Address',max_length=50,null=True)
    phone=models.CharField(max_length=12,verbose_name='Mobile Number')
    message=models.TextField(verbose_name='Message')

    def __str__(self):
        return str(self.name)

class about_us(models.Model):
    title=models.CharField(max_length=30,verbose_name='Title')
    description=models.TextField(verbose_name='Description')
    project_done=models.PositiveIntegerField(verbose_name='Project Done',default=0)
    happy_clients=models.PositiveIntegerField(verbose_name='Happy Clients',default=0)
    employee=models.PositiveIntegerField(verbose_name='Employee Count',default=0)

    def __str__(self):
        return str(self.title)

class service_category(models.Model):
    name=models.CharField(primary_key=True,max_length=50,unique=True,verbose_name='Category name')
    descript=models.TextField(verbose_name='Category Description')
    image=models.ImageField(upload_to='Media',verbose_name='Category Image')

    def __str__(self):
        return str(self.name)

class service_sub_category(models.Model):
    cat_name=models.ForeignKey(service_category,on_delete=models.CASCADE,verbose_name='Category name')
    sub_cat_name=models.CharField(max_length=30,verbose_name='Sub Category Name')
    sub_descript=models.TextField(verbose_name='Sub Category Description')
    sub_img=models.ImageField(upload_to='Media',verbose_name='Sub Category Image')

    def __str__(self):
        return str(self.sub_cat_name)

class testimonials(models.Model):
    client_name=models.CharField(max_length=50,verbose_name='Client name')
    client_image=models.ImageField(upload_to='Media',verbose_name='Client Image')
    feedback=models.TextField(verbose_name='Feedback')
    date=models.DateField(default=timezone.now,verbose_name='Date')
    rating=models.CharField(max_length=1,choices=rating,verbose_name='Rating by client')

    def __str__(self):
        return str(self.client_name)

class feedback(models.Model):
    feed_name=models.CharField(verbose_name='Name',max_length=50)
    email=models.EmailField(verbose_name='Email Address',max_length=50,null=True)
    phone=models.CharField(max_length=12,verbose_name='Mobile Number')
    feedback=models.TextField(verbose_name='Feedback')
    rate=models.CharField(max_length=1,choices=rating,verbose_name='Rating')

    def __str__(self):
        return str(self.feed_name)