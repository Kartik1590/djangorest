from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class StreamingPlatform(models.Model):
    name=models.CharField(max_length=50)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title=models.CharField(max_length=50)
    storyline=models.TextField(blank=True)
    platform=models.ForeignKey(StreamingPlatform,on_delete=models.CASCADE,related_name="watchlist")
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200,null=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    Watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="review")
    
    def __str__(self):
        return str(self.rating) + "  -->  " + (self.Watchlist.title)