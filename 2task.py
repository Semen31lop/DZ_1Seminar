#Найдите сумму цифр трехзначного числа.
import random


n = random.randint(99,1000)
s = ((n%10)+(n//100)+((n//10)%10))
print(f'{n} -> {s} ')
