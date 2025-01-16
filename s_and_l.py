import os 
import json 
import datatime from datatime 



class save_and_load () : 
    

    def get_info (self) :  
        self.data ={} 
        print (f"enter ur task name :\n")
        task = input ()
        self.data["task"] = task
        # find time till dead_line 
    
        time = input ("what is ur dead line with ( yyyy,mm,dd  format)  :\n")
        user_date = datetime.strptime(time , "%Y-%m,%d")
        differ = user_date - datetime.now()
        self.data["dead_line"] = differ 

        load(self.data)
        save(self.data)
        return self.data 




    def load(self,file) :
         self.file_name  = file 
         try:
            if os.path.exists(self.file_name):
                 with open(self.file_name , 'r') as F  :
                    self.file_name = json.load (F) 
                    return [] , self.file_name 
         except IOError:
             print("somthing else went wrong when opening file!")
    def save (self , packet ) : 
        self.Packet = packet 
        with open (self.Packet , 'w') as F :
            json.dumm(self.Packet , F , indent=4 )

    



        
