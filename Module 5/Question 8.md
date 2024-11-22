#### The Doubling Time formula below is used in Finance to calculate the length of time required to double an investment or money in an interest bearing account.

#### Doubling Time= log(2) / log(1 + r)

#### Where r is the rate of return

#### If one wishes to calculate the amount of time to double their money in a money market account that is compounded monthly, then r needs to express the monthly rate and not the annual rate. The monthly rate can be found by dividing the annual rate by 12. With this situation, the doubling time formula will give the number of months that it takes to double money and not years  (Please use monthly rate for 8a - 8c)

#### 8a - Marc wants to determine how long it would take to double the money in his money market account in BMO Harris Bankin 2020. BMO offers a 1.85% APR, which is compounded monthly. How long would it take Marc to double his money by investing with BMO? Please round to 1 decimal place. (You can use the figure above to check your answer).

Answer

The answer in code form is in the Question 8.py file. (8a)
I converted the annual rate to monthly rate, then used that rate in the equation.

#### 8b - Write a lambda function (doubling_time_yrs) that returns the time it will take to double his money in years. Use math.log10(a) to get the base-10 logarithm of a number in the formula.

The answer in code form is in the Question 8.py file. (8b)
Here I pass in the annual rate of 1.85% and use the log10 in the lambda function, which converts it into monthly rate
and returns the value

#### 8c - According to your ACME broker The 10-year average annual return on the S&P 500, ending in 2018 and including dividends, is around 10%. However your ACME broker is recommending that you open a money market account since stock market volatility is high (understanding you will experience down years as well as up years - no guarantees). How long would it take Marc to double his money if he invests in a money market account that will compound monthly and earn him 3% per year ? You can use the figure above to check your answer (round to 1 decimal place)

The answer in code form is in the Question 8.py file (8c)
Here I pass in the annual rate of 3% and use the natural log in the lambda function, which converts it into monthly rate
and returns the value

#### Side Note

During out breakout session, we discovered that when we remove the rounding, that there was no difference between the
answer of log10 and natural log. 


