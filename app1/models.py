from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone


# Create your models here.
# question model
class Question(models.Model):
    q_id = models.IntegerField(primary_key=True)
    q_title = models.CharField(max_length=40)
    q_descrp =models.TextField()
    q_ip_formate = models.TextField(null=True,blank=True)
    q_op_formate = models.TextField(null=True,blank=True)
    q_const = models.TextField(null=True,blank=True)
    q_sip = models.TextField(null=True,blank=True)
    q_sop = models.TextField(null=True,blank=True)
    q_diff_level = models.CharField( max_length=50)
    q_point = models.IntegerField(default=0)
    q_aqrcy = models.IntegerField(default=0)
    q_subns = models.IntegerField(default=0)
    q_time_limit = models.IntegerField(null=True,default=1)
    q_memory_limit = models.IntegerField(null=True,default=50000)
    def __str__(self):
        return f"{self.q_id}"

class Testcases(models.Model):
    q_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    t_id = models.IntegerField(null=True)
    t_ip = models.TextField(null=True)
    t_op = models.TextField(null=True) 
    def __str__(self):
        return f"{self.q_id}"
    
# import uuid
# class UniqueId(models.Model):
#     p_id = models.UUIDField(primary_key=True,unique=True ,default=uuid.uuid4, editable=False)

#     class Meta:
#         abstract = True   


class Player(models.Model):
    # temp = models.TextField(default = "-1")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    p_id = models.BigAutoField(primary_key=True,unique=True)
    p_score = models.IntegerField(default=0)
    p_is_started = models.BooleanField(default=False)
    p_start_time = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.user}"
    


class Submission(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    q_id = models.IntegerField(null=True)
    # q_num=models.ForeignKey(Question, on_delete=models.CASCADE) 
    # player=models.CharField( max_length=50)

    s_code = models.TextField(null=True)
    s_pt = models.IntegerField(default=0)
    s_time= models.DateTimeField(default = timezone.now)
    # s_time = models.TimeField(auto_now=False, auto_now_add=False)
    # iscorrect = models.BooleanField(default=False)

    q_chices = (
        ('TLE','Time Limit Exceeded'),
    	('MLE','Memory Limit Exceeded'), 	
        ('CE','Compilation Error'),
        ('RE','Runtime Error'),
        ('AC' ,'Accepted'),
    )
    q_stat = models.CharField(max_length=5,choices=q_chices,null=True)

    def __str__(self):
        return f"{self.player}"
    
