import math

def math_module_demo():
    print("------ Math Module Functions Demo ------\n")

    # Constants
    print("Math Constants:")
    print("PI:", math.pi)
    print("Euler's number (e):", math.e)
    print("Infinity:", math.inf)
    print()

    # Basic functions
    print("Basic Functions:")
    print("Absolute value of -15:", math.fabs(-15))
    print("Factorial of 5:", math.factorial(5))
    print("Square root of 16:", math.sqrt(16))
    print()

    # Trigonometric functions
    print("Trigonometric Functions:")
    angle = math.radians(30)  # converting degrees to radians
    print("sin(30°):", math.sin(angle))
    print("cos(30°):", math.cos(angle))
    print("tan(30°):", math.tan(angle))
    print()

    # Logarithmic functions
    print("Logarithmic Functions:")
    print("Natural log of 10:", math.log(10))
    print("Base-10 log of 1000:", math.log10(1000))
    print("Base-2 log of 8:", math.log2(8))
    print()

    # Power functions
    print("Power Functions:")
    print("2 raised to 5:", math.pow(2, 5))
    print("10^3:", math.exp(3))
    print()

    # Rounding and flooring
    print("Rounding and Flooring:")
    print("Floor of 3.7:", math.floor(3.7))
    print("Ceil of 3.2:", math.ceil(3.2))
    print("Truncate 3.9:", math.trunc(3.9))
    print()

    # Greatest Common Divisor & LCM
    print("GCD and LCM:")
    print("GCD of 54 and 24:", math.gcd(54, 24))
    print("LCM of 4 and 6:", math.lcm(4, 6))
    print()

    print("------ End of Demo ------")

# Run the demo
math_module_demo()
