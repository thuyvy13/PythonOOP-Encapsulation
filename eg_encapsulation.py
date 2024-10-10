# Ví dụ 1
class Person:
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if len(name) > 0:
            self._name = name
        else:
            print("Tên không được để trống")
 
 #sử dụng class Person           
person = Person("Hoà")
print("Tên ban đầu: ", person.get_name()) #lấy giá trị của tên thông qua getter
person.set_name("Khánh") #đổi tên thông qua setter
print("Tên mới: ", person.get_name())
person.set_name("") #tên không được để trống 


#Ví dụ 2
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance #thuộc tính ẩn
    
    def get_balance(self):
        return self.__balance
    
#sử dụng: 
account = BankAccount(1000)
print(account.get_balance()) #truy cập thông qua getter


