# Exercise 55:  Bank account
# 1) Create a Python class named CompteBankaire that represents a bank account, with the following attributes: numeroCompte (numeric type), name (name of the account owner of the string type), balance.
# 2) Create a constructor with the following parameters: numeroCompte, name, balance.
# 3) Create a method Paiement() that manages the deposits.
# 4) Create a method Retrait() that manages the withdrawals.
# 5) Create a method Agios() to apply the agios to a percentage of 5% of the balance
# 6) Create a method affiche() to display the details on the account
# 7) Give the complete code of the CompteBankaire class.

class CompteBankaire:
    def __init__(self, numeroCompte: int, name: str, balance: float):
        self.numeroCompte = numeroCompte
        self.name = name
        self.balance = balance

    def Paiement(self, amount: float):
        self.balance += amount
        print(f"Deposit: {amount} \nNew Balance: {self.balance}")

    def Retrait(self, amount: float):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawal: {amount} \nNew Balance: {self.balance}")
        
    def apply_agios(self):
        self.balance -= (self.balance * 0.05)
        print(f"Agios applied. New Balance: {self.balance}")
    
    def affiche(self):
        print(f"Account Number: {self.numeroCompte}\nAccount Holder: {self.name}\nBalance: {self.balance}\n")


# Example usage
a1 = CompteBankaire(2201, 'Nihal', 1600)
a1.affiche()

a1.Paiement(200)
a1.affiche()

a1.Retrait(500)
a1.affiche()

a1.apply_agios()
a1.affiche()
