"""Employee pay calculator."""


class MonthlySalaryBuilder:
    def __init__(
        self,
        amount,
    ):
        self.amount = amount

    def get_pay(self):
        return self.amount

    def __str__(self):
        return f"monthly salary of {self.amount}"


class HourlySalaryBuilder:
    def __init__(self, hour, hour_wage):
        self.hour = hour
        self.hour_wage = hour_wage

    def get_pay(self):
        return self.hour_wage * self.hour

    def __str__(self):
        return f"contract of {self.hour} hours at {self.hour_wage}/hour"


class NoCommissionBuilder:
    def get_pay(self):
        return 0

    def __str__(self):
        return ""


class BonusCommissionBuilder:
    def __init__(self, bonus):
        self.bonus = bonus

    def get_pay(self):
        return self.bonus

    def __str__(self):
        return f" and receives a bonus commission of {self.bonus}"


class ContractCommissionBuilder:
    def __init__(self, contract_num, commission):
        self.contract_num = contract_num
        self.commission = commission

    def get_pay(self):
        return self.contract_num * self.commission

    def __str__(self):
        return f" and receives a commission for {self.contract_num} contract(s) at {self.commission}/contract"


class Employee:
    def __init__(
        self,
        name,
        contract_type=MonthlySalaryBuilder(0),
        commission_type=NoCommissionBuilder(),
    ):
        self.name = name
        self.contract_type = contract_type
        self.commission_type = commission_type

    def get_pay(self):
        return self.contract_type.get_pay() + self.commission_type.get_pay()

    def __str__(self):
        return f"{self.name} works on a {self.contract_type}{self.commission_type}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", MonthlySalaryBuilder(4000))
print(billie)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", HourlySalaryBuilder(100, 25))
print(charlie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", MonthlySalaryBuilder(3000), ContractCommissionBuilder(4, 200))
print(renee)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", HourlySalaryBuilder(150, 25), ContractCommissionBuilder(3, 220))
print(jan)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", MonthlySalaryBuilder(2000), BonusCommissionBuilder(1500))
print(robbie)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", HourlySalaryBuilder(120, 30), BonusCommissionBuilder(600))
print(ariel)
