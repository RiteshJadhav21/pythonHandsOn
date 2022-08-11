from abc import ABC, abstractmethod
#
# class Loan(ABC):
#
#     @abstractmethod
#     def cust_verification(self):
#         pass
#
#     # myabstmethod = abstractmethod(cust_verification)
#
# class ICICILoan(Loan):
#
#     def cust_verification(self):
#         aadhar_num = input("Enter your aadhar number:")
#         print("Successfully verified")
#
#     def issue_loan(self, amount):
#         self.cust_verification()
#         print(f"Your loan for amount {amount} has been approved and amount disbursed.")
#
# l1 = ICICILoan()
# l1.issue_loan(25000)

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def parimeter(self):
        pass

class Sqaure(Shape):
    def __init__(self,s):
        self.sides=s

    def area(self):
        return self.sides*self.sides

    def parimeter(self):
        return self.sides*4





s=Sqaure(5)

print(s.area())
print(s.parimeter())