money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
money_in_bank = money_capital + salary
month = 0

while money_in_bank >= spend:
    money_in_bank -= spend
    money_in_bank += salary
    spend = spend + spend * increase
    month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
