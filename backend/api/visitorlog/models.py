from django.db import models

# Create your models here.
class Log(models.Model):
    in_time = models.DateTimeField(auto_now_add=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()

    def __str__(self) -> str:
        return '{} arrived at {}'.format(self.email, self.in_time)
