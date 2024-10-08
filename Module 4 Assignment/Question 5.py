def elapsedTime(v, u, a):
    t = (v - u) / a
    return round(t, 1)

initial_velocity = 0  # The ball starts at rest
final_velocity = 31.6  # From the previous calculation
acceleration = 9.8  # Standard gravity in m/s²

time = elapsedTime(final_velocity, initial_velocity, acceleration)
print(f"The elapsed time from when the ball is dropped till it hits the ground is {time} seconds")