from datetime import datetime, timedelta
from IPython.display import clear_output 

class CarRental:
    def __init__(self, stock=0): #Constructor car Rental
        self.stock = stock
        self.runningStock = stock
        self.hourlyTariff = 200 #Rs200/hour
        self.dailyTariff = 1500 #Rs1500/hour
        self.weeklyTariff = 7500 #Rs7500/hour

        self.billAmount = 0

    def ShowAvailableStock(self): #Display the running stock available for rent 
        return self.runningStock
    
    def ShowMaxStock(self): #Display the max stock
        return self.stock

    def RentCar(self,rentCount): #Issue cars in hourly/daily/weekly rent basis
        self.runningStock -= rentCount
        return True
    
    def ReturnDaily(self,daysUsed,noofCars):
        self.billAmount = daysUsed * noofCars * self.dailyTariff
        self.runningStock += noofCars
        return self.billAmount

    def ReturnHourly(self,hoursUsed,noofCars):
        self.billAmount = hoursUsed * noofCars * self.hourlyTariff 
        self.runningStock += noofCars
        return self.billAmount
    
    def ReturnWeekly(self,weeksUsed,noofCars):
        self.billAmount = weeksUsed * noofCars * self.weeklyTariff 
        self.runningStock += noofCars
        return self.billAmount


#*********************************************************************************************************   
class Customer():
    def __init__(self):        
        self.dailyCarRequestCount = 0 #Car request count - Daily
        self.dailyFromDate = 'NoDate' #Car request From date - Daily
        self.dailyCarReturnCount = 0  #Car return count - Daily
        self.dailyToDate = 'NoDate'   #Car return To date - Daily
        self.DailyHiredDays = 0       #No. of days hired

        self.hourlyCarRequestCount = 0 #Car request count - Hourly
        self.hourlyFromHour = 0        #Car request From hour - Hourly
        self.hourlyCarReturnCount = 0  #Car return count - Hourly
        self.hourlyToHour = 0          #Car return To hour - Hourly
        self.hourlyHiredhours = 0      #No. of hours hired

        self.weeklyCarRequestCount = 0 #Car request count - Weekly
        self.weeklyFromWeek = 0        #Car request From hour - Weekly
        self.weeklyCarReturnCount = 0  #Car return count - Weekly
        self.weeklyToWeek = 0          #Car return To hour - Weekly
        self.weeklyHiredWeeks = 0      #No. of hours hired
        
    def RequestCarHourly(self,carStock):   #Method to request cars on DAILY RENTAL basis     
        #Getting and validating the no. of car request for rent
        print(f'Currently available cars to rent:{carStock}')
        strCountCarMsg = 'HOURLY RENTAL HIRE: How many cars you would like to rent? Request between 1 and '+ str(carStock) + '.'
        self.hourlyCarRequestCount = UserInputNumberBetween(1,carStock,strCountCarMsg)

        #Getting and validating the from hour of rent
        strCountCarMsg = 'HOURLY RENTAL HIRE: Enter from hour of hire.? Enter between 1 and 24.'
        self.hourlyFromHour = UserInputNumberBetween(1,24,strCountCarMsg) 

    def RequestCarWeekly(self,carStock):   #Method to request cars on DAILY RENTAL basis     
        #Getting and validating the no. of car request for rent
        print(f'Currently available cars to rent:{carStock}')
        strCountCarMsg = 'WEEKLY RENTAL HIRE: How many cars you would like to rent? Request between 1 and '+ str(carStock) + '.'
        self.weeklyCarRequestCount = UserInputNumberBetween(1,carStock,strCountCarMsg)

        #Getting and validating the from hour of rent
        strCountCarMsg = 'WEEKLY RENTAL HIRE: How many weeks you would like to hire? Select between 1 and 52.'
        self.weeklyFromWeek = UserInputNumberBetween(1,52,strCountCarMsg) 
    
    def ReturnCarHourly(self):
        #Getting and validating the no. of car return for rent   
        self.hourlyCarReturnCount = self.hourlyCarRequestCount
        print(f'HOURLY HIRE RETURN: You have rented {self.hourlyCarRequestCount} car/s from {self.hourlyFromHour}th hour.')

        #Getting and validating the end hour of rent
        strCountCarMsg = 'HOURLY RENTAL RETURN: Enter end hour of hire.? Enter between 1 and 24.'
        self.hourlyToHour = UserInputNumberBetween(1,24,strCountCarMsg) 

        HourlyHiredhours = self.hourlyToHour - self.hourlyFromHour
        if HourlyHiredhours > 0:
            return HourlyHiredhours
        else:
            print('HOURLY RENTAL RETURN: Error. Recheck the from hour and end hour.')
            return 0

    def ReturnCarWeekly(self):
        #Getting and validating the no. of car return for rent   
        self.weeklyCarReturnCount = self.weeklyCarRequestCount #weeklyCarReturnCount 
        print(f'WEEKLY HIRE RETURN: You have rented {self.weeklyCarReturnCount} car/s for {self.weeklyFromWeek} week/s.')  

        self.weeklyHiredWeeks = self.weeklyFromWeek
        return self.weeklyHiredWeeks
    
    def RequestCarDaily(self,carStock):   #Method to request cars on DAILY RENTAL basis     
        #Getting and validating the no. of car request for rent
        print(f'Currently available cars to rent:{carStock}')
        strCountCarMsg = 'DAILY RENTAL HIRE: How many cars you would like to rent? Request between 1 and '+ str(carStock) + '.'
        self.dailyCarRequestCount = UserInputNumberBetween(1,carStock,strCountCarMsg)

        #Getting and validating the from date of rent
        while True:            
            date1 = input('DAILY RENTAL HIRE: Enter from date of hire.')
            if DateValidation(date1) == True:
                self.dailyFromDate = date1
                break
            else:
                print('DAILY RENTAL HIRE: Error. Invalid from date of hire')
       
    def ReturnCarDaily(self):
        #Getting and validating the no. of car return for rent
        #print(f'Total no. of cars can return: {maxCarsCanReturn}')
        self.dailyCarReturnCount = self.dailyCarRequestCount
        print(f'DAILY HIRE RETURN: You have rented {self.dailyCarRequestCount} car/s from {self.dailyFromDate} date.')
        date1 = self.dailyFromDate
        
        #Getting and validating the end date of rent
        while True:            
            date2 = input('DAILY RENTAL RETURN: Enter end date of hire.')
            if DateValidation(date2) == True:
                self.dailyToDate = date2
                break
            else:
                print('DAILY RENTAL RETURN: Error. Invalid end date of hire.')

        #Getting the no. of days between the from and to dates
        DailyHiredDays = DaysBetween(date2,date1)
        if DailyHiredDays > 0:
            return DailyHiredDays
        else:
            print('DAILY RENTAL RETURN: Error. Recheck the from date and end date.')
            return 0

# Validation: Number validation for a range
def UserInputNumberBetween(FromNum,ToNum,strInputMsg):  
    ToNumEnd = ToNum + 1
    strInputMsg = strInputMsg +': '
    while True:
        a = input(strInputMsg)
        if a in map(str,range(FromNum,ToNumEnd)):
            a = int(a)
            break
        else:
            print('Error, please enter a number between', FromNum,'and',ToNum,'.')
    return a
        
# Validation: Date
def DateValidation(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%d/%m/%Y").strftime('%d/%m/%Y'):
            raise ValueError
        
        #weeklyFromDate = date_text
        return True
    except ValueError:
        return False

# Validation: Number of days between 2 dates
def DaysBetween(d1, d2):
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%d/%m/%Y")
    if d1 >= d2:
        return abs((d2 - d1).days) + 1
    else:
        return -1