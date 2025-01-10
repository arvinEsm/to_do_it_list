from s_and_l import *
import time
from datetime import datetime



# global hashtag_value = 0 




#main menu 
def menu() : 
    button = input (f"what is ur desire ? \n\n1-add a new task : \n2-see ur situations : \n3-tasks u have done  :").strip()
    
    if button == '1' : 
    
        obj1 = save_and_load()
        show_task = obj1.get_info()
    
        print (f"{show_task} seccussfully added .\nur dead_line is in  : ")
        TT = obj1.get_info("time")
        print (f"TT\n")
        print ("warnning : ur delay has a serious consequences  . ") 

    

        Q = input (f"do u wanna back to main menu or quit programm  ? (yes/no) :\n").strip() 
            if Q == 'yes' : 
                def menu ()
            elif Q == "no" : 
                sys.exit() 


    if button == '2' :
       obj1 = save_and_load()
       pending = obj1.load(_, )
       print(f"below taskes is pending :  \n{pending}")













print(f"\n\n\n\n\n\nexact current time , for on_times legend\n  ")
current_time = datetime.now()
print("current_time ")
