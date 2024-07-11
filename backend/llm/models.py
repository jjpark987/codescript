from django.db import models
from api.models import Submission

class Response(models.Model):
    title = models.CharField(max_length=200)
    analysis = models.TextField()
    score = models.IntegerField(null=True, blank=True, choices=[
        (1, 'Incorrect'),
        (2, 'Partially Correct'),
        (3, 'Correct'),
    ])

    created_at = models.DateTimeField(auto_now_add=True)

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='response')

    def __str__(self):
        return f'Response ID: {self.id}, Submission ID: {self.submission.id}'
    