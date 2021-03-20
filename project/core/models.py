from django.db import models

class Post(models.Model):
    image_type = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image