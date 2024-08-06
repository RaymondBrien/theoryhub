from django.db import models

# Create your models here.
class About(models.Model):
    """
    Stores title and description for welcome page
    """
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    class Meta:
        verbose_name_plural = "About"
    def __str__(self):
        return self.title
    