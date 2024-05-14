def main():
    try:
        name = input('Name: ')
        height = int(input('Height(cm): '))
        weight = int(input('Weight(kg): '))
    except:
        print('Error Entry again')
    else:
        weight_status(name, round(weight / (height/100) ** 2, 1))

def weight_status(name, data):
    if data < 18.5:
        print(f'Hello {name}:\nYour BMI is: {data}\nWeight Status: Underweight')
    elif 18.5 <= data < 24:
        print(f'Hello {name}:\nYour BMI is: {data}\nWeight Status: Healthy Weight')
    elif 24 <= data < 27:
        print(f'Hello {name}:\nYour BMI is: {data}\nWeight Status: Overweight')
    elif 27 <= data < 30:
        print(f'Hello {name}:\nYour BMI is: {data}\nWeight Status: Obesity class I')
    elif 30 <= data < 35:
        print(f'Hello {name}:\nYour BMI is: {data}\nWeight Status: Obesity class II')
    else:
        print(f'Hello {name}:\nYour BMI is: {data}\nWeight Status: Obesity class III')

main()