per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите желаемую сумму вклада :")
deposit = []

tkb = int(per_cent['ТКБ'] * (int(money)) /100)
skb = int(per_cent['СКБ'] * (int(money)) /100)
vtb = int(per_cent['ВТБ'] * (int(money)) /100)
sber = int(per_cent['СБЕР'] * (int(money)) /100)

deposit.append(tkb)
deposit.append(skb)
deposit.append(vtb)
deposit.append(sber)

print("deposit : " , deposit)
print("Максимальная сумма, которую вы можете заработать -", max(deposit), "руб. в год.")