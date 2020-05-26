# 1
a_dec = 10
b_string = "some string"
c_list = ['1', '2', '8']
d_dict = {'one': 1, 'two': 2, 'three': 3}
e_bool = True
f_tupl = ('a', 'b', 'c')

print("Enter number:")
g_ask_user = int(input())
print("Your number is:")
print(g_ask_user)

print("Enter your name:")
g_ask_user_name = input()
print("Your name is:")
print(g_ask_user_name)

# 2
print("Enter miliseconds:")
g_ask_user_sec = int(input())
h = int(g_ask_user_sec // 3600)
m = int((g_ask_user_sec / 60) % 60)
s = g_ask_user_sec % 60
print("Your time is:")
print(f"{h}:{m}:{s}")

# 3
print("Enter number n:")
n = int(input())
summ = n + int((str(n) + str(n))) + int(((str(n) + str(n) + str(n))))
print(f"Summ of n + nn + nnn: {summ}")

# 4
print("Enter number:")
n = int(input())
big_one = 0
while (n != 0):
    maybe_bigger = n % 10
    if maybe_bigger > big_one:
        big_one = maybe_bigger
    n = n // 10
print(f"The bigger number is {big_one}")

# 5
print("Enter Income:")
income = int(input())
print("Enter Outcome:")
outcome = int(input())
if (income > outcome):
    profit = income - outcome
    print("Profitable financial result")
    print(f"Profit is: {profit}")
    print("How many employee:")
    em = int(input())
    profit_per_person = profit // em
    print(f"Profit for employee: {profit_per_person}")
else:
    print("Lost financial result")

# 6
print("Enter first day km:")
day = int(input())
print("Enter result:")
result = int(input())

day_timing = 1
while(day < result):
    day = day + day * 0.1
    day_timing += 1

print(f"Result on {day_timing} day.")