# This program calculates and displays travel expenses

# 10/24/2023

# CTI-110 P1HW2 - Travel Expense

# Alex Morris

print('This program calculates and displays travel expenses')
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))
print("")
print('------------Travel Expenses------------')
print("Location: ",destination)
print("Initial Budget: ",budget)
print("")
print("Fuel: ",gas)
print("Accomodation: ",hotel)
print("Food: ",food)
print("")
print("Remaining Balance: ",budget-gas-hotel-food)




