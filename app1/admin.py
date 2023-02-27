from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(models.Question)
class QuestionAdmin (admin.ModelAdmin):
    list_display = ("q_id","q_title")
admin.site.register(Question,QuestionAdmin)

class PlayerAdmin (admin.ModelAdmin):
    list_display = ("user","p_score","p_is_started")
admin.site.register(Player,PlayerAdmin)

class SubmissionAdmin (admin.ModelAdmin):
    list_display = ("player","q_id","q_stat")
admin.site.register(Submission,SubmissionAdmin)

class TestcasesAdmin (admin.ModelAdmin):
    list_display = ("q_id","t_id")
admin.site.register(Testcases,TestcasesAdmin)


