# Koosta dictionary vähemalt viie endale iseloomuliku tunnusega (näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).
# Väljasta elukoht kahel erineval viisil (kasutades get() meetodit ja mitte kasutades seda).
# Muuda magustoidu väärtust.
# Tee kordus üle dictionary ja väljasta kõik võtmed.
# Tee kordus üle dictionary ja väljasta kõik väärtused (pööra tähelepanu sellele, et saab mitmel viisil, proovi erinevaid võimalusi).
# Kontrolli, kas isikukood on dictionary's olemas.
# Leia dictionary suurus (elementide arv).
# Lisa element enda pikkuse jaoks.
# Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
# Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
# Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
# Tutvu kõigi dictionary meetoditega.
# Läbi ülesanne juhendi lõpus.

# 1. Создайте словарь, содержащий не менее пяти характеристик, характеризующих вас (например: имя, фамилия, год рождения, место жительства, любимый десерт).
# 2. Вывести место жительства двумя разными способами (с использованием метода get() и без его использования).
# 3.Измените ценность десерта.
# 4. Пройдитесь по словарю и выведите все ключи.
# 5. Перебрать словарь и вывести все значения (обратите внимание, что есть несколько способов, попробуйте разные варианты).
# 6. Проверьте, есть ли персональный идентификационный код в словаре.
# 7. Найдите размер словаря (количество элементов).
# 8. Добавьте элемент для вашего роста.
# 9. Удалите элемент года рождения (обратите внимание, что есть несколько способов).
# 10. Обратите внимание, что ключевое слово del можно использовать для удаления всего словаря.
# 11. Поймите и проверьте разницу между ключевым словом del и методом clear.
# 12. Изучите все методы работы со словарем.
# 13. Выполните задание в конце руководства.

1. my_dict = {
    'name': 'Mikhail',
    'second_name': 'Kucherenko',
    'yob': '1998',
    'address': 'Ranna 2',
    'fav_dessert': 'truhvlikook'
}
print(my_dict['address'])
my_dict['fav_dessert'] = 'meekook'
print(my_dict)
print(my_dict.keys())
x = my_dict.values()
print(x)
my_dict['yob'] = 2000
print(my_dict)
y = my_dict.items()
print(y)
if 'isikukood' in my_dict:
    print('yes')
else:
    print('no isikukood in dict')

print(len(my_dict))
my_dict.update({'height': '183'})
print(my_dict)
my_dict.pop('yob')
print(my_dict)