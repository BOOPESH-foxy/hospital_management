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
        self.count = 0
        
    def check_credentials(self,username,password):
        selectQuery = "select isadmin from authentication where username like %s and password like %s"
        data = (username,password)
        self.hmcursor.execute(selectQuery,data)
        isUser = hmcursor.fetchall()
        if(isUser):
            return isUser
        else:
            return 0
        
    def inserInto(self,name,password):
        self.hmcursor.execute("insert into authentication(username,password,isadmin) values(%s,%s,{0})".format(False),(name,password))
        print("signed up successfully")
        self.hmdb.commit()
        
    def credential_prompt(self):
        self.count +=1
        Case = int(input("[1] : Login \n[2] : signUp\nEnter[1/2] : "))
        if (Case == 1):
            self.username = str(input("UserName : "))
            password = pwinput.pwinput(prompt="PassWord : ",mask="*")
            result = self.check_credentials(self.username, password)
            return result
        if (Case == 2):
            system('clear')
            name = input("Enter username: ")
            password = pwinput.pwinput(prompt="Password : ",mask="*")
            ReEntered = pwinput.pwinput(prompt="Re-enter new password : ",mask="*")
            if (password == ReEntered):
                self.inserInto(name, password)
                system('clear')
                time.sleep(1)
                choise = input("wanna get home ? [y/n] :")
                if choise in ['y' or 'Y']:
                    self.credential_prompt()
                else:
                    exit()
            else:
                print("password doesn't match :")
        else:
            print("Invalid option ..")
            time.sleep(1)
            system('clear')
            if (self.count > 3):
                print("Too many attempts")
                exit()
            self.credential_prompt()

    def login_page(self):
            status = self.credential_prompt()
            print("status :",status)
            if (status == None):
                system('clear')
                caseRetry = input("Failed !! \n Wanna give a try again [y/n] : ")
                if caseRetry in ['y' or 'Y']:
                    system('clear')
                    self.credential_prompt()
                else:
                    system('clear')
                    print("quitting .. ")
                    time.sleep(2)
                    system('clear')
                    
            elif(status[0][0] == True):
                system('clear')
                print("WELCOME ADMIN {0}!".format(self.username).capitalize().upper())
                
            elif(status[0][0] == False):
                system('clear')
                print("welcome user {0} !".format(self.username).capitalize().upper())
                
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
