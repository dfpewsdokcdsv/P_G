import random

password =''
length = int(input('Введите длину пароля'))
for i in range(length):
    password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

print(password)
