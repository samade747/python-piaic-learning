# Class Variables and Class Methods
# Create a class Bank with a class variable bank_name. Add a class method 
# change_bank_name(cls, name) that allows changing the bank name. Show that 
# it affects all instances.


class Bank():
        # Class variable (sab objects ke liye common hota hai)
    bank_name = "Meezan Bank"

    #class method jo bank ja naam change karega
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Class variable ko change karega


account1 = Bank()  # Bank ka pehla object
account2 = Bank()  # Bank ka doosra object

#Dono objects ke liye bank_name ko print karte hain
print("Before changing bank name:")
print("Account 1 Bank Name:", account1.bank_name)  # "Meezan Bank" print karega
print("Account 2 Bank Name:", account2.bank_name)  # "Meezan Bank" print karega


# Bank ka naam change karte hain
account1.change_bank_name("HBL")  # Bank ka naam change kiya

#Dono objects ke liye bank_name ko print karte hain
print("\nAfter changing bank name:")
print("Account 1 Bank Name:", account1.bank_name)  # "HBL" print karega
print("Account 2 Bank Name:", account2.bank_name)  # "HBL" print karega
