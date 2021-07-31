import eliza300_5_runtime_data
eliza300_5_runtime_data.read_complaint_data()
#print(eliza300_5_runtime_data.key_words)
def get_complaint_type(a_user_complaint):
    my_set=set()
    index = 0
    for list_element in eliza300_5_runtime_data.key_words:
        for element in list_element:
            if element in a_user_complaint.lower():
                my_set.add(index)
                break
        index = index + 1
    return my_set
