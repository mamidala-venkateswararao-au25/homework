from d_registration import cabdriver
from rider import cabrider
from wlcome import welcome
from dstance import distance
from reachpoint import destination
# import phonenumbers
if __name__=="__main__":
    hackman=cabdriver()
    passenger=cabrider()
    DriverCount=int(input("enter no.of Driver: "))
    for k in range(DriverCount):
    #Driver:::
        NAMe=str(input("Please Add your Name: "))
        CAB_NUMBER=input("Please Enter your Cab_NUMBER: ")
        PH_NUMBER=int(input("Please Enter your PH_NUMBER: "))
        AVAILABLE=input("Press<YES> if you are available else <NO>: ")
        print("Enter your location Co_ordinates: ")
        a1= int(input("Enter of X Co_ordinates: "))
        a2= int(input("Enter of Y Co_ordinates: "))
        Driver=hackman.driver_info(NAMe,CAB_NUMBER,PH_NUMBER,AVAILABLE,a1,a2)
        print("Your Details", Driver)
    #Rider::
    print("Enter Rider Details")
    NAME=str(input("Type Your NAME: "))
    CITY=input("Enter Your Place: ")
    # PH_NO=phonenumbers.parse(str(input("Your Mobile Number: ")))
    PH_NO=int(input("enter your number: "))
    BOOKING=input()
    if BOOKING == "yes":
        b1=int(input("Type your x Co_ordinates: "))
        b2=int(input("Type your y Co_ordinates: "))
        Rider=passenger.rider_info(NAME,CITY,PH_NO,BOOKING,b1,b2)
        print("Your Details:", Rider)
    
    alldrivers=hackman.getDriverslist()
    allriders=passenger.historyofrides()
    print("cab types <low>, <medium>, <high> ")
    entry = input("Provide your Input here: ")
    if entry == "low" or entry == "medium" or entry == "high":
        print(" THANK you for Booking with us , Please enter your the location you want to go:")
        d1=int(input("enter x co_ordinates: "))
        d2=int(input("enter y co_ordinates: "))
        space=999999999999
        cab_registered=None
        for i in range(len(alldrivers)):
            d=distance(alldrivers[i]["a1"], alldrivers[i]["a2"],allriders[0]["b1"],allriders[0]["b2"])
            print("This driver ", alldrivers[i]["NAME"], "is", d, "KM from you")            
            if d<space:
                space=d
                cab_registered=alldrivers[i]
        print("The driver is close to your location point so", cab_registered, "will reach you shortly")


        for j in range(len(allriders)):
            l= destination(allriders[0]["b1"], allriders[0]["b2"], d1, d2)
            print("Arrived to your Destination point")

        if entry == "low":
            amount = 3
            print("Pay the Amount of Rs. ", l*amount*(d/10))
        elif entry == "medium":
            amount = 4
            print("Pay the Amount of Rs. ", l*amount*(d/10))
        elif entry == "high":
            amount=6
            print("Pay the Amount of Rs. ", l*amount*(d/10))




    while True:
        print("To see history of all your Rides type<check>: ")
        print("To quit type <EXIT>: ")
        entry = input("Provide Your Input here:::   ")
        if entry=="check":
            print(alldrivers,allriders)

        if entry == "EXIT":
            print("Thank You, visit Again!")
            break
