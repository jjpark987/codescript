from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self) -> str:
        return self.name

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    examples = models.TextField()
    example_images = models.ImageField(upload_to='images/')
    constraints = models.TextField()
    difficulty = models.CharField(max_length=10, choices=[
        ('EASY', 'Easy'), 
        ('MEDIUM', 'Medium'), 
        ('HARD', 'Hard'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='problem')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, related_name='problem')

    def __str__(self) -> str:
        return self.title

class Submission(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    analysis = models.TextField()
    score = models.IntegerField(null=True, blank=True, choices=[
        (1, 'Incorrect'),
        (2, 'Partially Correct'),
        (3, 'Correct'),
    ])

    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='submissions')

    def __str__(self) -> str:
        return self.title
