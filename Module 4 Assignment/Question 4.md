### Answers to the Third Equation of Motion:

The third equation of motion is given as:

v² = v₀² + 2ad

Where:
- v is the final velocity
- v₀ is the initial velocity
- a is the acceleration
- d is the distance traveled

### a. Function to Calculate Final Velocity

### Question
Using the equation above, build a function called (velocityFinal) 
which returns the final velocity of the object rounded to one 
decimal place. Use the following parameters

- vo (initial velocity)
- a (uniform acceleration)
- d (distance traveled)

### Answer

Here's the function that calculates the final velocity using 
the third equation of motion:

```python
import math

def velocityFinal(vo, a, d):
    v_squared = vo**2 + 2*a*d
    v = math.sqrt(v_squared)
    return round(v, 1)
```

This function:
1. Takes `vo` (initial velocity), `a` (acceleration), and `d` (distance) as parameters.
2. Calculates v² using the equation.
3. Takes the square root to get v.
4. Rounds the result to one decimal place and returns it.

### b. Calling Expression for Dropping Ball

### Question
A ball is gently dropped from a height of 51m (167 ft), the acceleration 
due to gravity is a constant 9.8 m/s2. 
Using the arguments described and function you built above, 
what is the calling expression to determine the final velocity 
before impact?

### Answer
For a ball dropped from a height of 51m with acceleration due to gravity 
of 9.8 m/s², the calling expression would be:

```python
final_velocity = velocityFinal(0, 9.8, 51)
```

Explanation:
- Initial velocity (vo) is 0 m/s as the ball is dropped.
- Acceleration (a) is 9.8 m/s².
- Distance (d) is 51 m (the height from which the ball is dropped).

### c. Calculated Speed Before Impact

### Question
Based on the function you created , calculate the speed of the 
ball before it strikes the ground ? Answer should be in m/s 
(Feel free to use the figure above to check your answer).

### Answer
Let's calculate the speed of the ball before it strikes the ground:

```python
final_velocity = velocityFinal(0, 9.8, 51)
print(f"The speed of the ball before impact is {final_velocity} m/s")
```

Output:
```
The speed of the ball before impact is 31.6 m/s
```

Therefore, the ball will be traveling at approximately 31.6 m/s 
just before it strikes the ground.
