import configparser
from pyfiglet import Figlet
import mysql.connector
import os
import sys

sb_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="simple_booking_db"
)

mycursor = sb_db.cursor()
# mycursor.execute("create database simple_booking_db")
# mycursor.execute("create table cus_reg (first_name varchar(255), last_name varchar(255), user_name varchar(255), age int(255), sex varchar(255), password varchar(255))")


title_o = Figlet(font="standard")
print(title_o.renderText("SiMplY   BooKinG"))

print("---------------------------------------------------------------------------------------------------------------------------\n")


def user_login(user_name, password):
    # pass_check = mycursor.execute("SELECT password FROM Where password?", (password))
    sql = "select * from cus_reg where user_name = %s and password = %s"
    mycursor.execute(sql, [(user_name), (password)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            print("Login Success")
            main_page()
            break
    else:
        print("User Does Not Exist")


def account_create(first_name, last_name, user_name, age, sex, password):
    sql = "insert into cus_reg (first_name,last_name,user_name, age, sex, password) values (%s,%s,%s,%s,%s,%s)"
    val = (first_name, last_name, user_name, age, sex, password)
    mycursor.execute(sql, val)
    sb_db.commit()
    print("Account Created Succesfully")


def edit_account():
    mycursor.execute('''
                UPDATE cus_reg
                SET user_name = "Sohailt18"
                WHERE first_name = "Sohail"
                ''')
    sb_db.commit()


def main_page():
    main_title = Figlet(font="digital")
    print(main_title.renderText(f"Welcome to Simply Booking {user_name}"))
    print("    1-Movie Booking        2 - Flight Booking\n")
    book_options = int(input("Choose Your Booking: "))
    if book_options == 1 or book_options == 2:
        if book_options == 1:
            movie_book()
        elif book_options == 2:
            flight_book()


def movie_book():
    print("Enjoy Online Ticket Booking for Movies in With Simply Booking")
    print("SELECT THE CITY\n \n1 - Chennai  2 - Madurai  3 - Coimbatore  4 - Trichy\n")
    choose_loc = int(input("Choose The Location: "))
    if choose_loc == 1 or choose_loc == 2 or choose_loc == 3 or choose_loc == 4:
        if choose_loc == 1:
            chennai_shows()
        elif choose_loc == 2:
            madurai_shows()
        elif choose_loc == 3:
            coimbatore_shows()
        elif choose_loc == 4:
            print("Sorry Currently Trichy Not Avilable For Booking")


def chennai_shows():
    print("Chennai Shows\n")
    print("AADUKALAM - (ADK)\n")
    print("MARUDHANAYAGAM - (MDG)\n")
    print("VINNAITHAANDI VARUVAAYA - (VTV)\n")
    print("PARUTHIVEERAN - (PTN)\n")
    chen_movie = input("Enter the Key For Movie: (Eg: VTV)\n")
    if chen_movie == "ADK":
        print("Theatres List: \n\n 1- ALBERT 4K - Egmore\n")
        print("AADUKALAM\nShow Timings\n")
        print("1- 10.30AM        2- 2.30PM        3- 6.30PM        4- 10.30PM\n\n")
        show_timee()

    elif chen_movie == "MDG":
        print("Theatres List: \n\n 1- WOODLANDS 4K - Royapettah\n")
        print("MARUDHANAYAGAM\nShow Timings\n")
        print("1- 10.30AM        2- 2.30PM        3- 6.30PM        4- 10.30PM\n\n")
        show_timee()

    elif chen_movie == "VTV":
        print("Theatres List: \n\n 1- KASI 4K - Ashok Nagar\n")
        print("VINNAITHAANDI VARUVAAYA\nShow Timings\n")
        print("1- 10.30AM        2- 2.30PM        3- 6.30PM        4- 10.30PM\n\n")
        show_timee()

    elif chen_movie == "PTN":
        print("Theatres List: \n\n 1- Rohini 4K - Koyambedu\n")
        print("PARUTHIVEERAN\nShow Timings\n")
        print("1- 10.30AM        2- 2.30PM        3- 6.30PM        4- 10.30PM\n\n")
        show_timee()


def madurai_shows():
    print("Madurai Shows\n")
    print("TITANIC - (TTC)\n")
    print("MAYAKKAM ENNA - (MYK)\n")
    print("AYAN - (AYN)\n")
    mdu_movie = input("Enter the Key For Movie: (Eg: VTV)\n")
    if mdu_movie == "TTC":
        print("Theatres List: \n\n 1- VETRI CINEMAS 4K - Villapuram\n")
        print("TITANIC\nShow Timings\n")
        print("1- 10.30AM        2- 2.30PM        3- 6.30PM        4- 10.30PM\n\n")
        show_timee()

    elif mdu_movie == "MYK":
        print("Theatres List: \n\n 1- INOX 4K - RaceCourse\n")
        print("MAYAKKAM ENNA\nShow Timings\n")
        print("1- 10.30AM        2- 2.30PM        3- 6.30PM        4- 10.30PM\n\n")
        show_timee()

    elif mdu_movie == "AYN":
        print("Theatres List: \n\n 1- CINIPRIYA 4K - Anna Bustand\n")
        print("AYAN\nShow Timings\n")
        print("1- 10.30AM        2- 2.30PM        3- 6.30PM        4- 10.30PM\n\n")
        show_timee()


def coimbatore_shows():
    print("Coimbatore Shows\n")
    print("SILLUNU ORU KADHAL - (SOK)\n")
    print("SIVA MANASULA SAKTHI - (SMS)\n")
    cbe_movie = input("Enter the Key For Movie: (Eg: VTV)\n")
    if cbe_movie == "SOK":
        print("Theatres List: \n\n 1- YAMUNA 4K\n")
        print("SILLUNU ORU KADHAL\nShow Timings\n")
        print("1- 10.30AM        2- 2.30PM        3- 6.30PM        4- 10.30PM\n\n")
        show_timee()

    elif cbe_movie == "SMS":
        print("Theatres List: \n\n 1- KG CINEMAS 4K\n")
        print("SIVA MANASULA SAKTHI\nShow Timings\n")
        print("1- 10.30AM        2- 2.30PM        3- 6.30PM        4- 10.30PM\n\n")
        show_timee()


def show_timee():
    show_time = int(input("Choose the Show Time: "))
    if show_time == 1 or show_time == 2 or show_time == 3 or show_time == 4:
        print("Ticket Price: Rs: 150/-\n")
        ticket_rate = 150
        how_many_tick = int(input("Enter How Many Tickets: \n"))
        total_tick = ticket_rate * how_many_tick
        print(f"\nTotal Ticket Price is Rs:{total_tick}/- \n")


def flight_book():
    print("Enjoy Online Ticket Booking for Flight in With Simply Booking\n")
    print("Only Under Tamil Nadu Flights are Booking\n")
    places = ["Chennai", "Madurai", "Trichy",
              "Coimbatore", "Salem", "Tutucorin"]
    departure = input("Enter the departure Place: \n")
    destination = input("Enter the Destination: \n")
    if departure in places and destination in places:
        print(f"\nYes {departure} to {destination} Flights are Available!\n")
        if departure == "Chennai" and destination == "Madurai":
            print("Your Flight Ticket Price is Rs/- 13555\n")
            confirm_ticket = input("Confirm Ticket Yes or No: \n")
            ticket_price = 13555
            if confirm_ticket == "Yes" or confirm_ticket == "No":
                if confirm_ticket == "Yes":
                    how_many_ticket = int(input("Enter How Many Ticket: \n"))
                    total_tic = how_many_ticket*ticket_price
                    print(f"Total Ticket Price is {total_tic}\n")
                elif confirm_ticket == "No":
                    return main_page()

        elif departure == "Madurai" and destination == "Salem":
            print("Your Flight Ticket Price is Rs/- 10555\n")
            confirm_ticket = input("Confirm Ticket Yes or No: \n")
            ticket_price = 10555
            if confirm_ticket == "Yes" or confirm_ticket == "No":
                if confirm_ticket == "Yes":
                    how_many_ticket = int(input("Enter How Many Ticket: \n"))
                    total_tic = how_many_ticket*ticket_price
                    print(f"Total Ticket Price is {total_tic}\n")
                elif confirm_ticket == "No":
                    return main_page()

        elif departure == "Trichy" and destination == "Chennai":
            print("Your Flight Ticket Price is Rs/- 9555")
            confirm_ticket = input("Confirm Ticket Yes or No: \n")
            ticket_price = 9555
            if confirm_ticket == "Yes" or confirm_ticket == "No":
                if confirm_ticket == "Yes":
                    how_many_ticket = int(input("Enter How Many Ticket: \n"))
                    total_tic = how_many_ticket*ticket_price
                    print(f"Total Ticket Price is {total_tic}\n")
                elif confirm_ticket == "No":
                    return main_page()

        elif departure == "Coimbatore" and destination == "Chennai":
            print("Your Flight Ticket Price is Rs/- 7555")
            confirm_ticket = input("Confirm Ticket Yes or No: \n")
            ticket_price = 7555
            if confirm_ticket == "Yes" or confirm_ticket == "No":
                if confirm_ticket == "Yes":
                    how_many_ticket = int(input("Enter How Many Ticket: \n"))
                    total_tic = how_many_ticket*ticket_price
                    print(f"Total Ticket Price is {total_tic}\n")
                elif confirm_ticket == "No":
                    return main_page()

        elif departure == "Salem" and destination == "Chennai":
            print("Your Flight Ticket Price is Rs/- 6555")
            confirm_ticket = input("Confirm Ticket Yes or No: \n")
            ticket_price = 6555
            if confirm_ticket == "Yes" or confirm_ticket == "No":
                if confirm_ticket == "Yes":
                    how_many_ticket = int(input("Enter How Many Ticket: \n"))
                    total_tic = how_many_ticket*ticket_price
                    print(f"Total Ticket Price is {total_tic}\n")
                elif confirm_ticket == "No":
                    return main_page()

        elif departure == "Tutucorin" and destination == "Chennai":
            print("Your Flight Ticket Price is Rs/- 5555")
            confirm_ticket = input("Confirm Ticket Yes or No: \n")
            ticket_price = 5555
            if confirm_ticket == "Yes" or confirm_ticket == "No":
                if confirm_ticket == "Yes":
                    how_many_ticket = int(input("Enter How Many Ticket: \n"))
                    total_tic = how_many_ticket*ticket_price
                    print(f"Total Ticket Price is {total_tic}\n")
                elif confirm_ticket == "No":
                    return main_page()


print("1 - Login \n2 - Create Account")
acc_option = input("Choose: ")

if acc_option == "1":
    user_name = input("Enter UserName: ")
    password = input("Enter Password: ")
    user_login(user_name, password)

if acc_option == "2":
    first_name = input("Enter Your First Name: \n")
    last_name = input("Enter Your Last Name: \n")
    user_name = input("Enter Your User Name: \n")
    age = int(input("Enter Your Age: \n"))
    sex = input("Enter Your Sex: \n")
    password = input("Enter Your Password: \n")
    account_create(first_name, last_name, user_name, age, sex, password)
