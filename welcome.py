from get_name import *
from validate_age import *

print("="*35)
print("Welcome to voting eligilibity check")
print("="*35)
print("\n")

user_name = get_name()
print(f"hello {user_name}!\n")

age = int(input("Enter your age: "))
validate_age(age)
