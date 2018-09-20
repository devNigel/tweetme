from django.db import models
from django.conf import settings
from .validators import validate_content
from django.urls import reverse_lazy
# Create your models here.


class Tweet(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL)
    content=models.CharField(max_length= 140, validators=[validate_content])
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)
    
    def get_absolute_url(self):
        return reverse_lazy("tweet:detail", kwargs={"pk":self.pk})
    
    # def clean(self,*args,**kwargs):
    #     content=self.content
    #     if content=="abc":
    #         raise ValidationError("Cannot be ABC")
    #     return super(Tweet, self).clean(*args,**kwargs)