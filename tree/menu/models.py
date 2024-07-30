from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=100, null=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children',
                               on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        if self.url:
            url =  self.url
        else:
            url = self.parent.get_absolute_url() + self.named_url
        return reverse('menu_name', kwargs={'menu_url': url.lstrip('/')})