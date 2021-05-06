bilety = int(input("Введите количество приобретаемых билетов:"))
result = 0
for i in range(bilety):
    vozrast = int(input("Введите возраст участника конференции:"))
    if vozrast < 18:
       result += 0
    elif 18 <= vozrast < 25:
       result += 990
    elif vozrast >= 25:
       result += 1390
print('Общая стоимость билетов:', result)
if bilety > 3:
    result = result - (result * 0.1)
print('Сумма к оплате с учётом скидки:', result)


