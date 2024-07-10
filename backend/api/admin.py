from django.contrib import admin
from .models import Category, Subcategory, Problem, Submission

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Problem)
admin.site.register(Submission)
