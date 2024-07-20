# class JawnPakistan:
#     class Parrot:
    
#     # class attribute
#      species = 'bird'
    
#     # instance attribute
#      def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     # instantiate the Parrot class
#     blu = Parrot('Blu', 10)
#     woo = Parrot('woo', 15)
    
#     # access the class attributes
#     print('Blu is a {}'.format(blu.__class__.species))
#     print('Woo is also a {}'.format(woo.__class__.species))
#     # access the instance attributes
#     print('{} is {} years old'.format( blu.name, blu.age))
#     print('{} is {} years old'.format( woo.name, woo.age))

from datetime import date

# class Person:
#     def __init__(self, name, country, dob):
#         self.name = name
#         self.country = country
#         self.dob = dob

#     def calculate_age(self):
#         today = date.today()
#         birth_date = date(*map(int, self.dob.split('-')))
#         age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#         return age
    
# person = Person("hammad ", "paksitan ", "2006-05-13")
# print(f"{person.name} from {person.country} is {person.calculate_age()} years old.")




# class Person : 
#     def __init__(self , number, passing ) 
         

# from datetime import date

# class Person:
#     def __init__(self, number, passing_percent, year_of_passing):
#         self.number = number
#         self.passing_percent = passing_percent
#         self.year_of_passing = year_of_passing

#     def calculate_age(self):
#         current_year = date.today().year
#         age = current_year - self.year_of_passing
#         return age

# # Example usage
# person = Person(12345, 85.5, 2005)
# print(f"Person with number {person.number} passed with {person.passing_percent}% in the year {person.year_of_passing}.")
# print(f"Age since passing: {person.calculate_age()} years.")



# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             return "Cannot divide by zero!"
#         return a / b

# # Example usage
# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.subtract(5, 3))
# print(calc.multiply(5, 3))
# print(calc.divide(5, 3))



# class ShoppingCart:
#     def __init__(self):
#         self.items = {}

#     def add_item(self, item, price):
#         if item in self.items:
#             self.items[item] += price
#         else:
#             self.items[item] = price

#     def remove_item(self, item):
#         if item in self.items:
#             del self.items[item]

#     def calculate_total(self):
#         return sum(self.items.values())

# # Example usage
# cart = ShoppingCart()
# cart.add_item("Apple", 12.50)
# cart.add_item("Banana", 24.00)
# print(cart.calculate_total())
# cart.remove_item("Banana")
# print(cart.calculate_total())

