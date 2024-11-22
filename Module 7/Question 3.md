#### Question 3

```
Gases consist of atoms or molecules that move at different speeds in random directions. The root mean square velocity (
RMS velocity) is a way to find a single velocity value for the particles. The average velocity of gas particles is found
using the root mean square velocity formula:

μrms = (3RT/M)½ root mean square velocity in m/sec

R = ideal gas constant = 8.3145 (kg·m2/sec2)/K·mol

T = absolute temperature in Kelvin

M = mass of a mole of the gas in kilograms. molar mass of O2 = 3.2 x 10-2 kg/mol

T = °C + 273

a. By using the decimal module, create a decimal object and apply the sqrt and quantize method (match pattern “1.000”)
and provide the answer to the question:  What is the average velocity or root mean square velocity of a molecule in a
sample of oxygen at 25 degrees Celsius?Here's a brief explanation of the core functionality:
```

• Main Purpose:

- Calculates root mean square velocity (RMS) of oxygen molecules at a given temperature

• Key Constants Used:

- R = 8.3145 (Gas constant)
- M = 3.2E-2 (Molar mass of O2)
- Temperature conversion: Kelvin = Celsius + 273

• Core Formula:

- μrms = √(3RT/M)
- Uses Decimal module for precise calculations
- Results formatted to 3 decimal places

• Program Flow:

1. Get temperature input in Celsius
2. Convert to Kelvin
3. Apply RMS formula
4. Format and display result
5. Repeat until 'x' entered

• Example Calculation:

- Input: 25°C
- Converts to: 298.15 K (by adding 273 to the Celsius value)
- Result: 482.515 m/sec (velocity) (by applying the RMS formula)
