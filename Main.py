import random       
import csv     
import time
from datetime import datetime


records = open("records.csv", "a+", newline="")      

records.seek(0)         

if records.read(1) == "":      
    csv.writer(records).writerow(["Account Number", "Name", "Contact Number", "Address", "Amount"])        
                         
record = csv.writer(records)  
amount=0    
dictacc=[]                

global accno
global contf         
global addrf
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
def selectoptn():
    global dictacc
    global amount
    global namef

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
    if useroption== "a":   
        print("==="*40)
        namef=input("Please enter your Full Name: ")
        contf=int(input("Please enter your 10-digit contact Number: "))
        if len(str(contf)) == 10:
            addrf=input("Please enter your Address: ")
            accno = random.randint(11111111111,99999999999)
            dictacc = [accno,namef,contf,addrf,amount]      
            accs=str(accno)
            record.writerow(dictacc)
            records.flush()

            print("==="*40)
            print("\nYOUR NEW ACCOUNT HAS BEEN CREATED SUCCESSFULLY!")
            print("\n--YOUR ACCOUNT DETAILS--")
            print("==="*40)
            print("Account Number: ",accs)
            print("\nPLEASE SAVE YOUR ACCOUNT NUMBER, AS IT MAY BE VISIBLE TO YOU ONLY ONCE... CONTACT ADMIN FOR SUPPORT!")
            time.sleep(7) 
        else:
            print("INVALID CONTACT NUMBER... PLEASE TRY AGAIN")
            

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#        

    elif useroption == "b":
        print("==="*40)
        records.seek(0)
        accono = input("enter your account number to deposit: ")
        search = list(csv.reader(records))
        for i in range(len(search)):
            if search[i][0] == accono:
                print("Account found")
                namef = search[i][1]
                amount = int(search[i][4])
                enteredval = int(input("Enter the amount you want to deposit (in INR): "))
                print("This will change the balance in your account to INR", amount + enteredval, ",proceed? (y/n)")
                x = input("your choice: ")
                if x == "y":
                    search[i][4] = str(amount + enteredval)
                    print("==="*40)
                    print("UPDATED SUCCESSFULLY! Your New balance is INR", search[i][4])
                    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    email_receipt = f"""
                    =================================================
                        MINI BANK – TRANSACTION RECEIPT
                    =================================================
                    To: {namef.replace(" ", "").lower()}@minibank.com
                    Date & Time: {timestamp}

                    Account Number: {accono}
                    Account Holder: {namef}
                    Transaction Type: {"Deposit"}
                    Transaction Amount: INR {enteredval}
                    New Balance: INR {search[i][4]}

                    Thank you for banking with us!
                    - MiniBank System
                    =================================================
                    """

                    print(email_receipt)
                elif x != "n":
                    print("\nPlease answer as y/n")
                break
            
        else:
            print("\nError - ACCOUNT NOT FOUND")
        
            

        records.seek(0)
        records.truncate(0)
        writer = csv.writer(records)
        writer.writerows(search)
        records.flush()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#        

    elif useroption == "c":
        print("===" * 40)
        records.seek(0)
        accono = input("Enter your account number to withdraw from: ")
        search = list(csv.reader(records))

        for i in range(len(search)):
            if search[i][0] == accono:
                print("Account found")
                namef = search[i][1] 
                amount = int(search[i][4])
                enteredval = int(input("Enter the amount you want to withdraw (in INR): "))

                if enteredval > amount:
                    print("Insufficient balance!")
                else:
                    print("This will change the balance in your account to INR", amount - enteredval, ", proceed? (y/n)")
                    x = input("your choice: ")
                    if x == "y":
                        search[i][4] = str(amount - enteredval)
                        print("===" * 40)
                        print("UPDATED SUCCESSFULLY! Your New balance is INR", search[i][4])

                        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        email_receipt = f"""
                        =================================================
                            MINI BANK – TRANSACTION RECEIPT
                        =================================================
                        To: {namef.replace(" ", "").lower()}@minibank.com
                        Date & Time: {timestamp}

                        Account Number: {accono}
                        Account Holder: {namef}
                        Transaction Type: Withdrawal
                        Transaction Amount: INR {enteredval}
                        New Balance: INR {search[i][4]}

                        Thank you for banking with us!
                        - MiniBank System
                        =================================================
                        """
                        print(email_receipt)

                    elif x != "n":
                        print("\nPlease answer as y/n")
                break
        else:
            print("\nError - ACCOUNT NOT FOUND")

        records.seek(0)
        records.truncate(0)
        writer = csv.writer(records)
        writer.writerows(search)
        records.flush()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif useroption == "d":
        print("==="*40)
        records.seek(0)
        accono = input("enter your account number to view: ")
        search = list(csv.reader(records))

        for i in range(len(search)):
            if len(search[i]) >= 5 and search[i][0] == accono:
                print("===" * 40)
                print("Account Number:", search[i][0])
                print("Name:", search[i][1])
                print("Contact Number:", search[i][2])
                print("Address:", search[i][3])
                print("Amount: INR", search[i][4])

                print("===" * 40)
                print("These are your account Details... Please select an option to proceed: ")
                print("(1) Update information")
                print("(2) Delete your account *(This is permanent)*")
                print("(3) Return to Main Menu")
                print("Please answer as 1, 2, or 3")
                pro = input("Your choice: ")

                if pro == "1":
                    print("Please select the information you want to update under", accono)
                    print("a - Name")
                    print("b - Contact Number")
                    print("c - Address")
                    uptodate = input("Your choice: ")

                    if uptodate == "a":
                        print("The current name in your account is:", search[i][1])
                        newval = input("Enter your new name: ")
                        print("This will change your name to:", newval, ", proceed? (y/n)")
                        x = input("Your choice: ")
                        if x == "y":
                            search[i][1] = newval
                            print("UPDATED SUCCESSFULLY!")
                        elif x != "n":
                            print("\nPlease answer as y/n")
                    elif uptodate == "b":
                        print("The current contact number in your account is:", search[i][2])
                        newval = input("Enter your new 10-digit contact number: ")
                        print("This will change your contact to:", newval, ", proceed? (y/n)")
                        x = input("Your choice: ")
                        if x == "y":
                            search[i][2] = newval
                            print("UPDATED SUCCESSFULLY!")
                        elif x != "n":
                            print("\nPlease answer as y/n")
                    elif uptodate == "c":
                        print("The current address in your account is:", search[i][3])
                        newval = input("Enter your new address: ")
                        print("This will change your address to:", newval, ", proceed? (y/n)")
                        x = input("Your choice: ")
                        if x == "y":
                            search[i][3] = newval
                            print("UPDATED SUCCESSFULLY!")
                        elif x != "n":
                            print("\nPlease answer as y/n")
                    else:
                        print("Invalid choice. Please enter a, b, or c.")

                elif pro == "2":
                    print("Are you sure you want to permanently delete this account? (y/n)")
                    x = input("Your choice: ")
                    if x == "y":
                        del search[i]
                        print("ACCOUNT DELETED SUCCESSFULLY!")
                    elif x!="n":
                        print("Please answer as y/n")

                elif pro == "3":
                    print("Returning to main menu.")
                else:
                    break

                break 

        else:
            print("ERROR - ACCOUNT NOT FOUND.")

        records.seek(0)
        records.truncate(0)
        writer = csv.writer(records)
        writer.writerows(search)
        records.flush()

        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
print("Welcome to MiniBack, We are here to Help!")
while True:
    print("==="*40)
    print("What operation do you want to perform - (answer by a, b, c, d or e)")
    print("a - OPEN ACCOUNT")
    print("b - DEPOSIT AMOUNT")
    print("c - WITHDRAW AMOUNT")
    print("d - VIEW / UPDATE ACCOUNT STATS")
    print("e - EXIT")
    print("========================================")
    useroption = input("Enter your choice: ").lower()
    selectoptn()
    time.sleep(2)

    if useroption == "e":
        print("Thank you for using MiniBank! See you soon!")
        break

records.close()
