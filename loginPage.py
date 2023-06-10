from os import system, name
import time
import psycopg2
import pwinput


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
        selectQuery = "select isadmin from authentication where username like %s and password like %s"
        data = (username,password)
        print(self.hmcursor.execute(selectQuery,data))
        
    def credential_prompt(self):
        Case = int(input("[1] : Login \n[2] : signUp\nEnter[1/2] : "))
        if (Case == 1):
            username = str(input("UserName : "))
            password = pwinput.pwinput(prompt="PassWord : ",mask="*")
            result = self.check_credentials(username, password)
            return result
        
    def login_page(self):
            status = self.credential_prompt()
            if (status == 0):
                system('clear')
                caseRetry = input("Failed !! \n Wanna give a try again [y/n] : ")
                if (caseRetry =='y' or 'Y'):
                    system('clear')
                    self.credential_prompt()
                else:
                    system('clear')
                    print("quitting .. ")
            else:
                pass
            
if __name__  == "__main__":

    hmDb = psycopg2.connect(
        database = "hospital_management",
        user = "postgres",
        password = "new_password",
        host = "127.0.0.1",
        port = "5432"
    )
    hmcursor = hmDb.cursor()
    ClassObject = startPage(hmcursor,hmDb)
    ClassObject.login_page()
