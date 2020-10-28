#write a program to Restaurant project
bill=0
qty=0
flst=[]
blst=[]



print("*************Welcome to the DARSHAN Family Restaurant**********")

print("-----------------***Here''s' our Menu***------------")
while True:
    choice=input("""
               A. Veg Menu
               B. Non-Veg Menu
               C. Dessert Menu
               Z. Exit Menu
               What would you like to have sir/madam? => """)
    if choice=='a' or choice=='A':
        print("Veg")
        
        while True:
            
            print(" *********Starter********")
            
            starter=input("""
                    D.Aloo Chart \t 150
                    E.Soup menu      
                    F.Green salad \t 120
                    G.Masala papd \t 90
                    H.Paneer Tika \t 150
                    i.Sweet Potato\t 200
                    j.Exit for Main course
                    what would you have? =>""")
            
            if starter=='D' or starter=='d':
                print("Aloo chart")
                qty=int(input("How many qty you have?=>"))
                flst.append("Aloo chart")
                flst.append(150)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*150
                
                
            elif starter=='e' or starter=='E':
                
                print("************ Soup Menu ************")
                
                while True:
                    soup=input("""
                    1.Tomato soup \t 120
                    2.Mix Veg soup \t 100
                    3.Cremy of veg soup\t 100
                    4.Exit to starter menu 
                    choice your option? =>""")
                    
                    if soup=='1':
                        print("Tomato soup")
                        qty=int(input("How many qty you have?=>"))
                        flst.append("Tomato soup")
                        flst.append(120)
                        flst.append(qty)
                        blst.append(flst)
                        bill+=qty*120
                        
                
                    elif soup=='2':
                        print("Mix veg soup")
                        qty=int(input("How many qty you have?=>"))
                        flst.append("Mix Veg soup")
                        flst.append(100)
                        flst.append(qty)
                        blst.append(flst)
                        bill+=qty*100
                        
                
                    elif soup=='3':
                        print("Cremy of veg soup")
                        qty=int(input("How many qty you have?=>"))
                        flst.append("Cremy of veg soup")
                        flst.append(100)
                        flst.append(qty)
                        blst.append(flst)
                        bill+=qty*100
                        
                    elif soup=='4':
                        break
                        
                    
                    print("Do you want to continue ...or add dishes...??? select the choice","\n"," or select[0] for back to ***_Back to Menu_**")
                        
                    
                continue
                    
            if starter=='f' or starter=='F':
                    print("Green salad")
                    qty=int(input("How many qty you have?=>"))
                    flst.append("Green salad")
                    flst.append(120)
                    flst.append(qty)
                    blst.append(flst)
                    bill+=qty*120
                    
            if starter=='g' or starter=='G':
                    print("Masala Papd")
                    qty=int(input("How many qty you have?=>"))
                    flst.append("Masala Papd")
                    flst.append(90)
                    flst.append(qty)
                    blst.append(flst)
                    bill+=qty*90
                    
            if starter=='h' or starter=='H':
                    print("Paneer Tikka")
                    qty=int(input("How many qty you have?=>"))
                    flst.append("Paneer Tikka")
                    flst.append(150)
                    flst.append(qty)
                    blst.append(flst)
                    bill+=qty*150
                    
            if starter=='i' or starter=='I':
                    print("Sweet potato")
                    qty=int(input("How many qty you have?=>"))
                    flst.append("Sweet potato")
                    flst.append(200)
                    flst.append(qty)
                    blst.append(flst)
                    bill+=qty*200
                    
            if starter=='j' or starter=='J':
                break

                print("Exit for main course")
                 
            continue
        
        
        while True:

            print("!!!@!@!!@!@!@ Main Course !!@!@!@!@!@!@!@")
            
            Mcourse=input("""
                        5.Handi \t\t 200
                        6.mix veg \t\t 150
                        7.paeer veg \t\t 250
                        8.makhmali \t\t 200
                        9.Rumal roti \t\t 30
                        10.Nan  \t\t 40
                        11.Kulcha \t\t 50
                        12.Exit for Non-veg menu
                        choice your like => """)
            
            if Mcourse=='5':
                print("Handi")
                qty=int(input("How many qty you have?=>"))
                flst.append("Handi")
                flst.append(200)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*200

            elif Mcourse=='6':
                print("Mix Veg")
                qty=int(input("How many qty you have?=>"))
                flst.append("Mix Veg")
                flst.append(150)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*150

            elif Mcourse=='7':
                print("Paneer Veg")
                qty=int(input("How many qty you have?=>"))
                flst.append("Paneer Veg")
                flst.append(250)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*250

            elif Mcourse=='8':
                print("makhmali")
                qty=int(input("How many qty you have?=>"))
                bill+=qty*200

            elif Mcourse=='9':
                print("Rumali Roti")
                qty=int(input("How many qty you have?=>"))
                flst.append("Rumali Roti")
                flst.append(30)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*30

            elif Mcourse=='10':
                print("Nan")
                qty=int(input("How many qty you have?=>"))
                flst.append("Nan")
                flst.append(40)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*40

            elif Mcourse=='11':
                print("Kulcha")
                qty=int(input("How many qty you have?=>"))
                flst.append("Kulcha")
                flst.append(50)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*50

            elif Mcourse=='12':
                break

                print("Exit for Non- veg menu......")

            continue
        
                
    if choice=='b' or choice=='B':
        print("Non-Veg")

        while True:

            print(" @@@@@@@@@@ Non-Vge Starter @@@@@@@@@@@")

            starter=input("""
                        K.Aloo with chiken \t 100
                        L.Non-Vge Soup      
                        M.Fish salad \t\t 150
                        N.Kabba \t\t 80
                        O.Chili Chiken \t\t 120
                        P.Bhurji \t\t 75
                        Q.Exit for Main course
                        what would you have? =>""")

            if starter=='k' or starter=='K':
                print("Aloo with chiken")
                qty=int(input("How many qty you have?=>"))
                flst.append("Aloo With Chiken")
                flst.append(100)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*100
                    
                    
            elif starter=='l' or starter=='L':

                print("************ Non-Veg Soup ************")

                while True:
                        soup=input("""
                        13.Chiken Soup \t\t 105
                        14.Chiken Mix soup \t\t 95
                        15.Chiken manchow soup \t\t 100
                        16.Exit for Back to starter menu 
                        choice your option? =>""")

                        if soup=='13':
                            print("Chiken Soup")
                            qty=int(input("How many qty you have?=>"))
                            flst.append("Chiken Soup")
                            flst.append(105)
                            flst.append(qty)
                            blst.append(flst)
                            bill+=qty*105
                            
                    
                        elif soup=='14':
                            print("Chiken Mix soup")
                            qty=int(input("How many qty you have?=>"))
                            flst.append("Chiken Mix Soup")
                            flst.append(95)
                            flst.append(qty)
                            blst.append(flst)
                            bill+=qty*95
                            
                    
                        elif soup=='15':
                            print("Chiken manchow soup")
                            qty=int(input("How many qty you have?=>"))
                            flst.append("Chiken Manchow soup")
                            flst.append(100)
                            flst.append(qty)
                            blst.append(flst)
                            bill+=qty*100
                            
                        elif soup=='16':
                            break

                        print("Do you want to continue ...or add dishes...??? select the choice","\n","or select[0] for back to ***_Stater Menu_**")
                            
                continue
                        
            if starter=='M' or starter=='m':
                    print("Fish salad")
                    qty=int(input("How many qty you have?=> "))
                    flst.append("Tomato soup")
                    flst.append(120)
                    flst.append(qty)
                    blst.append(flst)
                    bill+=qty*150
                        
            if starter=='n' or starter=='N':
                    print("Kabab")
                    qty=int(input("How many qty you have?=> "))
                    flst.append("Kabab")
                    flst.append(80)
                    flst.append(qty)
                    blst.append(flst)
                    bill+=qty*80
                        
            if starter=='o' or starter=='O':
                    print("Chili Chiken")
                    qty=int(input("How many qty you have?=> "))
                    flst.append("Cgili Chiken")
                    flst.append(120)
                    flst.append(qty)
                    blst.append(flst)
                    bill+=qty*120
                        
            if starter=='p' or starter=='P':
                    print("Bhurji")
                    qty=int(input("How many qty you have?=> "))
                    flst.append("Bhurji")
                    flst.append(75)
                    flst.append(qty)
                    blst.append(flst)
                    bill+=qty*75
                        
            if starter=='Q' or starter=='q':
                break

                print("Exit for Non-Vge main course")
                     
            continue
            
        while True:
                
            print("!!!@!@!!@!@!@ Non-Veg Main Course !!@!@!@!@!@!@!")
                
            Mcourse=input("""
                            17.Chiken jalfrezi \t\t 300
                            18.Chiken fried rice \t 350
                            19.Fish kaddi \t\t 200
                            20.Chiken oyster \t\t 250
                            21.Rumal roti \t\t 30
                            22.Nan  \t\t 40
                            23.Fish Rice \t\t 185
                            24.Exit in Non-veg menu
                            choice your like => """)
                
            if Mcourse=='17':
                print("Chiken jalfrezi")
                qty=int(input("How many qty you have?=>"))
                flst.append("Chiken Jalfrezi")
                flst.append(300)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*300

            elif Mcourse=='18':
                print("Chiken fried rice")
                qty=int(input("How many qty you have?=>"))
                flst.append("Chiken Fried Rice")
                flst.append(350)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*350

            elif Mcourse=='19':
                print("Fish kaddi")
                qty=int(input("How many qty you have?=>"))
                flst.append("Fish Kaddi")
                flst.append(200)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*200

            elif Mcourse=='20':
                print("Chiken oyster")
                qty=int(input("How many qty you have?=>"))
                flst.append("Chiken Oyster")
                flst.append(250)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*250

            elif Mcourse=='21':
                print("Rumali roti")
                qty=int(input("How many qty you have?=>"))
                flst.append("Rumali Roti")
                flst.append(30)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*30

            elif Mcourse=='22':
                print("Nan")
                qty=int(input("How many qty you have?=>"))
                bill+=qty*40

            elif Mcourse=='23':
                print("Fish Rice")
                qty=int(input("How many qty you have?=>"))
                flst.append("Fish Rice")
                flst.append(185)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*185

            elif Mcourse=='24':
                break

                print("Exit in Non- veg menu......")

            continue
            
    if choice=='c' or choice=='C':
        print("Dessert")

        while True:
            
            print("@@@@@@@@@@@@@@@@ Dessert @@@@@@@@@@@@@@@@@@")

            Dess=input("""
                        R.Ice-Crem \t 20
                        S.Brownie \t 55
                        T.Choco Hazelnut 120
                        U.Rabdi \t 56
                        V.Exit in Dessert
                        Please Select Your choice => """)

            if Dess=='R' or Dess=='r':
                print("Ice-Crem")
                qty=int(input("How many qty you have?=>"))
                flst.append("Ice-Crem")
                flst.append(120)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*20

            elif Dess=='S' or Dess=='s':
                print("Brownie")
                qty=int(input("How many qty you have?=>"))
                flst.append("Brownie")
                flst.append(55)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*55

            elif Dess=='T' or Dess=='t':
                print("Choco Hazelnut")
                qty=int(input("How many qty you have?=>"))
                flst.append("Choco Hazelnut")
                flst.append(120)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*120

            elif Dess=='U' or Dess=='u':
                print("Rabdi")
                qty=int(input("How many qty you have?=>"))
                flst.append("Rabdi")
                flst.append(56)
                flst.append(qty)
                blst.append(flst)
                bill+=qty*56

            elif Dess=='V' or Dess=='v':
                break

            else:
                print("Exit in Dessert")

        print("Do you want to continue ...or add dishes...??? select the choice","\n"," or select[0] for back to ***_Back to Menu_**")    

        continue

    if choice=='Z' or choice=='z':
        print("We have Done please take the Bill")

        while True:

            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Bill of List !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
            for c in blst:
                for j in c:
                    print(j, " " , end = "" )
                    print("\n")    
                    break
            break
    
        gst_bill= (bill * 18) /100
        gst_invoice= bill+ gst_bill
        print("Total Bill => " ,bill)
        break
    
                     
                     
                     
                    
    
    
    
