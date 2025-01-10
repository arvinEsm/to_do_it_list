from lage import *



global hashtag_value = 0 




#main menu 
button = input (f"what is ur desire ? \n\n1-add a new task : \n2-see ur situations : \n3-tasks u have done  :").strip()
if button == '1' : 
    obj = lage() 
    obj.save_tasks() 




