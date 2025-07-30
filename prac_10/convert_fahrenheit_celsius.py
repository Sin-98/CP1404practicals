from flask import Flask

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

@app.route('/')
def home():
    return "Welcome! Try adding /f/100.2 to convert Celsius to Fahrenheit."

@app.route('/f/<celsius_str>')
def convert_temperature(celsius_str):
    try:
        celsius = float(celsius_str)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f"{celsius:.2f}°C is {fahrenheit:.2f}°F"
    except ValueError:
        return f"Invalid input: '{celsius_str}' is not a valid number."

if __name__ == '__main__':
    app.run()
