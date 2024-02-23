#Eg - 1
class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a+b+c)

obj = Calculation()
obj.add()
obj.add(1)
obj.add(1,2)
obj.add(1,2,3)
