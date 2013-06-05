from django.db import models
from django.contrib.auth.models import User
#from django.forms import ModelForm

class Annotation(models.Model):
    by_user = models.ForeignKey(User, related_name = 'by_user')
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length = 1000)
    comment = models.TextField()
    upVotes = models.IntegerField(default = 0)
    downVotes = models.IntegerField(default = 0)
    time = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.comment

#class PaperForm(ModelForm):
#    class Meta:
#        model = Paper
#        exclude = ['by_user']
