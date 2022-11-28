from time import asctime

#1
print(asctime())

#2
#imperial_or_metric, weight, growth = [int(input()) for i in range(3)]

#if imperial_or_metric:
#	print(weight/(growth/100)**2)
#else:
#	print((weight/(growth/100)**2)*703)

#3
#celsius = float(input())

#print(f'фаренгейт: {(celsius*9/5) + 32}')
#print(f'кельвины: {celsius + 273.15}')

#4
#kPa = float(input())

#print(f'PSI: {kPa/6.895}')
#print(f'mm rt st: {kPa*7.501}')

#5
#a = int(input())
#print(sum([int(i) for i in str(a)]))

#6
#arr = [int(input()) for i in range(3)]
#[print(i) for i in sorted(arr)]
#min_ = min(arr)
#max_= max(arr)
#last = sum(arr) - min_ - max_

#7
#hleb = int(input())
#hleb_price = 3.49
#hleb_discont_price = hleb_price - hleb_price*0.6
#print(f'{hleb_price}\n{round(hleb_discont_price,2)}\n{round(hleb_discont_price*hleb,2)}')

#8
#a = int(input())

#if a % 2 == 0:
#	print('четное')
#else:
#	print('нечетное')

#9
#human_age = int(input())
#dog_age = 0
#if human_age > 0:
#	for i in range(human_age):
#		if i < 2:
#			dog_age += 10.5
#		else:
#			dog_age += 4
#else:
#	print('ошибка')
#print(dog_age)

#10
word = input()
if word in ('a','e','i','o','u'):
	print('гласная')
elif word == 'y':
	print('гласная или согласная')
else:
	print('согласная')
