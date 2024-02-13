from passengerInfo import*
class TicketShow():
    def ticketShow(self):
        bln = []
        with open("passengerData.csv","r+",newline="") as f:
                r = csv.reader(f)
                data = list(r)
                id = int(input("Enter your Booking ID :"))
                for i in data:
                     if id==int(i[0]):
                        for j in i:
                            bln.append(j)
                        break
        print("----------------------------------------------------------------------")
        print("--------------------------*********-----------------------------------")
        print("                     Gajraj Bus Servise                               ")
        print("--------------------------*********----------------------------------")
        print("----------------------------------------------------------------------")
        print()
        print("e-Ticket ::","Address                :Hingna Road, Pyarepatti,Ludhiana")
        print("           ","Phone Number           :6307537795 , 87349765")
        print()
        print("",bln[3],"------------>",bln[4],"           ","      Number of Passenger:",bln[2])
        print("______________________________________________________________________")
        print()
        print(" Date of Booking:",bln[5],"            ","Seat Number :",bln[6],"       ")
        print("Bus Type :",bln[7],"                                                   ")
        print()
        print("--------------------------*********----------------------------------")
        print("----------------------------------------------------------------------")

