"""
Famous People Checker Module

This module provides functionality to check if a given person's name appears in a predefined
list of 20 famous individuals from history. It includes data validation, name normalization,
and case-insensitive matching.

Author: [Your Name]
Date: [Current Date]
"""

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

def check_famous_individual(name):
    """
    Check if a given name appears in the list of famous individuals.
    
    This function performs the following operations:
    1. Validates the input name for emptiness and numeric characters
    2. Normalizes the name by removing special characters and extra whitespace
    3. Performs a case-insensitive search in the famous_list
    
    Args:
        name (str): The name of the person to check
        
    Returns:
        str: A message indicating whether the person is in the Top 20 list
        
    Raises:
        ValueError: If the name is empty, contains only whitespace, contains numbers,
                  or contains no valid characters after cleaning
    """
    # Input validation
    if not name or name.isspace():
        raise ValueError("Name cannot be empty or just whitespace")
    
    if any(char.isdigit() for char in name):
        raise ValueError("Name should not contain numbers")
    
    # Remove extra whitespace and special characters, keeping only letters and spaces
    name = ''.join(char for char in name if char.isalpha() or char.isspace())
    name = ' '.join(name.split())  # Normalize whitespace
    
    if not name:  # Check if name is empty after cleaning
        raise ValueError("Name contains no valid characters")
    
    name_normalized = name.lower()
    famous_list_normalized = famous_list.lower()

    if name_normalized in famous_list_normalized:
        return f"Yup, {name.title()} did make the Top 20 cut!"
    else:
        return f"Sorry, {name.title()} did not make the Top 20 cut!"

# Main program loop
"""
Main execution block that:
1. Continuously prompts for user input
2. Processes the input using check_famous_individual()
3. Handles various exceptions that might occur
4. Provides a way to exit the program
"""
while True:
    try:
        famous_person = input("\nPlease enter the name of the famous individual (or 'quit' to exit): ")
        
        if famous_person.lower() == 'quit':
            print("Thank you for using the Famous People Checker!")
            break
            
        result = check_famous_individual(famous_person)
        print(result)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
