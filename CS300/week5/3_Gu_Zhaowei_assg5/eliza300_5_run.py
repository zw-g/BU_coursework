import eliza300_5_functions
import eliza300_5_runtime_data
'''
key_words = [
    ['depress', 'sad', 'down'],
    ['conflict', 'argument', 'mistreat', 'quarrel'],
    ['drug', 'alcohol', 'drink', 'cocaine', 'opioid', 'heroin']]
'''
advice_per_type = [
    ['Get out more.', 'Take up a hobby that you love.'],
    ["Don't expect too much of people.", "Don't take offence easily."],
    ['Get counseling.', "Don't delay action on counseling."]]

# (Welcome): Postcondition 1

print("Thank you for using Eliza300, a fun therapy program.")

# (user_complaint): Postcondition 2

print("Please state your complaint:")
user_complaint = input()

# (observed_complaint_type): Postcondition 3

observed_complaint_type = eliza300_5_functions.get_complaint_type(user_complaint)

# (Advice displayed): Postcondition 4
#print(eliza300_5_runtime_data.key_words)
#print (key_words)

if len(observed_complaint_type) > 0:
    for i in range(len(eliza300_5_runtime_data.key_words)):
        if i in observed_complaint_type:
            for advice in advice_per_type[i]:
                print(advice)
import sys
sys.exit()
