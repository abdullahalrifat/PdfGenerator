from django.db import models
from django.core.urlresolvers import reverse


class pdf(models.Model):
    name=models.CharField(max_length=250)
    org=models.CharField(max_length=250)
    talk=models.CharField(max_length=1000)
    person_image=models.ImageField()

    def get_absolute_url(self):
        return reverse('pdf:view')

    def __str__(self):
        return self.name+' '+self.org+' '+ self.talk+' '+u'<img src="%s" />' % self.person_image.url



class Comment(models.Model):

    message = models.EmailField(max_length=1000)
    def __str__(self):
        return self.message


class verify(models.Model):
    password=models.TextField(max_length=1000)

    def __str__(self):
        return self.password


class excel(models.Model):
    ex=models.FileField()

    def __str__(self):
        return self.ex.url

class data(models.Model):
    #name,designation,company,contactno,email,address,interest1,interest2,interest3
    #['name', 'designation', 'company', 'contactno', 'email', 'address', 'interest1', 'interest2', 'interest3']
    name=models.TextField(max_length=1000)
    designation = models.TextField(max_length=1000)
    company = models.TextField(max_length=1000)
    contactno = models.TextField(max_length=1000)
    email = models.TextField(max_length=1000)
    address = models.TextField(max_length=1000)
    interest1 = models.TextField(max_length=1000)
    interest2 = models.TextField(max_length=1000)
    interest3 = models.TextField(max_length=1000)

    def __str__(self):
        return self.email

