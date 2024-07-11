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
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    constraints = models.TextField()
    difficulty = models.IntegerField(choices=[
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Hard'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='problems', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(Subcategory, related_name='problems', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title

class Example(models.Model):
    content = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    problem = models.ForeignKey(Problem, related_name='examples', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Example ID: {self.id}, Problem ID: {self.problem.id}'

class Submission(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    problem = models.ForeignKey(Problem, related_name='submissions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Submission ID: {self.id}, Problem ID: {self.problem.id}, User ID: {self.user.id}'
