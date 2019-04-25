class Account():
    def __init__(self,balance,name):
        self.__balance= balance
        self.name=name
    def credit(self,deposit):
        self.__balance+=deposit

    def debit(self,withdraw):
        self._balance-=withdraw

    def get_balance(self):
        return self.__balance

customer=Account(100,"mani")
#customer.name("veena")
customer.credit(100)
customer.debit(50)
