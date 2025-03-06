

sales_data = input("Введите информацию о продажах в формате 'товар:количество', разделённую запятыми: ")
pairs = sales_data.split(",")

pair1, pair2, pair3, pair4 = pairs[0], pairs[1], pairs[2], pairs[3] # Предполагаем, что в строке ровно 4 пары

product1, count1 = pair1.split(":")# Разбираем каждую пару на товар и кол-во
product2, count2 = pair2.split(":")
product3, count3 = pair3.split(":")
product4, count4 = pair4.split(":")

sales_dict = {} # словарь для хранения продаж


sales_dict[product1] = sales_dict.get(product1, 0) + int(count1)# Добавляем значения в словарь, get() для суммирования
sales_dict[product2] = sales_dict.get(product2, 0) + int(count2)
sales_dict[product3] = sales_dict.get(product3, 0) + int(count3)
sales_dict[product4] = sales_dict.get(product4, 0) + int(count4)


print("Суммарные продажи по товарам:")
print(sales_dict)