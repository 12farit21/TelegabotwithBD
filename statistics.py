import funcDatabase
def get_statistics(user_id):
    topic_name_list=["variable_name_correct", "variable_name_wrong", "if_correct", "if_wrong", "for_correct", "for_wrong", "while_correct", "while_wrong"]
    #variable_name_correct variable_name_wrong    if_correct if_wrong for_correct for_wrong while_correct while_wrong
    for i in range(0,len(topic_name_list)):
        topic_name=topic_name_list[i]
        value=funcDatabase.get_db_user_topic(user_id,topic_name)
        if i == 0: variable_name_correct=value
        if i == 1: variable_name_wrong=value
        if i == 2: if_correct=value
        if i == 3: if_wrong=value
        if i == 4: for_correct=value
        if i == 5: for_wrong=value
        if i == 6: while_correct=value
        if i == 7: while_wrong=value
    try:
        variable_procent=str(round(((variable_name_correct/(variable_name_correct+variable_name_wrong))*100),2))+"%"
    except:
        variable_procent="0%"
    
    try:
        if_procent=str(round(((if_correct/(if_correct+if_wrong))*100),2))+"%"
    except:
        if_procent="0%"
        
    try:
        for_procent=str(round(((for_correct/(for_correct+for_wrong))*100),2))+"%"
    except:
        for_procent="0%"
    
    try:
        while_procent=str(round(((while_correct/(while_correct+while_wrong))*100),2))+"%"
    except:
        while_procent="0%"
    return variable_procent,if_procent,for_procent,while_procent
    
