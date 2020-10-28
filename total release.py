

# Restaurant_Project
    #Veg_Nonveg 

print("\t","*** Hello !!! *** " , "\n", "\" Welcome to Darshan Family Restaurant \" ")
bill=0
while True:
    print( "\n","****** Menu-Card ****** ", "\n" ,"Sr.No." ,"\t" ,"Course", "\t" )  
    print("\n", "1", "\t", "Veg Course")
    print("\n", "2", "\t", "Non-Veg Course")
    print( "\n", "v => Veg", "\n", "n => Non_veg", "\n")
    ch= input("Select your Choice: ")
    qty=0
 
    
    if(ch=='v' or ch=='V' ):
        while True:
            print("\n","(*(*(*(*(*(*(*(*(* MAIN MENU *)*)*)*)*)*)*)*)*)")
            print("\n", "Sr. no.", "\t", "Items", "\n", "1","\t", "Starter", "\n", "2","\t", "Main Course", "\n", "3", "\t", "Dessert", "\n", "4", "\t", "Breads")
            print("\n","Select", "\n", "s => Starters", "\n", "m => Main Course", "\n", "d => Dessert", "\n", "b => Breads","\n", "e => Exit to Home Page Menu", "\n")
            start=input("Select Category from the List above: ")
            
    ##
            if(start=='d' or start=="D"):
                print("\n", "**** DESSERT MENU ***")
                print("\n", "Sr. no.", "\t", "Items", "\t", "Price")
                print("\n", "1","\t", "Ice Creams", "\t", "125")
                print("\n", "2","\t", "Malai Kulfi", "\t", "150")
                print("\n", "3","\t", "Cassata", "\t","\t", "200")
                print("\n", "4","\t", "Sizzling Brownie", "\t", "175")
                print("\n", "5","\t", "Tea/Coffee", "\t","50")
                print("\n", "6","\t", "Ice Tea", "\t","\t", "110")
                print("\n", "7","\t","Mocktails", "\t", "150")

                while True:
                    print("\n","Select the Sr no. of Dish you wish to Order: ")
                    dish= int(input("Enter your Choice:" ))

                    if (dish==1):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 125
                        
                    elif(dish==2):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 150
                        
                    elif(dish==3):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 200
                        
                    elif(dish==4):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 175
                        
                    elif(dish==5):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 50
                        
                    elif(dish==6):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 110
                        
                    elif(dish==7):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 150

                    elif(dish==0):
                        break

                    else:
                        print("Invaid Choice,...Try again!! ")

                    print("\n","\r","\r", "More Dishes you wish to Add ?? Select the Choice: ", "\n", "or SELECT [ 0 ] for  *_BACK__MENU_*")
                    
                continue  

    ##
            if start in ('B','b'):
                print("\n", "**** BREADS MENU ***")
                print("\n", "Sr. no.", "\t", "Items", "\t", "Price")
                print("\n", "1","\t", "Bhakri", "\t", "\t","20")
                print("\n", "2","\t", "Tandoori Roti", "\t", "25")
                print("\n", "3","\t", "Butter Roti", "\t", "30")
                print("\n", "4","\t", "Naan", "\t","\t", "35")
                print("\n", "5","\t", "Kulcha", "\t","\t","40")
                print("\n", "6","\t", "Butter Kulcha", "\t", "45")

                while True:
                    print("\n","Select the Sr no. of Dish you wish to Order: ")
                    dish= int(input("Enter your Choice:" ))

                    if (dish==1):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 20
                        
                    elif(dish==2):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 25
                        
                    elif(dish==3):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 30
                        
                    elif(dish==4):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 35
                        
                    elif(dish==5):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 40
                        
                    elif(dish==6):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 45

                    elif(dish==0):
                        break

                    else:
                        print("Invaid Choice,...Try again!! ")

                    print("\n","\r","\r", "More Dishes you wish to Add ?? Select the Choice: ", "\n", "or SELECT [ 0 ] for  *_BACK__MENU_*")
                continue
            
    ##
            if(start=='m' or start=="M"):
                print("\n", "**** MAIN COURSE MENU ***")
                print("\n", "Sr. no.", "\t", "Items", "\t", "Price")
                print("\n", "1","\t", "Veg Kolhapuri", "\t", "200")
                print("\n", "2","\t", "Veg Handi", "\t", "200")
                print("\n", "3","\t", "Veg Kurma", "\t", "200")
                print("\n", "4","\t", "Palak Paneer", "\t", "250")
                print("\n", "5","\t", "Paneer Kadai", "\t","260")
                print("\n", "6","\t", "Paneer Makhani", "\t", "300")
                print("\n", "7","\t", "Mushroom Masala", "\t", "300")
                print("\n", "8","\t", "Kaju Curry", "\t", "310")
                print("\n", "9","\t", "Dal Fry", "\t", "\t", "130")
                print("\n", "10","\t", "Dal Takda", "\t", "180")
                print("\n", "11","\t", "Channa Masala", "\t", "170")
                print("\n", "12","\t", "Malai Kofta", "\t", "220")

                while True:
                    print("\n","Select the Sr no. of Dish you wish to Order: ")
                    dish= int(input("Enter your Choice:" ))

                    if (dish==1):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*200
                    
                    elif(dish==2):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*200
                        
                    elif(dish==3):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*200
                        
                    elif(dish==4):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*250
                        
                    elif(dish==5):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*260
                        
                    elif(dish==6):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*300
                        
                    elif(dish==7):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*300
                        
                    elif(dish==8):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 310

                    elif(dish==9):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 130

                    elif(dish==10):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 180

                    elif(dish==11):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 170

                    elif(dish==12):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 220
                        
                    elif(dish==0):
                        break

                    else:
                        print("Invaid Choice,...Try again!! ")

                    print("\n","\r","\r", "More Dishes you wish to Add ?? Select the Choice: ", "\n", "or SELECT [ 0 ] for  *_BACK__MENU_*")
                continue
    ##
            if(start=='s' or start=='S'):
                print("\n", "**** STARTER MENU ***")
                print("\n", "Sr. no.", "\t", "Items", "\t", "Price")
                print("\n", "1","\t", "Veg Lollipop", "\t", "120")
                print("\n", "2","\t", "Veg Crispy", "\t", "135")
                print("\n", "3","\t", "Veg Chilli", "\t", "121")
                print("\n", "4","\t", "Gobi Manchurian", "\t", "117")
                print("\n", "5","\t", "Paneer Chilli", "\t","160")
                print("\n", "6","\t", "Paneer Crispy", "\t", "180")
                print("\n", "7","\t", "Paneer Tikka", "\t", "200")
                print("\n", "8","\t", "Veg Cutlet", "\t", "210")

                while True:
                    print("\n","Select the Sr no. of Dish you wish to Order: ")
                    dish= int(input("Enter your Choice:" ))

                    if (dish==1):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*120
                        
                    elif(dish==2):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*135
                        
                    elif(dish==3):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*121
                        
                    elif(dish==4):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*117
                        
                    elif(dish==5):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*160
                        
                    elif(dish==6):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*180
                        
                    elif(dish==7):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*200
                        
                    elif(dish==8):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 210
                        
                    elif(dish==0):
                        break
                    
                    else:
                        print("Invaid Choice,...Try again!! ")

                    print("\n","\r","\r", "More Dishes you wish to Add ?? Select the Choice: ", "\n", "or Select 0 for  *_Back__Menu_*")
                    
                continue
            print("Your Total bill = ", bill)
            ## from main menu to home page
            if(start=='e'):
                break
    ##continue

# ***************************
    if(ch=='n' or ch=='N' ):
        while True:
            print("\n","(*(*(*(*(*(*(*(*(* MAIN MENU *)*)*)*)*)*)*)*)*)")
            print("\n", "Sr. no.", "\t", "Items", "\n", "1","\t", "Starter", "\n", "2","\t", "Main Course", "\n", "3", "\t", "Dessert", "\n", "4", "\t", "Breads")
            print("\n","Select", "\n", "s => Starters", "\n", "m => Main Course", "\n", "d => Dessert", "\n", "b => Breads","\n", "e => Exit to Home Page Menu", "\n")
            start=input("Select Category from the List above: ")
            
    ##
            if start in ('d','D'):
                print("\n", "**** DESSERT MENU ***")
                print("\n", "Sr. no.", "\t", "Items", "\t", "Price")
                print("\n", "1","\t", "Ice Creams", "\t", "125")
                print("\n", "2","\t", "Malai Kulfi", "\t", "150")
                print("\n", "3","\t", "Cassata", "\t","\t", "200")
                print("\n", "4","\t", "Sizzling Brownie", "\t", "175")
                print("\n", "5","\t", "Tea/Coffee", "\t","50")
                print("\n", "6","\t", "Ice Tea", "\t","\t", "110")
                print("\n", "7","\t","Mocktails", "\t", "150")

                while True:
                    print("\n","Select the Sr no. of Dish you wish to Order: ")
                    dish= int(input("Enter your Choice:" ))

                    if (dish==1):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 125
                        
                    elif(dish==2):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 150
                        
                    elif(dish==3):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 200
                        
                    elif(dish==4):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 175
                        
                    elif(dish==5):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 50
                        
                    elif(dish==6):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 110
                        
                    elif(dish==7):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 150

                    elif(dish==0):
                        break

                    else:
                        print("Invaid Choice,...Try again!! ")

                    print("\n","\r","\r", "More Dishes you wish to Add ?? Select the Choice: ", "\n", "or SELECT [ 0 ] for  *_BACK__MENU_*")
                    
                continue  

    ##
            if start in ('B','b'):
                print("\n", "**** BREADS MENU ***")
                print("\n", "Sr. no.", "\t", "Items", "\t", "Price")
                print("\n", "1","\t", "Bhakri", "\t", "\t","20")
                print("\n", "2","\t", "Tandoori Roti", "\t", "25")
                print("\n", "3","\t", "Butter Roti", "\t", "30")
                print("\n", "4","\t", "Naan", "\t","\t", "35")
                print("\n", "5","\t", "Kulcha", "\t","\t","40")
                print("\n", "6","\t", "Butter Kulcha", "\t", "45")

                while True:
                    print("\n","Select the Sr no. of Dish you wish to Order: ")
                    dish= int(input("Enter your Choice:" ))

                    if (dish==1):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 20
                        
                    elif(dish==2):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 25
                        
                    elif(dish==3):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 30
                        
                    elif(dish==4):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 35
                        
                    elif(dish==5):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 40
                        
                    elif(dish==6):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty* 45

                    elif(dish==0):
                        break

                    else:
                        print("Invaid Choice,...Try again!! ")

                    print("\n","\r","\r", "More Dishes you wish to Add ?? Select the Choice: ", "\n", "or SELECT [ 0 ] for  *_BACK__MENU_*")
                continue
            
    ##
            if(start=='m' or start=="M"):
                print("\n", "**** MAIN COURSE MENU ***")
                print("\n", "Sr. no.", "\t", "Items", "\t", "Price")
                print("\n", "1","\t", "Egg Curry", "\t", "180")
                print("\n", "2","\t", "Butter Chicken", "\t", "250")
                print("\n", "3","\t", "Chicken Masala", "\t", "200")
                print("\n", "4","\t", "Chicken Handi", "\t", "250")
                print("\n", "5","\t", "Mutton Curry", "\t","280")
                print("\n", "6","\t", "Mutton Handi", "\t", "300")
                print("\n", "7","\t", "Fish Masala", "\t", "330")
                print("\n", "8","\t", "Fish Curry", "\t", "330")
                print("\n", "9","\t", "Prawns Masala","\t", "350")
                print("\n", "10","\t", "Chicken Tikka", "\t", "280")
                print("\n", "11","\t", "Mutton Kheema", "\t", "370")
                print("\n", "12","\t", "chicken Mughlai", "\t", "250")

                while True:
                    print("\n","Select the Sr no. of Dish you wish to Order: ")
                    dish= int(input("Enter your Choice:" ))

                    if (dish==1):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*180
                    
                    elif(dish==2):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*250
                        
                    elif(dish==3):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*200
                        
                    elif(dish==4):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*250
                        
                    elif(dish==5):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*280
                        
                    elif(dish==6):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*300
                        
                    elif(dish==7):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*330
                        
                    elif(dish==8):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 330

                    elif(dish==9):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 350

                    elif(dish==10):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 280

                    elif(dish==11):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 370

                    elif(dish==12):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 250
                        
                    elif(dish==0):
                        break

                    else:
                        print("Invaid Choice,...Try again!! ")

                    print("\n","\r","\r", "More Dishes you wish to Add ?? Select the Choice: ", "\n", "or SELECT [ 0 ] for  *_BACK__MENU_*")
                continue
    ##
            if(start=='s' or start=='S'):
                print("\n", "**** STARTER MENU ***")
                print("\n", "Sr. no.", "\t", "Items", "\t", "Price")
                print("\n", "1","\t", "Chicken Lollipop", "\t", "220")
                print("\n", "2","\t", "Murgh Kabab", "\t", "235")
                print("\n", "3","\t", "Murgh Tikka", "\t", "250")
                print("\n", "4","\t", "Murgh Afghani", "\t", "280")
                print("\n", "5","\t", "Tandoori Murgh", "\t","200")
                print("\n", "6","\t", "Prawns BBQ", "\t", "300")
                print("\n", "7","\t", "Fish Tikka", "\t", "350")
                print("\n", "8","\t", "Chicken 65", "\t", "350")

                while True:
                    print("\n","Select the Sr no. of Dish you wish to Order: ")
                    dish= int(input("Enter your Choice:" ))

                    if (dish==1):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*220
                        
                    elif(dish==2):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*235
                        
                    elif(dish==3):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*250
                        
                    elif(dish==4):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*280
                        
                    elif(dish==5):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*200
                        
                    elif(dish==6):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*300
                        
                    elif(dish==7):
                        qty=int(input("Enter the quantity: "))
                        bill+=qty*350
                        
                    elif(dish==8):
                        qty=int(input("Enter the quantity: "))
                        bill+= qty* 350
                        
                    elif(dish==0):
                        break
                    
                    else:
                        print("Invaid Choice,...Try again!! ")

                    print("\n","\r","\r", "More Dishes you wish to Add ?? Select the Choice: ", "\n", "or Select 0 for  *_Back__Menu_*")
                continue
            print("Your Total bill = ", bill)
            ## from main menu to home page
            if(start=='e'):
               break
    continue
print("Your Total bill = ", bill)
    





