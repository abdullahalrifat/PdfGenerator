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


