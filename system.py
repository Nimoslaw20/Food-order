#Author: Emmanuel Nimo
#Simulation of cutomer service at Akornor Cafeteria using Queue





#A class for Customer details
class Customer:
    def __init__(self, name, food, amount):
        self.name = name
        self.food = [ ]
        self.food.append(food)
        self.amount = amount


#Accessor methods
    def getName(self):
        return self.name

    def getfood(self):
        return self.food

    def getAmount(self):
        return self.amount

#Mutator method

    def setName(self, newName):                    
        self.name = newName

    def setFood(self, newFood):
        self.food = newFood

    def setAmount(self, newAmount):
        self.amount = newAmount

    def __str__(self):
        s = ""
        for i in self.food:
            s = s + i  + ' , '  
        return "Customer details: " + self.name + "\nItems: \n" + s + "\nAmount: " + str(self.amount)


#A class of the Queue method

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    
def printMenu():
    print('AVAILABLE OPTION AT AKORNOR CAFETERIA: \n'+
          '1. Buy Food \n2. End ')

def readCommand():                                                    #Asking Customer's service
    command = input('How may I help you?: ')
    args = command.lower()
    #print(args)
    return args

def readFMCommand():                                                               #Input for addition food items
    command = input('Do you want to buy another food? (y or n): ')
    ask = command.lower()
    return ask

    
def OrderSys():
        printMenu()
        args = readCommand()
        x = Queue()
        while (args != 'end'):
            c = Customer(None, None, 0)
            NAME = str(input('Enter your name: '))           # customer input name
            foodlist = []                                            # Foodlist for one or more items
            FOOD = str(input('Enter the food: '))              #Customer input food name
            foodlist.append(FOOD)
            ask = readFMCommand()
            while (ask != 'n'):
                Extra = str(input('Which food please?: '))
                foodlist.append(Extra)
                ask = readFMCommand()
                            
            AMOUNT = float(input('Enter the money you have: '))                      #Customer input money
            c.setFood(foodlist)
            c.setName(NAME)
            c.setAmount(AMOUNT)
            x.enqueue(c)
            b = x.peek()
            args = readCommand()

        if(x.isEmpty()):
            print("You entered nothing")
            return
        print("The available orders are: ")                          
        while(not x.isEmpty()):
            print(x.dequeue())                                                                #Show the content of the Queue with first order being first output
        print('\n')
        print('1st : ', b)


        
    
        
OrderSys()        

        

        

    


