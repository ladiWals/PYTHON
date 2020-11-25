class Customer:
    def __init__(self, first, last, mobile, monthly):
        self.first = first
        self.last = last
        self.mobile = mobile
        self.fullName = first + ' ' + last
        self.monthly = monthly
    def annual(self):
        self.salary = self.monthly * 12
        return '{0}, {1}'.format(self.fullName, self.salary)
    def obbyName(self):
        print('{}'.format(self.name))
cust1 = Customer('Emilee', 'Smith', '0821231234', 20000)
print(cust1.annual())
print(cust1.fullName)
print(cust1.obbyName)