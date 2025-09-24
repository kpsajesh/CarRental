# car_rental.py

from datetime import datetime, timedelta

class CarRental:
    def __init__(self, stock=0): #Constructor car Rental
        self.stock = stock
        self.hourlyTariff = 200 #Rs200/hour
        self.dailyTariff1 = 1500 #Rs1500/hour
        self.weeklyTariff = 7500 #Rs7500/hour

    def display_stock(self): #Display stock available for rent
        print(f"We have currently {self.stock} cars available to rent.")
        return self.stock
    def hi(self):
        print('hi')

    

