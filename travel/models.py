from django.db import models

# Create your models here.


class travel(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to = 'pics')
    offer = models.BooleanField(default=False)

    class Meta:
        db_table = 'travel'