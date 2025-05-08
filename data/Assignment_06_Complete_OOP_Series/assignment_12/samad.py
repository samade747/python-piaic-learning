# Static Methods
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
# that returns the Fahrenheit value.



# TemperatureConverter class define kiya
class TemperatureConverter():

    @staticmethod
    def celsius_to_fehreheit(c):
        # formula celsius se fahrenheit ka
        # (C * 9/5) + 32 = F
        return (c * 9/5) + 32
    

temp_c = 25 # Celsius value


# Static method ko class se call kiya farenheit value ke liye
temp_f = TemperatureConverter.celsius_to_fehreheit(temp_c)

print(f"{temp_c}°C = {temp_f}°F") # Output: 25°C = 77.0°F


