names = [ "кеша" , " толик" , "попугай "]

names.append("попугай1") # append функция добавления элемента в список - попугай 1 
print (names)

names.pop() # pop - удаление элемента списка - в данном случа в скобках пусто - значит удалит последний
print(names)

""" про метод индекс"""

n = names.index(" толик") # метод индекс - запрос в данном случае через метод индекс индекса толик
print (n) # важно чтоб элемент был написан со всеми прбелами мобелами и все такое -иначе питон его не увидит

"""функция len - измерение длины списка"""

names = [ "кеша" , " толик" , "попугай "]
print(len(names))# len - функция измерения длины списка - в данном случае три элемента - значит 3