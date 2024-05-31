import csv

# Creating a class for items
class Items:
    pay_rates = 0.8
    all = []
    def __init__(self, name, price, quantity=0):
        # Run valitation
        assert price >= 0, f"Price should be greater than zero not {self.price}"
        assert quantity >=0, f"Quantity should be positive."
        
        # Assign value
        self.__name = name
        self.price = price
        self.quantity = quantity

        # adding items in list
        Items.all.append(self)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value

    def calculate_price(self):
        return self.price * self.quantity

    def display(self):
        print(f"Item name is {self.name}.The price of item is {self.price}. And the quantity available is {self.quantity}") 

    def apply_discount(self):
        self.price = self.price * self.pay_rates

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r')as f:
            reader = csv.DictReader(f)
            items = list(reader) 

        for item in items:
            Items(
                name = item.get("name"),
                price = int(item.get("price")),
                quantity = int(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
        
class Phone(Items):
    def __init__(self, name, price, quantity=0,broken_phone=0):
        # super function
        super().__init__(name, price, quantity)
        # validation
        assert broken_phone >= 0, f"Broken phone should be greater than or equal to 0"
        # assign value
        self.broken_phone = broken_phone

    def calculate_price(self):
        return self.price * (self.quantity - self.broken_phone)    

    @property
    def read_only(self):
        return "AAA"
    
phone1 = Phone("Lava",1000,2)
phone2 = Phone("Sony",2999,10,2)
print(phone1.read_only)
phone1.read_only = "BBB"
print(phone1.read_only)
print(phone1.calculate_price())
print(phone2.calculate_price())

# Items.instantiate_from_csv()
# print(Items.is_integer(5))
# print(Items.is_integer(5.9))
# print(Items.is_integer(3.0))
# item1 = Items("Laptop", 1000, 3)
# item2 = Items("Phone", 500, 10)
# item3 = Items("Tablet", 2000, 2)
# print(item1.calculate_price())
# item1.apply_discount()
# print(item1.calculate_price())
# for instant in Items.all:
    # print(instant.name)