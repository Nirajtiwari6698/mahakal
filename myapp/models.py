from _typeshed import Self
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

#DEPARTMENT
class Department(models.Model):
    code = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
#DEGREE
class Degree(models.Model):
    code = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.short_name 


#REGISTER
class UserInfo(models.Model):
    user = models.ForeignKey(User,unique=True)
    status = models.IntegerField(default=0) 
    department = models.ForeignKey(Department,null=True,blank=True)
    degree = models.ForeignKey(Degree,null=True,blank=True)
    roll_no = models.CharField(max_length=10,null=True,blank=True)
    year_of_admission = models.IntegerField(null=True,blank=True)
    stream = models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    phone_no = models.CharField(max_length=20,null=True,blank=True)
    personal_email = models.EmailField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    college_name = models.CharField(max_length=220)
    def __unicode__(self):
        return self.department.code +' '+str(self.year_of_admission)+self.degree.code + self.roll_no

# model for event
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=256)
    location = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    duration = models.CharField(max_length=20)
    content = models.TextField()
    contact = models.CharField(max_length=100)
    subscribed = ArrayField(models.IntegerField(), blank=True, null=True)

    def __str__(self):
        return self.event_name

#POLL
class Poll(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    yes_count = models.IntegerField(default=0)
    no_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.event_id)

# CONTACT FORM
class Contact(models.Model):
    name=models.CharField(max_length=220)
    email=models.EmailField(max_length=220)
    Description=models.CharField(220)
    contact_no=models.IntegerField()


    def __str__(self):
        return self.name
 #MODEL FOR ADMIN REGISTERATION 

class Admin_register(models.Model):
    name=models.CharField(max_length=220)
    email=models.EmailField()
    contact_no=models.IntegerField()
    designation=models.CharField(max_length=220)
    college=models.CharField(max_length=220)

# MODEL FOR POSTING ARTICLE

class Post_article(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Admin_register, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, default="")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title


# gallery

class Gallery(models.Model):
    photo = models.ImageField(upload_to ='uploads/')
    dept = models.CharField(max_length=220)
    description = models.CharField(max_length=220)
    date_upload = models.DateField(default=datetime.now)


# PAYMENT GATEWAY MODELS
class Pay(models.Model):
    amount = models.CharField(max_length=220)
    staus = models.BooleanField(default=False)
    donor_name = models.CharField(max_length=220)
    payment_id = models.CharField(max_length=50)
    def __str__():
        return Self.donor_name

#feedback and complain
class Feedback_Complain(models.Model):
    name = models.CharField(max_length=220)
    description = models.CharField(max_length=220)
    email = models.CharField(max_length=220)
    
