from passengerInfo import*
from ticketShow import*
from admin import*

global ch

print("--------------------------*********-----------------------------------")
print("--------------------------*********-----------------------------------")
print("              Welcome to Gajraj Traveller's   ")
print("--------------------------*********-----------------------------------")
print("--------------------------*********-----------------------------------")
print()

def start():
    print("1:Admin Registration   :")
    print("2:Admin Login          :")
    print()
    adminObj = Admin()
    ch = int(input("Choose correct option:"))
    if ch==1:
        adminObj.adminRegistration()
    if ch==2:
        adminObj.adminLogin()
        print()
        print("1: Passenger Registration")
        print("2 : Show Ticket")
        ch = int(input("Enter any one option:"))
        if ch==1:
            pd_obj=PassangerDataCsv()
            pd_obj.getPassengerInfo()
            pd_obj.saveInfo()
        elif ch==2:
            obj = TicketShow()
            obj.ticketShow()
start()