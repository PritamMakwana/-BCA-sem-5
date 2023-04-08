print("1.single inheritance")

#single inheritance
class Bank(object):
    cash=500000
    @classmethod
    def available_cash(cls):
        print(cls.cash)
class AndhraBank(Bank):
 pass

class StateBank(Bank):
 cash=200000
 @classmethod
 def available_cash(cls):
    print(cls.cash+Bank.cash)

a=AndhraBank()
a.available_cash()
s=StateBank()
s.available_cash()

print("multipale inheritance")
#multiple inheritance
class Father:
 def height(self):
        print("Height is 6.0 Foot")
class Mother:
 def color(self):
    print("Color is Brown")
class Child(Father,Mother):
 pass
c=Child()
print("Child's inherited qualities: ")
c.height()
c.color()