from app1.models import Question,Submission
from django.contrib.auth.models import User
def last_submission(submission_query_set):
    for submission in submission_query_set:
        last_element = submission.s_code
        print(last_element)
    return last_element



def get_leaderboard(team_set,user_set):
    place=0
    dict=[]
    for team in team_set:
        user_list=user_set.filter(team__id=team.id)
        inner_dict=[]
        if len(user_list)>=2:
            # print("one ele")
            # print(user_list[0].username)
            # inner_dict["place"]=place+1
            # inner_dict["user"]=user_list[0].username
            # inner_dict["user2"]=user_list[1].username
            # inner_dict["score"]=team.team_score
            # inner_dict["attempted_question"]=team.team_attempted
            # inner_dict["Time"]=team.teamTime
            inner_dict.append(place+1)
            inner_dict.append(f"{user_list[0].username} and {user_list[1].username}")
            inner_dict.append(team.team_score)
            inner_dict.append(team.team_attempted)
            # inner_dict.append(team.teamTime)

        else:
            inner_dict.append(place+1)
            inner_dict.append("{}".format(user_list[0].username))
            inner_dict.append(team.team_score)
            inner_dict.append(team.team_attempted)
            # inner_dict.append(team.teamTime)

        place += 1
        dict.append(inner_dict)
    # print(dict)
    return dict


def check_accuracy():
    questions= Question.objects.all()
    submissions = Submission.objects.all()
    for question in questions:
        actual_sub = len(submissions.filter(q_id=question.q_id))
        right_sub=len(submissions.filter(q_status="AC",q_id=question.q_id))
        try:
            accuracy = (right_sub/actual_sub)*100
            question.q_aqrcy = accuracy
            question.save()
        except:
            pass

# player==user
def check_solved(team):
    submissions = Submission.objects.filter(team=team,q_status="AC")
    ques_list = [str(x.q_id) for x in submissions ]
    # ques_list = []
    # for i in range(len(submissions)):
    #     qes = submissions[i].q_id
    #     # print(qes)
    #     if (qes not in ques_list):
    #         ques_list.append(qes)
    #     # print(i.q_id)
    # final_ques_list=[]
    # for i in ques_list:
    #     final_ques_list.append(str(i))
    #     # print(i)
    # print(final_ques_list)
    return set(ques_list)

#It will calculate score of that question for player
def calc_score(submissions):
    numberOfWrongSubmission = len(submissions.filter(q_status="WA"))
    numberOfRightSubmission = len(submissions.filter(q_status="AC"))
    marks_reduce = numberOfWrongSubmission*10
    return marks_reduce



def getQuestionSet(questionQuerySet,teamObject):
    questionList = []
    for i in questionQuerySet:
        questionDict = {}
        questionDict["id"] = i.questionNumber
        questionDict["questionTitle"] = i.q_title
        questionDict["questionAccuracy"] = i.q_aqrcy
        questionDict["questionSubmissions"] = i.q_subns
        try:
            if(Submission.objects.filter(team=teamObject,q_id=i.q_id,q_status="AC")):
                print("submission Done")
                questionDict["playerIsAttempted"]=True
            else:
                questionDict["playerIsAttempted"]=False
        except:
            questionDict["playerIsAttempted"]=False
            
        questionList.append(questionDict)
    # questionDict = dict(questionDict)
    # print(type(questionDict))
    return questionList