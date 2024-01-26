from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    assign_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f'{self.title} {self.is_complete}'
