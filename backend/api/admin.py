from django.contrib import admin
from .models import Category, Subcategory, Problem, Example, Submission

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Problem)
admin.site.register(Example)
admin.site.register(Submission)
