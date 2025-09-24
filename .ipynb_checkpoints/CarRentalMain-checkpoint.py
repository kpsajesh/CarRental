{
 "cells": [
  {
   "cell_type": "raw",
   "id": "5ae74a44-82ad-4741-8399-328ab4d28fec",
   "metadata": {},
   "source": [
    "from car_rental import CarRental, Customer\n",
    "\n",
    "def main():\n",
    "    car_rental = CarRental(100)  # Initialize the Car Rental system with 100 cars\n",
    "    customer = Customer()  # Initialize a new customer\n",
    "\n",
    "    while True:\n",
    "        print(\"\n",
    "        ====== Car Rental Shop ======\n",
    "        1. Display available cars\n",
    "        2. Request a car on hourly basis $5/hour\n",
    "        3. Request a car on daily basis $20/day\n",
    "        4. Request a car on weekly basis $60/week\n",
    "        5. Return a car\n",
    "        6. Exit\n",
    "        \")\n",
    "        choice = input(\"Enter your choice: \")\n",
    "\n",
    "        try:\n",
    "            choice = int(choice)\n",
    "        except ValueError:\n",
    "            print(\"Please enter a number between 1-6.\")\n",
    "            continue\n",
    "\n",
    "        if choice == 1:\n",
    "            car_rental.display_stock()\n",
    "\n",
    "        elif choice == 2:\n",
    "            customer.rental_time = car_rental.rent_hourly(customer.request_car())\n",
    "            customer.rental_basis = 1\n",
    "\n",
    "        elif choice == 3:\n",
    "            customer.rental_time = car_rental.rent_daily(customer.request_car())\n",
    "            customer.rental_basis = 2\n",
    "\n",
    "        elif choice == 4:\n",
    "            customer.rental_time = car_rental.rent_weekly(customer.request_car())\n",
    "            customer.rental_basis = 3\n",
    "\n",
    "        elif choice == 5:\n",
    "            customer_bill = car_rental.return_car(customer.return_car())\n",
    "            customer.rental_basis, customer.rental_time, customer.cars = 0,0,0\n",
    "\n",
    "        elif choice == 6:\n",
    "            break\n",
    "\n",
    "        else:\n",
    "            print(\"Invalid input. Please enter a number between 1-6.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09c8a1b5-e0f7-42dd-9333-abbc45df24a7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
