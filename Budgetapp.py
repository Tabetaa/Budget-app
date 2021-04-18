class budget:

    def __init__(self, category, balance):
        self.category = category
        self.balance = balance

    def deposit(self, depositamount):
        self.balance = self.balance + depositamount

        return f"new balance is £ {self.balance} in {self.category} budget"

    def withdraw(self, withdrawalamount):
        if self.balance <= withdrawalamount:
            feedback = "Take your cash /n"
            feedback += f"new balance is £{self.balance} in {self.category} budget"
            return feedback
        else:
            return "insufficient funds, please enter a lesser amount"

    def category_balance(self):
        feedback = f"your balance is £{self.balance} in {self.category} budget"
        return feedback

    def transfer(self, transferamount, transfercategory):
        if self.balance <= transferamount:
            return "insufficient funds, please enter a lesser amount"
        else:
            self.balance -= transferamount
        transfercategory.balance += transferamount
        feedback = "                        \n"
        feedback += f"your new balance for {transfercategory.category} is £{transfercategory.balance}\n"
        feedback += f"the balance in {self.category}  is {self.balance}"

        return feedback


food = budget("food", 2000)
entertainment = budget("entertainment", 3000)

print(entertainment.transfer(1000, food))
print(f"{food.category} budget has £{food.balance}")
print("------------------------------------------")
print(f"{entertainment.category} budget has £{entertainment.balance}")
print("                                   ")
print(food.deposit(2000))
print("                                   ")
print(entertainment.deposit(4000))
print(food.category_balance())