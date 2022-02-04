#1 funktion der tager et argument (string) der skrives til brugeren.
#Returnerer en værdi brugerens input (number_as_string)
def get_number(string):
    number_as_string = input(string)
    return number_as_string

#2 Kalder get_number funktionen, laver string til float, returnerer værdi (height) som nu er float.
#Hvis fejl kaldes funktionen igen med (except: ... return get_height)
def get_height():
    try:
        height = get_number("Enter height (m)")
        height = float(height)
        return height
    except:
        print("Please enter a floating point number")
        return get_height()

#2 Kalder get_number funktionen som forrige
def get_weight():
    try:
        weight = get_number("Enter weight (kg)")
        weight = float(weight)
        return weight
    except:
        print("Please enter a floating point number")
        return get_weight()

#3 Kalder get_height og get_weight, gemmer værdier i variabler (height, weight)
def bmi_calculator():
    height = get_height()
    weight = get_weight()
    bmi = weight / (height**2)
    print(bmi)

#4 Funktionen kaldes
bmi_calculator()