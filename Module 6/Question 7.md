#### Question 7

My solution checks if a famous individual is in the `famous_list` by matching their name,
accounting for case insensitivity, and then responding accordingly.

```python
# The famous list of people
famous_list = '''\

Marilyn Monroe (1926 – 1962) American actress, singer, model
Abraham Lincoln (1809 – 1865) US President during American civil war
Nelson Mandela (1918 – 2013)  South African President anti-apartheid campaigner
John F. Kennedy (1917 – 1963) US President 1961 – 1963
Martin Luther King (1929 – 1968)  American civil rights campaigner
Queen Elizabeth II (1926 – ) British monarch since 1954
Winston Churchill (1874 – 1965) British Prime Minister during WWII
Donald Trump (1946 – ) Businessman, US President.
Bill Gates (1955 – ) American businessman, founder of Microsoft
Muhammad Ali (1942 – 2016) American Boxer and civil rights campaigner
Mahatma Gandhi (1869 – 1948) Leader of Indian independence movement
Margaret Thatcher (1925 – 2013) British Prime Minister 1979 – 1990
Mother Teresa (1910 – 1997) Macedonian Catholic missionary nun
Christopher Columbus (1451 – 1506) Italian explorer
Charles Darwin (1809 – 1882) British scientist, theory of evolution
Elvis Presley (1935 – 1977) American musician
Albert Einstein (1879 – 1955) German scientist, theory of relativity
Paul McCartney (1942 – ) British musician, member of Beatles
Queen Victoria ( 1819 – 1901) British monarch 1837 – 1901
Pope Francis (1936 – ) First pope from the Americas
'''


# Function to check if a name is in the list
def check_famous_individual(name):
    # Normalize the famous_list and name to handle case insensitivity
    name_normalized = name.lower()
    famous_list_normalized = famous_list.lower()

    # Check if the individual's name is in the list
    if name_normalized in famous_list_normalized:
        print(f"Yup, {name.title()} did make the Top 20 cut!")
    else:
        print(f"Sorry, {name.title()} did not make the Top 20 cut!")


# Take input from the user
famous_person = input("Please Enter the name of the famous individual: ")

# Check if the person is in the list
check_famous_individual(famous_person)
```

### Explanation:

1. famous_list_normalized: Both the list and input are converted to lowercase lower() to make the comparison
   case-insensitive.
2. Then the program checks if the normalized input name exists within the normalized famous list string.
3. Based on the check, the program prints whether the person is in the list or not.
4. Although the checks are done in lower case, when printing it out, I made the names proper case.

### Sample Console Output:

```
Please Enter the name of the famous individual: Albert Einstein
Yup, Albert Einstein did make the Top 20 cut!

Please Enter the name of the famous individual: leonardo Da vinci
Sorry, Leonardo Da Vinci did not make the Top 20 cut!
```

You can run the above code in Question 7.py file
