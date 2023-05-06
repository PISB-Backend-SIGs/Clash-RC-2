from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(models.Question)
class QuestionAdmin (admin.ModelAdmin):
    list_display = ("q_id","questionNumber","q_title","isForJuniors")
admin.site.register(Question,QuestionAdmin)

class PlayerAdmin (admin.ModelAdmin):
    list_display = ("user","p_score","p_is_started","p_is_junior","p_is_loged_in")
admin.site.register(Player,PlayerAdmin)

class SubmissionAdmin (admin.ModelAdmin):
    list_display = ("team","player","q_id","q_status")
admin.site.register(Submission,SubmissionAdmin)

class TestcasesAdmin (admin.ModelAdmin):
    list_display = ("q_id","t_id")
admin.site.register(Testcases,TestcasesAdmin)

class TeamAdmin (admin.ModelAdmin):
    list_display = ("id","user_names","team_score","team_attempted")
    # list_display = ("team_id","user1","user2","team_score")
admin.site.register(Team,TeamAdmin)

class Contest_timeAdmin (admin.ModelAdmin):
    list_display = ("id","start_time","end_time")
    # list_display = ("team_id","user1","user2","team_score")
admin.site.register(Contest_time,Contest_timeAdmin)



