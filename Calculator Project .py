class Calculator:
    def __init__(self):
        self.result = 0.0
        self.firstnum = 0.0
        self.secondnum = 0.0
        self.options = ""
        self.temp = 0.0

    def add(self):
        print("~~~~~~~ Welcome to Add ~~~~~~~~~~")
        str_firstnum = input("Please enter the first number: ")
        str_secondnum = input("Please enter the second number: ")
        try:
            self.firstnum = float(str_firstnum)
            self.secondnum = float(str_secondnum)
            self.result = (self.firstnum + self.secondnum)
            print(f"The sum of the two numbers you entered is = {self.result}")
        except ValueError:
            print("\nError :( ")
            print("Please enter numbers only")

    def sub(self):
        print("~~~~~~~ Welcome to Subtract ~~~~~~~~~~")
        str_firstnum = input("Please enter the first number: ")
        str_secondnum = input("Please enter the second number: ")
        try:
            self.firstnum = float(str_firstnum)
            self.secondnum = float(str_secondnum)
            if self.firstnum < self.secondnum:
                print("Error.. Swapping the first num with second num... ")
                self.temp = self.secondnum
                self.secondnum = self.firstnum
                self.firstnum = self.temp 
                self.result = (self.firstnum - self.secondnum)
                print(f"The sub of the two numbers you entered is = {self.result}")
            else:
                self.result = (self.firstnum - self.secondnum)
                print(f"The sub of the two numbers you entered is = {self.result}")
        except ValueError:
            print("\nError :( ")
            print("Please enter numbers only")

    def mul(self):
        print("~~~~~~~ Welcome to Multiplication ~~~~~~~~~~")
        str_firstnum = input("Please enter the first number: ")
        str_secondnum = input("Please enter the second number: ")
        try:
            self.firstnum = float(str_firstnum)
            self.secondnum = float(str_secondnum)
            self.result = (self.firstnum * self.secondnum)
            print(f"The mul of the two numbers you entered is = {self.result}")
        except ValueError:
            print("\nError :( ")
            print("Please enter numbers only")

    def div(self):
        print("~~~~~~~ Welcome to Division ~~~~~~~~~~")
        str_firstnum = input("Please enter the first number: ")
        str_secondnum = input("Please enter the second number: ")
        try:
            self.firstnum = float(str_firstnum)
            self.secondnum = float(str_secondnum)
            if self.secondnum != 0.0:
                self.result = (self.firstnum / self.secondnum)
                print(f"The div of the two numbers you entered is = {self.result}")
            else:
                print("Error! Number cannot be divided by zero...")
        except ValueError:
            print("\nError :( ")
            print("Please enter numbers only")

    def front_end_user(self):
        try:
            while True:
                print("\n~~~~~~ Welcome to the Calculator App ~~~~~~~")
                print("Enter '+' for Addition")
                print("Enter '-' for Subtraction")
                print("Enter '*' for Product")
                print("Enter '/' for  Division")
                print("Enter CRTL+C TO EXIT")
                self.options = input("Enter a choice ranging from '+','-','*','/','%': ")

                if self.options == "+": 
                    self.add()
                elif self.options == "-": 
                     self.sub()
                elif self.options == "*":
                    self.mul()
                elif self.options == "/":
                    self.div()
                else:
                    print("\nError...")
                    print("Please enter from these options '+','-','*','/','%' ")
        except KeyboardInterrupt:
            print("\nExiting from the Calculator App...")

calc = Calculator()
calc.front_end_user()








