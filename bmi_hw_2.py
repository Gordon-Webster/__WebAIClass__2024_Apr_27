# class BMI:
#     def __init__(self) -> None:
#         self.name = input('Enter Name: ').strip()
#         self.weight = float(input('Enter Weight(kg): ').strip())
#         self.height = float(input('Enter Height(cm): ').strip())

#     def __str__(self) -> str:
#         return f'Hello {self.name}, Your BMI:{self.bmi}, Weight status:{self.weight_status(self.bmi)}'
    
#     @property
#     def bmi(self):
#         return round(self.weight / (self.height/100) ** 2, 1)
    
#     def weight_status(self, data):
#         if data < 18.5:
#             return 'Underweight'
#         elif 18.5 <= data < 24:
#             return 'Healthy Weight'
#         elif 24 <= data < 27:
#             return 'Overweight'
#         elif 27 <= data < 30:
#             return 'Obesity class I'
#         elif 30 <= data < 35:
#             return 'Obesity class II'
#         else:
#             return 'Obesity class III'




# p1 = BMI()
# print(p1)


class BMI:
    def __init__(self,name, weight, height) -> None:
        if not name:
            raise ValueError('Missing Name')
        if not weight.isdigit() or not height.isdigit():
            raise ValueError('Invalid Value Entry')
        else:
            self._name = name
            self._weight = float(weight)
            self._height = float(height)

    def __str__(self) -> str:
        return f'Hello {self.name}, Your BMI:{self.bmi}, Weight status:{self.weight_status(self.bmi)}'
    
    #add error checking
    @property
    def name(self):
        return self._name
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError('Missing Name')
    #     self._name = name

    @property
    def weight(self):
        return self._weight
    # @weight.setter
    # def weight(self, weight):
    #     if not isdigit(weight):
    #         raise ValueError('Invalid Value')
          
    #     self._weight = weight

    @property
    def height(self):
        return self._height
    # @height.setter
    # def height(self, height):
        # if not name:
            # raise ValueError('Missing Name')
        # self._height = height

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
    print(p1)

def get_BMI(): 
    name = input('Enter Name: ').strip()
    weight = (input('Enter Weight(kg): ').strip())
    height = (input('Enter Height(cm): ').strip())
    return BMI(name, weight, height)

if __name__ == '__main__':
    main()
