# WRITE YOUR SOLUTION HERE:
class BankAccount:
	def __init__(self, owner: str, acc_num: str, balance: float):
		self.__balance = balance
		self.__owner = owner
		self.__acc_num = acc_num

	def deposit(self, amount: float):
		self.__balance += amount
		self.__service_charge()
		

	def withdraw(self,amount: float):
		self.__balance -= amount
		self.__service_charge()

	@property
	def balance(self):
		return self.__balance

	def __service_charge(self):
		self.__balance -= self.__balance / 100
		

if __name__ == "__main__":
	account = BankAccount("Randy Riches", "12345-6789", 1000)
	account.withdraw(100)
	print(account.balance)
	account.deposit(100)
	print(account.balance)