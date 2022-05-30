from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.
rating=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

service_choice=(
    (),
    (),
    (),
)

class contact_us(models.Model):
    name=models.CharField(verbose_name='Name',max_length=50)
    email=models.EmailField(verbose_name='Email Address',max_length=50,null=True)
    phone=models.CharField(max_length=12,verbose_name='Mobile Number')
    address=models.TextField(verbose_name='Address',null=True)
    #service_choice=models.CharField(choices=service_choice,max_length=50,verbose_name='Service choice')
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
    image=models.ImageField(upload_to='Media',null=True,verbose_name='Category Image')

    def __str__(self):
        return str(self.name)

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 500 or img.width > 400:
            new_img = (400, 500)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path

class service_sub_category(models.Model):
    cat_name=models.ForeignKey(service_category,on_delete=models.CASCADE,verbose_name='Category name')
    sub_cat_name=models.CharField(max_length=30,verbose_name='Sub Category Name')
    sub_descript=models.TextField(verbose_name='Sub Category Description')
    sub_img=models.ImageField(upload_to='Media',null=True,verbose_name='Sub Category Image')

    def __str__(self):
        return str(self.sub_cat_name)

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.sub_img.path) # Open image using self

        if img.height > 500 or img.width > 400:
            new_img = (400, 500)
            img.thumbnail(new_img)
            img.save(self.sub_img.path)  # saving image at the same path

class testimonials(models.Model):
    client_name=models.CharField(max_length=50,verbose_name='Client name')
    client_image=models.ImageField(upload_to='Media',null=True,verbose_name='Client Image')
    feedback=models.TextField(verbose_name='Feedback')
    date=models.DateField(default=timezone.now,verbose_name='Date')
    rating=models.CharField(max_length=1,choices=rating,verbose_name='Rating by client')

    def __str__(self):
        return str(self.client_name)

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.client_image.path) # Open image using self

        if img.height > 400 or img.width > 400:
            new_img = (400, 400)
            img.thumbnail(new_img)
            img.save(self.client_image.path)  # saving image at the same path

class feedback(models.Model):
    feed_name=models.CharField(verbose_name='Name',max_length=50)
    email=models.EmailField(verbose_name='Email Address',max_length=50,null=True)
    phone=models.CharField(max_length=12,verbose_name='Mobile Number')
    feedback=models.TextField(verbose_name='Feedback')
    rate=models.CharField(max_length=1,choices=rating,verbose_name='Rating')

    def __str__(self):
        return str(self.feed_name)

class team(models.Model):
    profile_pic=models.ImageField(upload_to='Media',null=True,verbose_name='Profile picture')
    name=models.CharField(verbose_name='Name',max_length=30)
    profession=models.CharField(max_length=30,verbose_name='Profession')
    description=models.TextField(verbose_name='Description')

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.profile_pic.path) # Open image using self

        if img.height > 400 or img.width > 400:
            new_img = (400, 400)
            img.thumbnail(new_img)
            img.save(self.profile_pic.path)  # saving image at the same path

    def __str__(self):
        return str(self.name)
class client(models.Model):
    name=models.CharField(max_length=50,verbose_name='Client Name')
    image=models.ImageField(upload_to='Media',verbose_name='Client Image')
    description=models.TextField(verbose_name='Description')
    project=models.CharField(max_length=100,verbose_name='Project name')

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 400 or img.width > 400:
            new_img = (400, 400)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path