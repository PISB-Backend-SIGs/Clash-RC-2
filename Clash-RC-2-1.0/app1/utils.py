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
        inner_dict={}
        if len(user_list)>=2:
            # print("one ele")
            # print(user_list[0].username)
            inner_dict["place"]=place+1
            inner_dict["user1"]=user_list[0].username
            inner_dict["user2"]=user_list[1].username
            inner_dict["score"]=team.team_score
            inner_dict["attempted_question"]=team.team_attempted
        else:
            inner_dict["place"]=place+1
            inner_dict["user1"]=user_list[0].username
            inner_dict["score"]=team.team_score
            inner_dict["attempted_question"]=team.team_attempted
        place += 1
        dict.append(inner_dict)
    # print(dict)
    return dict
