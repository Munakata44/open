# client class
class Client:
    def __init__(self, firstname, lastname, title, pronouns, date_of_birth, balance, occupation, overdraft):
        # instance variables
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.pronouns = pronouns
        self.date_of_birth = date_of_birth
        self.balance = balance
        self.occupation = occupation
        self.overdraft = overdraft
        #set overdraft limit for all clients
        self.overdraft_limit = 100
    #adding and removing clients
    def add_client(self,firstname, lastname, title, pronouns, date_of_birth, balance, occupation, overdraft):
        self.Client.append(add_client)
    def remove_client(self,firstname, lastname, title, pronouns, date_of_birth, balance, occupation, overdraft):
        self.

    #returning   as strings
    def __str__(self):
        return "Client ({},{},{},{},{},{})".format(self.firstname, self.lastname, self.title, self.pronouns, self.date_of_birth , self.occupation)
    #overriding the string method
    def __repr__(self):
        return "Client ({},{},{},{},{},{})".format(self.firstname, self.lastname, self.title, self.pronouns, self.date_of_birth , self.occupation)


    # showing all the client details
    def show_details(self):
        print("Client information")
        print("")
        print("Forename ", self.firstname)
        print("Surname ", self.lastname)
        print("Title ", self.title)
        print("Birthday ", self.date_of_birth)
        print("balance ", self.balance)
        print("job ", self.occupation)
        print("overdraft ", self.overdraft)

    ##getters for the variables

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def title(self):
        return self.__title

    @property
    def pronouns(self):
        return self.__pronouns

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def balance(self):
        return self.__balance

    @property
    def occupation(self):
        return self.__occupation

    @property
    def overdraft(self):
        return self.__overdraft
#setters for editing client data

    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @pronouns.setter
    def pronouns(self, pronouns):
        self.__pronouns = pronouns

    @title.setter
    def title(self, title):
        self.__title = title

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @occupation.setter
    def occupation(self, occupation):
        self.__occupation = occupation

    @overdraft.setter
    def overdraft(self, overdraft):
        self.__overdraft = overdraft

    #Functions for adding and subtracting balance
    def subtract(self, x):
        if self.balance > x:
            self.balance = self.balance - x
        else:
            y = x - self.balance
            self.balance = 0
            self.overdraft = self.overdraft - y
            print("Account has been updated: £", self.overdraft)

    def addition(self, x):
        if self.overdraft < 0:
            if abs(self.overdraft) < x:
                y = x - abs(self.overdraft)
                self.overdraft = 0
                self.balance = self.balance + y
            else:
                self.overdraft = x + self.overdraft
        else:
            self.overdraft = 0
            self.balance = self.balance + x
            print("Account has been updated: £", self.balance)

