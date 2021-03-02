# данный код
numbers =(10,35)
print(sum(numbers))
# требуемый вывод:
# 45

# данный код
long_word = (
    'т', 'т', 'а', 'и', 'и', 'а', 'и',
    'и', 'и', 'т', 'т', 'а', 'и', 'и',
    'и', 'и', 'и', 'т', 'и'
)
# count_t = long_word.count("т")
print("Количество 'т':",long_word.count("т"))
print("Количество 'a':",long_word.count("а"))
print("Количество 'и':",long_word.count("и") )
# требуемый вывод:
# Колличество 'т': 5
# Колличество 'а': 3
# Колличество 'и': 11

# данный код
week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days =  len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))
# требуемый вывод:
# 28

lake = ("Python", 51, False, "22")
print(lake[lake.index("22")])