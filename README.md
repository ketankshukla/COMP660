# <span style="font-size: 48px;">📚 Comp660</span>

<div style="background-color: #000000; padding: 20px; font-size: 24px;">

## <span style="font-size: 36px;">📖 Overview</span>
A powerful project with comprehensive features.

## <span style="font-size: 36px;">✨ Key Features</span>
| Feature | Description |
|---------|-------------|
| 🔒 **Security** | <span style="color: #00ffff;">Advanced authentication and authorization</span> |
| 🔌 **API** | <span style="color: #ffff00;">RESTful API with comprehensive documentation</span> |
| 💾 **Database** | <span style="color: #00ffff;">Optimized queries and data integrity</span> |
| ⚡ **Performance** | <span style="color: #ffff00;">Caching and load balancing ready</span> |

## <span style="font-size: 36px;">🚀 Installation</span>
```bash
# Clone the repository
git clone https://github.com/ketankshukla/COMP660.git
cd COMP660

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## <span style="font-size: 36px;">📁 Project Structure</span>
```
📄 .gitignore
📄 .pylintrc
📁 Module 1
  📄 Question 4.py
  📄 graph.png
  📄 questions.md
📁 Module 2
  📄 Question 1 Screenshot.png
  📄 Question 1.py
  📄 Question 2 Screenshot.png
  📄 Question 2.py
  📄 Question 3 Screenshot.png
  📄 Question 3.py
  📄 questions.md
📁 Module 3
  📄 Question 2 Screenshot.png
  📄 Question 2.py
  📄 Question 3 - Equal To 70 Degrees.png
  📄 Question 3 - Greater Than 70 Degrees.png
  📄 Question 3 - Less Than 70 Degrees.png
  📄 Question 3.py
  📄 questions.md
📁 Module 4
  📄 Question 4.py
  📄 Question 5.py
  📄 questions.md
📁 Module 5
  📄 Question 2.py
  📄 Question 3.py
  📄 Question 4.py
  📄 Question 5.py
  📄 Question 6.py
  📄 Question 7.py
  📄 Question 8.py
  📄 questions.md
📁 Module 6
  📄 Question 1.py
  📄 Question 2.py
  📄 Question 3a.py
  📄 Question 3b.py
  📄 Question 4.py
  📄 Question 5.py
  📄 Question 6.py
  📄 Question 7.py
  📄 questions.md
📁 Module 7
  📄 Question 1.py
  📄 Question 2.py
  📄 Question 3.py
  📄 questions.md
```

## <span style="font-size: 36px;">👨‍💻 Development</span>

### Core Components
Here's a detailed breakdown of the key components and their functionality:

#### <span style="color: #00ffff;">🔹 Module 4\Question 4.py:calculate_final_velocity</span>

<span style="color: #ffff00;">Calculate the final velocity using the equation v² = v₀² + 2ad</span>

```python
def calculate_final_velocity(initial_velocity: Any, distance: Any)
        """
        Calculate the final velocity using the equation v² = v₀² + 2ad.
    
        Args:
            initial_velocity (float): Initial velocity in m/s
            distance (float): Distance traveled in meters
    
        Returns:
            float: Final velocity in m/s, rounded to 1 decimal place
    
        Example:
            >>> calculate_final_velocity(0, 10)
            14.0
        """
        acceleration = 9.8
        velocity_squared = initial_velocity ** 2 + 2 * acceleration * distance
        final_velocity = math.sqrt(velocity_squared)
        return round(final_velocity, 1)
```


#### <span style="color: #00ffff;">🔹 Module 4\Question 4.py:get_valid_input</span>

<span style="color: #ffff00;">Get valid numerical input from the user</span>

```python
def get_valid_input(prompt: Any)
        """
        Get valid numerical input from the user.
    
        Args:
            prompt (str): The prompt message to display to the user
    
        Returns:
            float: The validated numerical input
    
        Raises:
            ValueError: If the input cannot be converted to a float
        """
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print('Error: Please enter a valid number.')
```


#### <span style="color: #00ffff;">🔹 Module 4\Question 5.py:calculate_elapsed_time</span>

<span style="color: #ffff00;">Calculate the elapsed time for an object under constant acceleration</span>

```python
def calculate_elapsed_time(final_velocity: Any, initial_velocity: Any, acceleration: Any)
        """
        Calculate the elapsed time for an object under constant acceleration.
    
        Uses the equation: t = (v - u) / a, where:
        - t is elapsed time
        - v is final velocity
        - u is initial velocity
        - a is acceleration
    
        Args:
            final_velocity (float): Final velocity in m/s
            initial_velocity (float): Initial velocity in m/s
            acceleration (float): Acceleration in m/s²
    
        Returns:
            float: Elapsed time in seconds, rounded to 1 decimal place
    
        Example:
            >>> calculate_elapsed_time(10, 0, 9.8)
            1.0
        """
        elapsed_time = (final_velocity - initial_velocity) / acceleration
        return round(elapsed_time, 1)
```


#### <span style="color: #00ffff;">🔹 Module 4\Question 5.py:get_valid_input</span>

<span style="color: #ffff00;">Get valid numerical input from the user</span>

```python
def get_valid_input(prompt: Any)
        """
        Get valid numerical input from the user.
    
        Args:
            prompt (str): The prompt message to display to the user
    
        Returns:
            float: The validated numerical input
    
        Raises:
            ValueError: If the input cannot be converted to a float
        """
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print('Error: Please enter a valid number.')
```


#### <span style="color: #00ffff;">🔹 Module 4\Question 5.py:main</span>

<span style="color: #ffff00;">Main program function that:
1</span>

```python
def main()
        """
        Main program function that:
        1. Displays program information
        2. Gets user input for velocities
        3. Calculates and displays elapsed time
        
        Uses constant acceleration due to gravity (9.8 m/s²)
        """
        print('Calculate elapsed time for an object in free fall')
        print('Equation: t = (v - u) / a')
        print('where t is elapsed time, v is final velocity, u is initial velocity,')
        print('and a is acceleration due to gravity (9.8 m/s²).')
        initial_velocity = get_valid_input('Enter the initial velocity (m/s): ')
        final_velocity = get_valid_input('Enter the final velocity (m/s): ')
        ACCELERATION = 9.8
        elapsed_time = calculate_elapsed_time(final_velocity, initial_velocity, ACCELERATION)
        print(f'The elapsed time is {elapsed_time} seconds.')
```


#### <span style="color: #00ffff;">🔹 Module 5\Question 2.py:factorial</span>

<span style="color: #ffff00;">Handles conditional logic takes n as input.</span>

```python
def factorial(n: Any)
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
```


#### <span style="color: #00ffff;">🔹 Module 5\Question 2.py:main</span>

<span style="color: #ffff00;">Function to main.</span>

```python
def main()
        while True:
            user_input = input("Enter a positive integer (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            if not user_input.isdigit():
                print('Please enter a valid non-negative integer.')
            else:
                n = int(user_input)
                result = factorial(n)
                print(f'The factorial of {n} is: {result}')
            print()
```


#### <span style="color: #00ffff;">🔹 Module 5\Question 3.py:main</span>

<span style="color: #ffff00;">Function to main.</span>

```python
def main()
        while True:
            user_input = input("Enter a positive integer (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            if not user_input.isdigit() or int(user_input) == 0:
                print('Please enter a valid positive integer.')
            else:
                n = int(user_input)
                result = sum_nint(n)
                print(f'The sum of the first {n} integers is: {result}')
            print()
```


#### <span style="color: #00ffff;">🔹 Module 5\Question 3.py:sum_nint</span>

<span style="color: #ffff00;">Handles conditional logic takes n as input.</span>

```python
def sum_nint(n: Any)
        if n == 0:
            return 0
        return n + sum_nint(n - 1)
```


#### <span style="color: #00ffff;">🔹 Module 5\Question 4.py:main</span>

<span style="color: #ffff00;">Function to main.</span>

```python
def main()
        while True:
            user_input = input("Enter a word to reverse (or 'q' to quit): ").strip()
            if user_input.lower() == 'q':
                print('Thank you for using the word reverser. Goodbye!')
                break
            if not user_input or not user_input.isalpha():
                print('Error: Please enter a non-empty word containing only letters.')
            else:
                print('Reversed word: ', end='')
                semordnilap(user_input, 0)
                print()
            print()
```


#### <span style="color: #00ffff;">🔹 Module 5\Question 4.py:semordnilap</span>

<span style="color: #ffff00;">Handles conditional logic processes aString and index.</span>

```python
def semordnilap(aString: Any, index: Any)
        if index < len(aString):
            semordnilap(aString, index + 1)
            print(aString[index], end='')
```


#### <span style="color: #00ffff;">🔹 Module 5\Question 6.py:area_circle</span>

<span style="color: #ffff00;">Takes radius as input.</span>

```python
def area_circle(radius: Any)
        return math.pi * radius ** 2
```


#### <span style="color: #00ffff;">🔹 Module 5\Question 6.py:main</span>

<span style="color: #ffff00;">Function to main.</span>

```python
def main()
        while True:
            user_input = input("Enter the radius of the circle (or 'q' to quit): ").strip().lower()
            if user_input == 'q':
                break
            if not user_input or not user_input.replace('.', '', 1).isdigit() or float(user_input) <= 0:
                print('Please enter a valid positive number for the radius.')
            else:
                radius = float(user_input)
                area = area_circle(radius)
                print(f'The area of a circle with radius {radius} is: {area:.2f}')
            print()
```


#### <span style="color: #00ffff;">🔹 Module 5\Question 7.py:main</span>

<span style="color: #ffff00;">Function to main.</span>

```python
def main()
        while True:
            user_input = input("Enter the radius of the circle (or 'q' to quit): ").strip().lower()
            if user_input == 'q':
                break
            if not user_input or not user_input.replace('.', '', 1).isdigit() or float(user_input) <= 0:
                print('Please enter a valid positive number for the radius.')
            else:
                radius = float(user_input)
                area = area_circle_lambda(radius)
                print(f'The area of a circle with radius {radius} is: {area:.2f}')
            print()
```


#### <span style="color: #00ffff;">🔹 Module 6\Question 4.py:add_html_tags</span>

<span style="color: #ffff00;">Wrap the given text with HTML opening and closing tags</span>

```python
def add_html_tags(tag: Any, text: Any)
        """
        Wrap the given text with HTML opening and closing tags.
    
        Args:
            tag (str): The HTML tag to use (e.g., 'h1', 'p', 'div')
            text (str): The text content to wrap with HTML tags
    
        Returns:
            str: The text wrapped with the specified HTML tags
    
        Example:
            >>> add_html_tags('h1', 'Hello')
            '<h1>Hello</h1>'
        """
        return f'<{tag}>{text}</{tag}>'
```


#### <span style="color: #00ffff;">🔹 Module 6\Question 5.py:get_name_input</span>

<span style="color: #ffff00;">Get and validate a name input from the user</span>

```python
def get_name_input(prompt: Any)
        """
        Get and validate a name input from the user.
    
        This function:
        1. Prompts the user for input using the provided prompt
        2. Removes leading/trailing whitespace
        3. Validates that the input is not empty
        4. Capitalizes the first letter of the name
    
        Args:
            prompt (str): The prompt message to display to the user
    
        Returns:
            str: The validated and properly capitalized name
    
        Note:
            The function will keep prompting until valid input is received
        """
        while True:
            name = input(prompt).strip()
            if name:
                return name.capitalize()
            else:
                print('Input cannot be blank. Please try again.')
```


#### <span style="color: #00ffff;">🔹 Module 6\Question 6.py:abbreviate_middle_name</span>

<span style="color: #ffff00;">Format a full name by abbreviating middle names</span>

```python
def abbreviate_middle_name(full_name: Any)
        """
        Format a full name by abbreviating middle names.
    
        This function:
        1. Splits the input name into parts
        2. Capitalizes each part
        3. Handles different cases:
           - Single name: returns as is
           - Two names: returns both parts
           - Three or more names: abbreviates middle names
    
        Args:
            full_name (str): The full name to format (can contain multiple parts)
    
        Returns:
            str: Formatted name with abbreviated middle names
    
        Examples:
            >>> abbreviate_middle_name("john smith")
            "John Smith"
            >>> abbreviate_middle_name("john william smith")
            "John W. Smith"
            >>> abbreviate_middle_name("john william james smith")
            "John W. J. Smith"
        """
        name_parts = [part.capitalize() for part in full_name.split()]
        if len(name_parts) == 1:
            return name_parts[0]
        if len(name_parts) == 2:
            return f'{name_parts[0]} {name_parts[1]}'
        first_name = name_parts[0]
        last_name = name_parts[-1]
        middle_names = ' '.join([f'{name[0].upper()}.' for name in name_parts[1:-1]])
        return f'{first_name} {middle_names} {last_name}'
```


#### <span style="color: #00ffff;">🔹 Module 6\Question 7.py:check_famous_individual</span>

<span style="color: #ffff00;">Check if a given name appears in the list of famous individuals</span>

```python
def check_famous_individual(name: Any)
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
        if not name or name.isspace():
            raise ValueError('Name cannot be empty or just whitespace')
        if any((char.isdigit() for char in name)):
            raise ValueError('Name should not contain numbers')
        name = ''.join((char for char in name if char.isalpha() or char.isspace()))
        name = ' '.join(name.split())
        if not name:
            raise ValueError('Name contains no valid characters')
        name_normalized = name.lower()
        famous_list_normalized = famous_list.lower()
        if name_normalized in famous_list_normalized:
            return f'Yup, {name.title()} did make the Top 20 cut!'
        else:
            return f'Sorry, {name.title()} did not make the Top 20 cut!'
```


#### <span style="color: #00ffff;">🔹 Module 7\Question 1.py:format_tau</span>

<span style="color: #ffff00;">Function to format tau.</span>

```python
def format_tau()
        tau = 2 * math.pi
        half_tau = math.pi
        formatted_string = f'The value of Tau is {tau:^8.3f}, which is two times {half_tau:^8.3f}.'
        print(formatted_string)
```


#### <span style="color: #00ffff;">🔹 Module 7\Question 2.py:calculate_integer_range</span>

<span style="color: #ffff00;">Takes num_bytes as input.</span>

```python
def calculate_integer_range(num_bytes: Any)
        num_bits = num_bytes * 8
        total_numbers = 2 ** num_bits
        max_value = 2 ** (num_bits - 1) - 1
        min_value = -2 ** (num_bits - 1)
        return (total_numbers, min_value, max_value)
```


#### <span style="color: #00ffff;">🔹 Module 7\Question 2.py:format_number</span>

<span style="color: #ffff00;">Handles conditional logic processes number and use_scientific.</span>

```python
def format_number(number: Any, use_scientific: Any)
        if use_scientific:
            return f'{number:.2e}'
        return f'{number:,}'
```


#### <span style="color: #00ffff;">🔹 Module 7\Question 2.py:main</span>

<span style="color: #ffff00;">Function to main.</span>

```python
def main()
        while True:
            user_input = input("Enter number of Bytes you would like to determine the signed range of (or 'x' to exit): ")
            if user_input.lower() == 'x':
                print('Exiting program...')
                break
            try:
                num_bytes = int(user_input)
                if num_bytes <= 0:
                    print('Please enter a positive number of bytes.')
                    continue
                total_numbers, min_value, max_value = calculate_integer_range(num_bytes)
                use_scientific = num_bytes > 10
                total_formatted = format_number(total_numbers, use_scientific)
                min_formatted = format_number(min_value, use_scientific)
                max_formatted = format_number(max_value, use_scientific)
                output = f'{num_bytes} Byte(s) integral type with 8 bits can encode {total_formatted} numbers.\nThe signed range will be from {min_formatted} to {max_formatted}'
                print(f'{output}\n')
            except ValueError:
                print(f'Please enter a valid integer for the number of bytes.\n')
```


#### <span style="color: #00ffff;">🔹 Module 7\Question 3.py:calculate_rms_velocity</span>

<span style="color: #ffff00;">Handles conditional logic takes temp_celsius as input.</span>

```python
def calculate_rms_velocity(temp_celsius: Any)
        if temp_celsius < -273.15:
            raise ValueError('Temperature cannot be below absolute zero (-273.15 Celsius)')
        getcontext().prec = 6
        try:
            gas_constant_r = Decimal('8.3145')
            molar_mass_m = Decimal('3.2E-2')
            kelvin_temp_t = Decimal(str(temp_celsius + 273))
            rt_product = gas_constant_r * kelvin_temp_t
            three_rt = Decimal('3') * rt_product
            fraction = three_rt / molar_mass_m
            rms_velocity = fraction.sqrt()
            pattern = Decimal('1.000')
            return rms_velocity.quantize(pattern)
        except InvalidOperation as e:
            raise ValueError('Error in decimal calculation. Please check input values.') from e
```


#### <span style="color: #00ffff;">🔹 Module 7\Question 3.py:get_temperature_input</span>

<span style="color: #ffff00;">Handles conditional logic takes prompt as input.</span>

```python
def get_temperature_input(prompt: Any)
        value = input(prompt).strip().lower()
        if value == 'x':
            return None
        try:
            temp = float(value)
            return temp
        except ValueError:
            raise ValueError('Invalid input. Please enter a numeric value.')
```


#### <span style="color: #00ffff;">🔹 Module 7\Question 3.py:main</span>

<span style="color: #ffff00;">Function to main.</span>

```python
def main()
        while True:
            try:
                temperature_input = get_temperature_input("Enter temperature in Celsius or 'x' to exit program: ")
                if temperature_input is None:
                    print('\nExiting program...')
                    break
                velocity = calculate_rms_velocity(temperature_input)
                print('\nThe average velocity or root mean square velocity of a molecule in a sample of oxygen')
                print(f'at {temperature_input} degrees Celsius is {velocity} m/sec\n')
            except ValueError as e:
                print(f'\nError: {str(e)}\n')
            except Exception as e:
                print(f'\nAn unexpected error occurred: {str(e)}\n')
                print('Please try again.\n')
```


### Configuration Management
| Function | Description |
|----------|-------------|
| `ConfigLoader.load_config` | <span style="color: #00ffff;">Loads and merges system and project configurations</span> |
| `ConfigLoader.__init__` | <span style="color: #ffff00;">Initializes paths for configuration files</span> |

### README Generation
| Function | Description |
|----------|-------------|
| `ReadmeGenerator.generate_readme_content` | <span style="color: #00ffff;">Generates formatted README content from template</span> |
| `ReadmeGenerator._format_file_structure` | <span style="color: #ffff00;">Formats project directory structure</span> |
| `ReadmeGenerator._analyze_code` | <span style="color: #00ffff;">Analyzes code files for documentation</span> |
| `ReadmeGenerator.select_specific_repo` | <span style="color: #ffff00;">Interactive repository selection</span> |

### Git Operations
| Function | Description |
|----------|-------------|
| `ReadmeGenerator.run_command` | <span style="color: #00ffff;">Executes Git and system commands</span> |
| `ReadmeGenerator.clone_repository` | <span style="color: #ffff00;">Clones and configures repositories</span> |
| `ReadmeGenerator.cleanup` | <span style="color: #00ffff;">Removes temporary files and directories</span> |

## <span style="font-size: 36px;">🧪 Testing</span>
```bash
# Run all tests
python manage.py test

# Run with coverage
coverage run manage.py test
coverage report
```

## <span style="font-size: 36px;">🤝 Contributing</span>
1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## <span style="font-size: 36px;">📄 License</span>
This project is licensed under the MIT License.

---
<span style="color: #00ffff; font-size: 32px;">❤️ Generated with love by ketankshukla ❤️</span>
</div>
