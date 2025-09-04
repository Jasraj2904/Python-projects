import math

# Function to calculate sin, cos, and tan
def calculate_trig(angle_degrees):
    # Convert degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate sin, cos, and tan
    sin_val = math.sin(angle_radians)
    cos_val = math.cos(angle_radians)
    
    try:
        tan_val = math.tan(angle_radians)
    except:
        tan_val = "Undefined"
    
    # Print results
    print(f"Angle: {angle_degrees}°")
    print(f"sin({angle_degrees}) = {sin_val}")
    print(f"cos({angle_degrees}) = {cos_val}")
    print(f"tan({angle_degrees}) = {tan_val}")

# Example usage
angle = float(input("Enter angle in degrees: "))
calculate_trig(angle)
