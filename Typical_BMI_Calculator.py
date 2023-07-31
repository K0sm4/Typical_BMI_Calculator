def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_verification(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal weight"
    else:
        return "overweight"

def main():
    try:
        name = input('Enter your name: ')
        weight = float(input('Enter your weight (in kg): '))
        height = float(input('Enter your height (in meters): '))
    except ValueError:
        print('Invalid input. Weight and height must be numbers.')
        return

    bmi = bmi_calculator(weight, height)
    result = bmi_verification(bmi)
    print(name)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {result}")

if __name__ == "__main__":
    main()
