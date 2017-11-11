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
    type=models.CharField(max_length=250)
    def __str__(self):
        return self.ex.url

class data(models.Model):
    #name,designation,company,contactno,email,address,interest1,interest2,interest3
    #['name', 'designation', 'company', 'contactno', 'email', 'address', 'interest1', 'interest2', 'interest3']
    FullName=models.TextField(max_length=1000)
    Company = models.TextField(max_length=1000)
    Position = models.TextField(max_length=1000)
    Interest1 = models.TextField(max_length=1000)
    Interest2 = models.TextField(max_length=1000)
    Interest3 = models.TextField(max_length=1000)
    Number=models.TextField(max_length=1000)
    def __str__(self):
        return self.FullName+' '+self.Number

