from django.db import models
from blog.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    content=models.TextField()
    author=models.CharField(max_length=40)
    slug=models.SlugField()
    timestamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title +" by "+self.author

