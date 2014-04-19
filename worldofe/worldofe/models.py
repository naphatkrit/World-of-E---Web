from django.db import models
class Base(models.Model):
    text = models.CharField(max_length=20)
    moretext = models.TextField()
    some_more_text = models.TextField()
