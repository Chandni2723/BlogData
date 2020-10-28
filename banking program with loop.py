#write a program to do banking in loop

balance=2000
eid=input("enter id => ")
pas =input("enter password=> ")
while True:
    if eid == 'admin@123' and pas== 'admin12' :
        print("balance is {}".format(balance))
        print("w for widrow amount")
        print("d for deposit amount")
        print("q for quit ")
        ch=input("enter yore choice=> ")
        if ch=='w' or ch== 'W':
            if balance<=1000 or 1000>=balance:
                print("limit plz deposite first ")
                   
            else:
                amt=float(input("enter amount=> " ))
                balance=balance-amt  
            
        elif ch=='d' or ch=='D':
            amt=float(input("enter amount => "))
            balance=balance+amt
            print("Now your balance is => ",balance)
        elif ch =='q' or ch=='Q':
            break
        else:
            print("do not such transaction choice .....try again")
                
    else:
        print("invaild ID password enter correct")
        break
        

print("Your Balance is ",balance)       
