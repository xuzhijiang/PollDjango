from django.contrib import admin
from .models import Question



class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
