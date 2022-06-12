class Category:
    def __init__(self,Category):
        self.ledger=[]
        self.balance=0.00
        self.Category=Category
    
    def __repr__(self):
        topbar=self.Category.center(30,'*')+'\n'
        body=''
        for i in self.ledger:
            temp=i['description'].ljust(23)
            temp=temp[:23]
            num='%.2f'%i['amount']
            body+=f"{temp}{str(num).rjust(7)}\n"
        total=f'{self.balance:.2f}'
        return topbar+body+f'Total: {total}'

    def deposit(self,amount,description=""):
        self.ledger.append({"amount":amount,"description":description})
        self.balance+=amount

    def withdraw(self,amount,description=""):
        if self.get_balance()>=amount:
            self.ledger.append({"amount":-1*amount,"description":description})
            self.balance-=amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
    def transfer(self,amount,obj):
        if self.withdraw(amount,f'Transfer to {obj.Category}'):
            obj.deposit(amount,f'Transfer from {self.Category}')
            return True
        else:
            return False

    def check_funds(self,amount):
        return amount<=self.get_balance()

    
def create_spend_chart(categories):
    history=[]
    for i in categories:
        ans=0
        for j in i.ledger:
            if j['amount']<0:
                ans+=abs(j['amount'])
        ans=round(ans,2)    
        history.append(ans)
    body=''
    for i in range(100,-1,10):
        temp=str(i)
        temp.rjust(4)
        body+=temp
        body+=' '
        for j in history:
            if j>=i:
                body+=f'o  '
            else:
                body+=f'   '
        body+='\n'
    maxi=-1
    for i in categories:
        maxi=max(maxi,len(i.Category))
    for i in range(maxi-1):
        body+='     '
        for j in categories:
            if i<len(j.Category):
                body+=f'{j.Category[i]}  '
            else:
                body+=f'   '
        body+='\n'
    body+='     '
    for j in categories:
        if maxi-1<len(j.Category):
            body+=f'{j.Category[maxi-1]}  '
        else:
            body+=f'   '
    return 'Percentage spent by category'+body
