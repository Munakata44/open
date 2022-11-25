### Banking Application##

from client import Client


class BankApp(Client):
    #initializing main class client
    def __int__(self, firstname, lastname, title, pronouns, date_of_birth, balance, occupation, overdraft):
        super().__init__(firstname, lastname, title, pronouns, date_of_birth, balance, occupation, overdraft)



        """""
        #adding the self values again?
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.pronouns = pronouns
        self.date_of_birth = date_of_birth
        self.overdraft = overdraft #isnt working
        self.occupation = occupation
        self.balance = balance
        """



    #overdraft = overdraft.__add__(5)
