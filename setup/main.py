import psycopg2
from os import system,name

def init_slot_book(name):
    mycursor.execute("""create table %s_booked_slots(
    bookingId int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    user varchar(255) NOT NULL ,
    SlotId int,
    time_begin varchar(255) NOT NULL ,
    time_end varchar(255) NOT NULL,
    isApproved int,
    isVaccinated int
    )""",(name,))
    mydb.commit()
    
def init_hospital_table():
    mycursor.execute("""create table hospitals(
    hospitalId int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    hospitalName varchar(255) NOT NULL UNIQUE,
    hospitalAdmin varchar(255) NOT NULL
    )""")
    
def init_table(name):
    mycursor.execute("""create table users(
    userId int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    username varchar(255) NOT NULL UNIQUE,
    password varchar(255) NOT NULL,
    isAdmin int NOT NULL
    )""")
    mycursor.execute("""create table hospitals(
    hospitalId int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    hospitalName varchar(255) NOT NULL UNIQUE,
    hospitalAdmin varchar(255) NOT NULL,
    )""")