import json
class banking():
    def __init__(self,name,dob,address,ph_no,acc_no, balance=1000):
        self.name=name
        self.dob=dob
        self.ph_no=ph_no
        self.address=address
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print('Amount Deposited Successfully')
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print('Amount Withdrawn Successfully')
        else:
            print('Insufficient Balance')
    def check_balance(self):
        print('Current Balance:', self.balance)
print('Account Details:')
name=input('Enter Account holder name:')
acc_no=input('Enter Account number:')
dob=input('Enter DOB(DD-MM-YYYY):')
address=input('Enter Address:')
ph_no=input('Enter Phone number:')
account=banking(name,dob,address,ph_no,acc_no)
while True:
    print("\n -----BANKING SYSTEM-----")
    print('1.Deposit')
    print('2.Withdrawal')
    print('3.Check Balance')
    choice=input('Enter choice:')
    if choice=="1":
        amount=float(input('Enter Deposit Amount:'))
        account.deposit(amount)
        break
    elif choice=='2':
        amount=float(input('Enter Withdrawl Amount:'))
        account.withdraw(amount)
        break
    elif choice=="3":
        account.check_balance()
        break
    else: 
        print('Invalid choice')
print('Thankyou for using the BANKING SYSTEM')
list=['name','dob','address','ph_no','acc_no','balance']
with open("banking.json","w") as f:
    json.dump([list, [account.name,account.dob,account.address,account.ph_no,account.acc_no,account.balance]],f)

with open("banking.json") as f:
    data=json.load(f)
    print(data[0])
    print(data[1])

