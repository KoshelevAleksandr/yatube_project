from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pud_date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
