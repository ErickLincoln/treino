#A fórmula de conversão é F ← C * 9 / 5 + 32
# sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

celcius = float(input('Digite a temperatura: '))
conversao = float(celcius) *9/5+32
fahrenheit = conversao

print(int(celcius), 'ºC')
print(int(fahrenheit) , 'ºF')