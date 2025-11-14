#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:

class ConversorTemperatura:

    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 1.8) + 32
    
# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:

conversor = ConversorTemperatura(celsius)

fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)