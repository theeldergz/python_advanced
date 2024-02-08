# get_age
### 1.Проблема в работе функции get_age, нет импортированного модуля datetime
### Была решена при помощи импорта модуля


### 2.Функция неверно считала возраст
### Было решено правильным порядком вычитаемого и уменьшаемого


# get_name
### Ошибок не было


# set_name
### Была проблема с изменением(установкой) аргумента name
### Решено изменением self.name = self.name на self.name = name


# set_address
### Была проблема в self.address == address, обьекты сравнивались друг с другом
### исправлено на self.address = address


# get_address
### Ошибок не было


# is_homeless
### Была ошибка в return self.address is None
### Было исправлено на "if self.address:
###                           return True
###                     else:
 ###                          return False"