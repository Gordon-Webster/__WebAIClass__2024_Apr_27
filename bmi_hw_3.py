from dataclasses import dataclass

@dataclass
class BMI:
    name: str
    weight: float
    height: float

    @property
    def bmi(self):
        return round(self.weight / (self.height/100) ** 2, 1)
    
    def weight_status(self, data):
        if data < 18.5:
            return 'Underweight'
        elif 18.5 <= data < 24:
            return 'Healthy Weight'
        elif 24 <= data < 27:
            return 'Overweight'
        elif 27 <= data < 30:
            return 'Obesity class I'
        elif 30 <= data < 35:
            return 'Obesity class II'
        else:
            return 'Obesity class III'


def main():
    p1 = get_BMI()
    print(f'Hello {p1.name}, BMI: {p1.bmi}, Weight Status: {p1.weight_status(p1.bmi)}')

def get_BMI(): 
    name = input('Enter Name: ').strip()
    weight = (input('Enter Weight(kg): ').strip())
    height = (input('Enter Height(cm): ').strip())
    #error checking for input
    if not name:
        raise ValueError('Missing Name')
    if not weight.isdigit() or not height.isdigit():
        raise ValueError('Invalid Value Entry')
    return BMI(name=name, height=float(height), weight=float(weight))

if __name__ == '__main__':
    main()