from django.db import models
from blog.models import User

class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    pic=models.ImageField(upload_to="images/",null=True)
    title=models.CharField(max_length=250)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 