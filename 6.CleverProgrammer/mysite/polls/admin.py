from django.contrib import admin
from. models import Question, Choice
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra =1
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text', ]
    inlines =[ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)