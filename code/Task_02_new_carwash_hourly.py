import numpy as np

# Cars washed in each hour of a 12-hour day (8 am to 7 pm)
hours = np.arange(8, 20)
cars = np.array([3, 5, 8, 11, 14, 12, 9, 10, 13, 11, 7, 4])
price_kes = 600            # assumed price of a standard wash

revenue = cars * price_kes                     # vectorized: one line, all hours
weekend_revenue = revenue * 1.10               # assumed 10% weekend surcharge

busiest = hours[np.argmax(cars)]
print("Total cars washed:", cars.sum())
print(f"Mean cars per hour: {cars.mean():.2f}")
print(f"Busiest hour starts at: {busiest}:00 with {cars.max()} cars")
print("Hourly revenue (KES):", revenue)
print(f"Total weekday revenue: KES {revenue.sum():,.0f}")
print(f"Total weekend revenue: KES {weekend_revenue.sum():,.0f}")
print("Hours with fewer than 6 cars:", hours[cars < 6])
