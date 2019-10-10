def celcius_to_fahrenheit(celcius: float) -> float:
    return (9/5) * celcius + 32


def celcius_to_reaumur(celcius: float) -> float:
    return celcius * (4/5)


def celcius_to_kelvin(celcius: float) -> float:
    return celcius + 273


def fahrenheit_to_celcius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * (5/9)


def fahrenheit_to_reaumur(fahrenheit: float) -> float:
    return (fahrenheit - 32) * (4/9)


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return fahrenheit_to_celcius(fahrenheit) + 273


def reaumur_to_celcius(reaumur: float) -> float:
    return reaumur * (5/4)


def reaumur_to_fahrenheit(reaumur: float) -> float:
    return (9/4) * reaumur + 32


def reaumur_to_kelvin(reaumur: float) -> float:
    return reaumur_to_celcius(reaumur) + 273


def kelvin_to_celcius(kelvin: float) -> float:
    return kelvin - 273


def kelvin_to_fahrenheit(kelvin: float) -> float:
    return celcius_to_fahrenheit(kelvin_to_celcius(kelvin))


def kelvin_to_reaumur(kelvin: float) -> float:
    return celcius_to_reaumur(kelvin_to_celcius(kelvin))


def main():
    """
    This class is used to run the program.
    :return:
    """

    print("Enter 'celcius', 'fahrenheit', 'reaumur', or 'kelvin'.")
    units: list = ["celcius", "fahrenheit", "reaumur", "kelvin"]
    first_unit: str = input("What unit do you want to convert from? ")
    second_unit: str = input("What unit do you want to convert to? ")
    while first_unit.lower() not in units or second_unit.lower() not in units or first_unit == second_unit:
        first_unit = input("What unit do you want to convert from? ")
        second_unit = input("What unit do you want to convert to? ")

    input_temp: float = float(input("Please enter temperature in " + str(first_unit) + ": "))
    result_temp: float = globals()[str(first_unit).lower() + "_to_" + str(second_unit).lower()](input_temp)
    print(str(input_temp) + " degrees in " + str(first_unit).capitalize() + " is equal to "
          + str(result_temp) + " degrees in " + str(second_unit).capitalize())


main()
