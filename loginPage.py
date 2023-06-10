from os import system, name
import time
class User():
    def __init__(self,userName,isAdmin,hospital_id=None,slotId=None,date=None) -> None:
        self.userName = userName
        self.isAdmin= isAdmin
        self.slotId = slotId
        self.hospitalId = hospital_id
        self.vaccinatedDate = date
        

class startPage():
    def __init__(self,dbCursor,db):
        self.hmcursor = dbCursor
        self.hmdb = db
        
    def check_credentials(self,username,password):
        pass
    
    def credential_prompt(self):
        Case = int(input("[1] : Login \n [2] : signUp \n Enter[1/2] : "))
        if (Case == 1):
            username = input("UserName : ")
            password = input("PassWord : ")
            result = self.check_credentials(username, password)
            return result
        
    def login_page(self):
            status = self.credential_prompt()
            if (status == 0):
                caseRetry = ("Wanna give a try again [y/n] : ")
                if (caseRetry is ['y' or 'Y']):
                    self.credential_prompt()
                else:
                    system('clear')
                    print("quitting .. ")
                    exit()
            else:
                
            
if __name__  == "__main__":
    startPage.login_page()