import math

def format_tau():
    tau = 2 * math.pi
    half_tau = math.pi

    formatted_string = f"The value of Tau is {tau:^8.6f}, which is two times {half_tau:^8.6f}."

    print(formatted_string)

format_tau()
