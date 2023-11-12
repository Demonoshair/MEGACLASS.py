from colorama import Fore, Back, Style   #Импорт колорамы

print(Fore.RED + "Красный текст")    #Вывод красного текста
print(Fore.GREEN + "Зеленый текст")  #Вывод зелёного текста
print(Fore.BLUE + "Синий текст")     #Вывод синего текста

print(Back.RED + "Текст на красном фоне")    #Текст на красном фоне
print(Back.GREEN + "Текст на зеленом фоне")  #Текст на зелёном фоне
print(Back.BLUE + "Текст на синем фоне")     #Текст на синем фоне

print(Style.NORMAL + "Нормальный текст") #Стандартный текст
print(Style.BRIGHT + "Яркий текст")      #Яркий текст

colorama.deinit()   #сброс стиля текста