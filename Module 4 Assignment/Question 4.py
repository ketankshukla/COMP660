import math

def velocityFinal(vo, a, d):
    v_squared = vo**2 + 2*a*d
    v = math.sqrt(v_squared)
    return round(v, 1)

final_velocity = velocityFinal(0, 9.8, 51)

print(f"The final velocity is {final_velocity} m/s.")