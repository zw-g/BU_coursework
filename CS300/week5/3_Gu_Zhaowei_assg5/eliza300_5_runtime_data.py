complaint_types = []
key_words = []


def read_complaint_data():
    data_source = "ElizaData.txt"
    file = open(data_source, "r")
    line_read = file.readline().rstrip() # remove EOL
    while line_read != '':
        index_of_key = line_read.index("for")
        complaintSet = line_read[index_of_key+4:]
        complaint_types.append(complaintSet)
        line_read = file.readline().rstrip()

        key_wordsList = line_read.split(" ")
        key_words.append(key_wordsList)
        line_read = file.readline().rstrip()
    file.close()
    #return complaint_types
    #return key_words
    '''
    Intent: Get complaint_types and key_words from local ElizaData.txt

    Precondition =========

    ElizaData.txt is a local file consisting of paragraphs of the form

    On first line: 'Key Words for '<phrase describing a complaint category>
    On second line: <words, separated by blanks, that may occur within a
    description of the corresponding category>

    Example of ElizaData.txt:

    Key Words for Depression
    depress sad

    Key Words for Human Relations
    conflict argument mistreat

    Postconditions =========

    (1) complaint_types = list of the phrases in ElizaData.txt describing all
    complaint categories
    {2) key_words = list of lists of words in ElizaData.txt that may occur
    within phrases that describe the corresponding complaint category

    '''
'''
read_complaint_data()  # need to execute this here

print("Priting complaint_types and key_words from ...runtime_data...")
print(complaint_types)
print(key_words)
'''