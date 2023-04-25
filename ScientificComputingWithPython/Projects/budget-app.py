class Category:

    def __init__(self, category = "", balance = 0, totwithdrawal = 0):
        self.category = category
        self.ledger = list()
        self.balance = balance
        self.totwithdrawal = totwithdrawal  #sum of all withdrawals necessary for percentage calculation
    
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
    
    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            self.totwithdrawal += amount
            return True
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, "Transfer to " + category.category)
            category.deposit(amount, "Transfer from " + self.category)
            return True
    
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
    
    def __str__(self):
        
        title = self.category.center(30, "*") + "\n"
        
        operations = ""
        for operation in self.ledger:
            d = operation["description"][:23]
            a = format(operation["amount"], '.2f')[:7]
            operations += d + a.rjust(30 - len(d)) + "\n"
        
        total = "Total: " + str(self.balance)

        return title + operations + total

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(food)
print(entertainment)
print(business)

def create_spend_chart(categories):

    totwithdrawal = 0   #total withdrawal for percentage calculation
    for category in categories:
        totwithdrawal += category.totwithdrawal
    pctline = ""    #percentage line
    for i in range(100, -10, -10):
        pctline += (str(i) + "|").rjust(4)
        for category in categories:
            pct = int(category.totwithdrawal / totwithdrawal * 100)
            if pct >= i:
                pctline += "o".center(3)
            else:
                pctline += " ".center(3)
        pctline += " "  #space necessary to match the test result
        if i > 0:   #avoid \n not necessary
            pctline += "\n"
    
    hline = ""  #horizontal line
    for i in range(len(categories)):
        hline += "---"
    hline = "    " + hline + "-"

    longcat = 0 #number of lines calculation, search for the category with the biggest number of character
    for category in categories:
        if len(category.category) > longcat:
            longcat = len(category.category)
    catline = ""    #category lines
    for i in range(longcat):
        catline += "    "
        for category in categories:
            if i < len(category.category):
                catline += category.category[i].center(3)
            else:
                catline += " ".center(3)
        catline += " "  #space necessary to match the test result
        if i < longcat - 1: #avoid \n not necessary
            catline += "\n"
    
    return "Percentage spent by category" + "\n" + pctline + "\n" + hline + "\n" + catline

print(create_spend_chart([business, food, entertainment]))