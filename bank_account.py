# creates class for the bank account function that shows the user their balance,
# and has availibility to deposit/withdraw/show balance

class BankAccount(object):
	balance = 0

	def __init__(self, name):
		self.name = name

	def __repr__(self):    #The __repr__() method defines what represents the object when a user tries to print that object using print
		return "This account belongs to %s; the balance is %.2f" % (self.name, self.balance)

	def show_balance(self):
		return "Balance is %.2f" % self.balance

	def deposit(self, amount):
		if amount <= 0:
			print "wrong amount"
			return
		else:
			print "This is the amount you are depositing: %.2f" % amount
			self.balance += amount 
			print self.show_balance()

	def withdraw(self, amount):
		if amount > self.balance:
			print "Wrong amount"
			return
		else:
			print "This is the amount you are withdrawing: %.2f" % amount
			self.balance -= amount
			print self.show_balance()

my_account = BankAccount("Phil")
print my_account
print my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
my_account.withdraw(500)
print my_account

