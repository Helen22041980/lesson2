# a=input("введите значение: ")
# while not a.isdigit():
#     a = input("введите повторно: ")
#
#
# while not (a := input("введите значение:")).isdigit(): ...
# print(a)

# a=input("введите значение: ")
# max_nam = max(a)
# print(a)
# print(max_nam)

# coins=(25,10,5,1)
# money= int(input())
# coins_total=0
# for coin in coins:
#     coins_total +=money //coin
#     money-=(money//coin)*coin
# print(coins_total)

money= int(input())
proc= int(input())
money2=money*2
year=0
while money < money2:
    year+=1
    depozit *=1+proc
print(year)


