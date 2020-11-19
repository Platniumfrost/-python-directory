def logo_screen():
    logo= """|          |
                                    /-\\
                                   -   -
                                  /     \\
                                 -       -
                                /         \\
                               -           -
                              /      |      \\
                             -    |  |  |    -
                            /   |    |     |  \\
                           -  |      |      |  -
                          /  |       |       |  \\
                         -    |      |      |    -
                        /       |    |    |       \\
                       -          |  |  |          -
                      /              |              \\
                     -                               -
                    /                                 \\
                   -                                   -
                  /                                     \\
          |      |---------------------------------------|     |"""
    creators= "EMILY BRIGGS, ELAINA KELL, HALEY BICE"
    title= "OREGON TRAIL"
    trademark= "TM 2020"
    print(logo)
    print(creators)
    print(title)
    print(trademark)



def menu_function(options):
    index= 1
    for i in options:
        print(str.format("{}-----  {}  ", index, i))
        index +=1
    while True:
        choice = input("pick a number between 1 and "+str(len(options)))
        if choice.isnumeric():
            choice= int(choice)
            if choice <=len(options)  and choice>= 1:
                return choice
            else:
                print("not a good option")
        else:
            print("not a good option")
        
def playgame():
    choices=["Banker from boston", "Carpenter from Ohio", "farmer from Illinois", "whats the difference?"]
    Proffesion=""
    Money=0
    player_name=""
    family_list=[]
    food = 0
    ammo = 0
    clothes = 0
    parts = []
    ox = 0
    Proffesion, Money = char_setup(choices)
    print("You chose to be:")
    print (Proffesion)
    print ("you will start with:")
    print(Money)
    player_name,family_list = get_player_names(player_name, family_list)
    print(player_name, family_list)
    Money, food, ammo, clothes, parts, ox = shop(Money, food, ammo, clothes, parts, ox)
    

def char_setup(options):
    
    
    while True:
        print("Many kinds of people made the trip to Oregon.")
        print("you may choose to be a:")
        option=menu_function(options)

        if option== 1:
            Money=1600
            Proffesion="Banker"
            break
        elif option== 2:
            Money=800
            Proffesion="Carpenter"
            break
        elif option==3:
            Money=400
            Proffesion="Farmer"
            break
        elif option==4:
            print("Banker has 1600 dollars  carpenter has 800 dollars  farmer has 400 dollars")
    return Proffesion, Money
    

    
def learn():
    print("""Try taking a journey by covered wagon across 2000
miles of plains, rivers, and mountains. Try! on the
 plains, will you slosh your oxen through mud and
 water-filled ruts or will you plod through dust six inches deep?""")
    input("\npress Enter to continue")
    print("""How will you cross the rivers?
If you have money, you might take a ferry
(if ther is a ferry). Or, you can ford the
river and hope you and your wagon aren't swallowed alive!""")
    input("\npress Enter to continue")
    print("""What about supplies? Well, if you're
low on food you can hunt. You might get a buffalo.....
you might. And there are bear in the mountains.""")
    input("\npress Enter to continue")
    print("""At the Dalles, you can try navigating
the Columbia River, but if running the rapids with a
makeshift raft makes you queasy, better take the Barlow Road.""")
    input("\npress Enter to continue")
    print(""" If for some reason you don't survive-- your
wagon burns, or thieves steall your oxen, or you run out of
provisions, or you die of cholera--don't give up! Try again....and again...
until your name is up with the others on the Oregon Top Ten.""")
    input("\npress Enter to continue")

    print("""              The software team responsible
        for creation of this product includes:

                   Emily Briggs
                   
                   Elaina Kell
                   
                    Haley Bice""")


    
def shop(money, food, ammo, clothes, parts, ox):
    bill = 0
    items = ["oxen", "food", "ammunition", "clothes", "wagon parts", "checkout"]
    spent_on_items = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
    print("before leaving independence you should buy equipment and supplies")
    print(str.format("you have {} in cash to make  this journey", money))
    print("remember you can buy supplys along the way")
    input("press any key to continue")

    while True:
        spent_on_items[len(spent_on_items)-1] = bill
        print("welcome to Eric's Gernerel store")
        print("here is a list of things you can buy")
        for i in range(len(items)):
            print(str.format("\t{}.    {:20}    ${:.2f}", i+1, items[i], spent_on_items[i]))   

        print(str.format("total bill so far:    ${:.2f}", bill))
        print(str.format("total funds available:    ${:.2f}", money-bill))
        choice = get_number("what item would you like to buy", 1, 6)#make sure this is a call to your get number function
        if choice == 1:
            bill -=spent_on_items[0]
            ox = 0
            spent_on_items[0] = 0.00
            print("""there are 2 oxen in a  yoke;
                     I recomend at least 3 yokes.
                     I charge $40 a yoke""")
            print(str.format("total bill so far:   ${:.2f}", bill))
            answer = get_number("how many yokes would you like to buy", 1, 6)
            cost = answer*40
            ox = answer*2
            bill+= cost
            spent_on_items[0] = cost
        if choice == 2:
            bill -=spent_on_items[1]
            food = 0
            spent_on_items[1] = 0.00
            print("""I recommend you take at least 200 pounds of food for each person in your family.
                      I see that you have{} people in all.
                      you'll need flour, sugar, bacon, and coffee.
                      My price is 20 cents a pond.""")
            print(str.format("total bill so far:   ${:.2f}", bill))
            answer = get_number("how many pounds would you like to buy", 1, 100000000)
            cost = answer*0.20
            food = answer
            bill+= cost
            spent_on_items[1] = cost
        if choice == 3:
            bill -=spent_on_items[2]
            ammunition = 0
            spent_on_items[2] = 0.00
            print("""I sell ammunition in boxes of 20 bullets.
                      Each box costs $2.00.""")
            print(str.format("total bill so far:   ${:.2f}", bill))
            answer = get_number("how many boxes would you like to buy", 1, 100000000)
            cost = answer*2
            ammunition = answer*1
            bill+= cost
            spent_on_items[2] = cost
        if choice == 4:
            bill -=spent_on_items[3]
            ox = 0
            spent_on_items[3] = 0.00
            print("""You'll need warm clothing in the montains.
                     I recommend taking at least 2 sets of clothes per peson.
                     Each set is $10.00.""")
            print(str.format("total bill so far:   ${:.2f}", bill))
            answer = get_number("how many sets would you like to buy", 1, 100000000)
            cost = answer*10
            clothes = answer*1
            bill+= cost
            spent_on_items[3] = cost


    


            
        
            


    


        
def start_screen():
    start= """
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ...............................................................................................................................................................................................'........
    .............'''''''...........................................................................................................................'''''''....................................''...,'.......
    .........'x0OOOKXKOOO0k:cOKl............................:dkxxxxxxkxl'......................................................................c0OOO0XX0OOO0o................................;kKd...........
    ..........co:';OM0:';ll''OWd...........................oNXd;;;;;;c0Nk'.....................................................................;oc,'lXNd',co:............................'....dWk...........
    ..............:0NKc.....'OWd...........................xWO,.......oN0;...................................,;....................................'dXXx,..............................'ld;...dNk'..........
    ..............,ON0:.....'OMKollloxo'..,oxdlllloxd,....;ON0c......,xXKl':c;:ddodxxc'cxdolllldx:..lxdoooooxKNx..,coooolodd;;lc:llllloo:...........lKXd....;c;:oollodc.,dkdooooxOd,...lOO:...dXx'..........
    ...............xWk'.....,ONk;...:0Xo..dWKl:;;;l0Wx.....xWO'.......lN0;.'o0Kd,',lxclXNx:;;;:kW0;:KWk:;;;;:kWK::0Kl,''';xNO:c0Xk:,,,lKXc..........:KNl....'o0Kd,..';:'cOOxddddONNo...;OXl...dWx...........
    ..............'kMO,.....;0Nx'...,OXx..xWKdooooddd;.....dW0:......'xW0,..c0Kc......cXNkoooooddc.'kNOdoooodkOo,lK0:.....oXO;:0Xd....;OXo..........cXNo.....:0Kl.......kWKoccccxXWd...:0Xo...xWk'..........
    .............,okkkd,....lkkx:...ckOx:.:0Kxooooool,.....;xK0kxxxkkOKOc..'d00d'.....,kKOdoooool:.'kXkooodooxOd',okxollloOKo;oO0k;...l0Kk;........:xkkxc...'o00d,......l00doooodkkko'.lxkd,.:dxxc..........
    ........................................,;;;;;,..........',;;;;;;;'.....'..'........,;;;;;,'...,kKkddddddkKk,...,;;;;;,'..''.''...''.,'..................'..'........',,,,,,'...........................
    .................................................................................................',,,,,,,,,.............................................................................................
    ........................................................................................................................................................................................................
    ........................'''.........................................................................''.........................................................................'''......................
    .......................'','''''.....................................................................''.....................................................................''''','......................
    ..............................................................................'.....................''..................................................................................................
    ...................................................................................................'....................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    ........................................................................................................................................................................................................
    """

    print(start)
    while True:
        options= ["Start game", "Learn about trail", "Quit"]
        option =  menu_function(options)
        if option== 1:
            playgame()
            break
        elif option== 2:
            learn()
        elif option==3:
            quit()
    
    
def get_name(question):
    while True:
        name=input(question)
        if len(name)>=2:
            return name
        print("name isn't long enough")
        
def get_number(question, low, high):
    while True:
        number=input(question)
        if number.isnumeric():
            number=int(number)
            if number>=low and number<=high:
                return number
        print("Not a good input")

def get_player_names(player_name, family_list):
    player_name = get_name("Enter wagon leaders name")
    family=get_number("How many members are in your family", 2,5)
    for i in range(family):
        name = get_name("Enter family member name")
        family_list.append(name)
    return player_name, family_list


        
    

#start game
logo_screen()
start_screen()
playgame()

input()








    
