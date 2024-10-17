import math

'''
Answer to question 8a
'''
annual_rate = 0.0185 #1.85%
monthly_rate = annual_rate / 12

# we have been asked to use the monthly rate for all the questions
double_time_months = math.log(2) /math.log(1 + monthly_rate) / 12

print("\nAnswer to Question 8a")
print(f"Time in years it would take to double the money at 1.85 APR compounded monthly is: {round(double_time_months,1)} years")

# For the value of 1.85% APR, the answer is 37.5 years or 450 months, which is pretty close to the graph.

'''
Answer to question 8b
Using a lambda function to calculate the doubling time in years, and also using log base 10 instead of natural log.
'''

double_time_years_log_10 = lambda ar: (math.log10(2) /math.log10(1 + (ar / 12))) / 12
print("\nAnswer to Question 8b")
print(f"Doubling time for 1.85% APR in years using log 10 is: {round(double_time_years_log_10(0.0185),1)} years")

'''
Answer to question 8c

'''
double_time_years = lambda ar: (math.log(2) /math.log(1 + (ar / 12))) / 12
print("\nAnswer to Question 8c")
print(f"Doubling time for 3% APR in years is : {round(double_time_years(0.03),1)} years")
