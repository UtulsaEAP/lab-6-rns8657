def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = 0
    
    price1 = services.get(service_choice1)
    price2 = services.get(service_choice2)
    print("ZyCar Wash \n " + "Base car wash - $10 \n" + service_choice1 + " - $" + str(price1) + "\n" + service_choice2 + " - $" + str(price2) + "\n" + "-----" + "\n" + "Total price: " + str(price1 + price2 + 10))
    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
