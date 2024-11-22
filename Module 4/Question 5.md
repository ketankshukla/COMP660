### Elapsed Time Calculation for Falling Object

### Question
Final velocity (v) of an object equals initial velocity (u) of that 
object plus acceleration (a) of the object times the elapsed time (t) 
from u to v.

a. Create a function which returns the elapsed time using the 
arguments v, u, and a. Calculate the elapsed time from when the ball 
is dropped till it hits the ground (1 decimal place)? 
Use standard gravity as 9.8 m/s2 
(Feel free to use the figures above to check your answer).

### Answer

The equation for final velocity in terms of initial velocity, 
acceleration, and time is:

v = u + at

Where:
- v is the final velocity
- u is the initial velocity
- a is the acceleration
- t is the elapsed time

## a. Function to calculate elapsed time

Here's the function that calculates the elapsed time using the 
equation above:

```python
def elapsedTime(v, u, a):
    t = (v - u) / a
    return round(t, 1)
```

This function:
1. Takes `v` (final velocity), `u` (initial velocity), and `a` (acceleration) as parameters.
2. Calculates t using the rearranged equation: `t = (v - u) / a`
3. Rounds the result to one decimal place and returns it.

### Calculating elapsed time for the falling ball

Now we can use this function to calculate the elapsed time for the ball 
dropped from a height of 51m. 
We'll use the final velocity we calculated in the previous 
problem (31.6 m/s).

```python
initial_velocity = 0  # The ball starts at rest
final_velocity = 31.6  # From the previous calculation
acceleration = 9.8  # Standard gravity in m/s²

time = elapsedTime(final_velocity, initial_velocity, acceleration)
print(f"The elapsed time from when the ball is dropped till it hits the ground is {time} seconds")
```

Output:
```
The elapsed time from when the ball is dropped till it 
hits the ground is 3.2 seconds
```

Therefore, it takes approximately 3.2 seconds for the ball to fall from
a height of 51m to the ground.

### Verification

We can verify this result using the equation for displacement 
in free fall:

d = (1/2) * a * t²

Where d is 51m and a is 9.8 m/s².

Plugging in our calculated time:

- 51 ≈ (1/2) * 9.8 * 3.2 * 3.2
- 51 ≈ 50.176

The slight difference is due to rounding in our calculations, 
but this confirms that our elapsed time calculation is correct.
