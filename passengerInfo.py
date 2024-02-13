import csv

class PassengerRegistration():
    def __init__(self) :
        self.passengerName = None
        self.noOfPassenger = None
        self.departureLocation = None
        self.destinationLocation = None
        self.ddmyyyy = None
        self.seatNo = None
        self.selectBusType = None
        self.busFare = None
        self.autoInc = 1
        self.countCol = 0

    def getPassengerInfo(self):
        self.passengerName = input("Enter Passenger Name             : ")
        self.noOfPassenger = int(input("Enter the Number of Passenger: "))
        print()
        print("1: Nagpur")
        print("2: Pune")
        print("3: Delhi")
        print("4: Mumbai")
        print("5: Lucknow")
        print("6: Hyderabad")

        self.dl = int(input("Enter Departure Location: "))
        if self.dl==1:
            self.departureLocation="Nagpur"
        elif self.dl==2:
            self.departureLocation="Pune"
        elif self.dl==3:
            self.departureLocation="Delhi"
        elif self.dl==4:
            self.departureLocation="Mumbai"
        elif self.dl==5:
            self.departureLocation="Lucknow"
        elif self.dl==6:
            self.departureLocation="Hydrabad"
        else:
            print("Print Enter correct choice: ")

        print()
        print("1: Patna")
        print("2: Phagwara")
        print("3: Jaipur")
        print("4: Shimla")
        print("5: Manali")
        print("6: Kolkata")
        self.dpl=int(input("Enter the Destination Location:"))
        if(self.dpl==1):
            self.destinationLocation = "Patna"
        elif(self.dpl==2):
            self.destinationLocation= "Phagwara"
        elif(self.dpl==3):
            self.destinationLocation= "Jaipur"
        elif(self.dpl==4):
            self.destinationLocation= "Shimla"
        elif(self.dpl==5):
            self.destinationLocation= "Manali"
        elif(self.dpl==6):
            self.destinationLocation= "Kolkata"

        print()
        self.ddmmyyyy = input("Enter Date of Journey Like(07-05-2002):")
        print()
        print("[1]_[2]_[3]_[4]_[5]")
        print("[6]_[7]_[8]_[9]_[10]")
        print("[11]_[12]_[13]_[14]_[15]")
        print("[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]")
        print("[26]_[27]_[28]_[29]_[30]")
        seatNoList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.bookingList = []

        while True:
            self.seatNo = int(input("Enter the seat Number and you can only book maximum 2 tickets:"))
            if self.seatNo<=30:
                if self.seatNo in seatNoList:
                    self.bookingList.append(self.seatNo)
                    del seatNoList[self.seatNo+1]
                    count = len(seatNoList)
                else:
                    print("Ticket Already Booked:")
                print("Do you want one more Seat enter(Yes/No):")
                y=input("")
                if y=="Yes":
                    pass
                else:
                    break
            else:
                print("Dont choose seat number which is not available:")

        print()
        print("1 : AC Bus fare    :500")
        print("2 : Non-AC Bus fare:300")
        self.busType = int(input("Select Bus Type:"))

        if self.busType == 1:
            self.selectBusType = "AC BUS"
            self.busFare = self.noOfPassenger*500
        elif self.busType == 2:
            self.selectBusType = "Non-AC BUS"
            self.busFare = self.noOfPassenger*300


class PassangerDataCsv(PassengerRegistration):
        def saveInfo(self):
            try:
                with open("passengerData.csv","r+",newline="") as f:
                    r = csv.reader(f)
                    data = list(r)
                    #print data
                    for i in data:
                        self.autoInc+=1
                        for j in i:
                            self.countCol+=1
                        print()
                    print("Number of records are found in database:",self.autoInc)
            except:
                print("File has not available")
            finally:
                with open("passengerData.csv",'a+',newline="") as f:
                    w = csv.writer(f)
                    w.writerow([self.autoInc,self.passengerName,self.noOfPassenger,self.departureLocation,self.destinationLocation,self.ddmmyyyy,self.seatNo,self.busType,self.busFare])

                    print("Data Save Successfully")
                    print()   



          