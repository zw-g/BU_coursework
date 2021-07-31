key_words = [
    ['depress', 'sad', 'down'],
    ['conflict', 'argument', 'mistreat', 'quarrel'],
    ['drug', 'alcohol', 'drink', 'cocaine', 'opioid', 'heroin']]

def get_complaint_type(a_user_complaint):
    my_set=set()
    index = 0
    for list_element in key_words:
        for element in list_element:
            if element in a_user_complaint.lower():
                my_set.add(index)
                break
        index = index + 1
    return my_set
