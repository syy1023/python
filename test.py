'''
def validate_pin(pin):


    if len(pin) == 4 or len(pin ) == 6:
        # return True
        for x in pin:
            if x.isdigit():
                #print(x)
                continue
            else:
                #print("Wrong output for" + x)
                return False
   # else:

      #  return False


print(validate_pin("12.0"))
print(validate_pin("120"))
print(validate_pin("1230"))


import re

def validate_pin(pin):
  return re.search('^(\d{4}|\d{6})$', pin) != None 

'''

import re

def validate_pin(pin):
  return re.search('^(\d{4}|\d{6})$', pin) != None


print(validate_pin("122222"))





