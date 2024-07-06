# Аве, Цезарь 🌶️
def ave_cezar(text, rot_n):
    eng = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rus = "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    new_text = ""
    if rot_n > 0:   # Для положительного сдвига вправо
        for i in range(len(text)):
            if text[i] in eng:   # Для ENG
                if text[i].islower():   # Нижний регистр
                    x = chr(ord(text[i]) + rot_n)
                    if ord(x) > ord("z"):   # если дальше z = 122 и продолжать с буквы "а".
                        new_text += chr(ord("a") + (rot_n - (123 - ord(text[i]))))   # до юникод a = 97 добавляем остаток от шага после буквы "z"
                    else:
                        new_text += x
                if text[i].isupper():   # Верхний регистр
                    x = chr(ord(text[i]) + rot_n)   # не заходит за границу
                    if ord(x) > ord("Z"):   # если дальше Z = 90 и продолжать с буквы "а".
                        new_text += chr(ord("A") + (rot_n - (91 - ord(text[i]))))   # до юникод А = 65 добавляем остаток от шага после буквы "Z"
                    else:
                        new_text += x
            if text[i] in rus:   # Для RUS
                if text[i].islower():   # Нижний регистр
                    x = chr(ord(text[i]) + rot_n)
                    if ord(x) > ord("я"):   # если дальше я = 1103 и продолжать с буквы "а".
                        new_text += chr(ord("а") + (rot_n - (1104 - ord(text[i]))))   # до юникод a = 1072 добавляем остаток от шага после буквы "я"
                    else:
                        new_text += x
                if text[i].isupper():   # Верхний регистр
                    x = chr(ord(text[i]) + rot_n)   # не заходит за границу
                    if ord(x) > ord("Я"):   # если дальше Я = 1071 и продолжать с буквы "А".
                        new_text += chr(ord("А") + (rot_n - (1072 - ord(text[i]))))   # до юникод a = 97 добавляем остаток от шага после буквы "Я"
                    else:
                        new_text += x
            if text[i].isalpha() == False:
                new_text += text[i]   # Для треша и цифр
        return new_text
####################################################################
    if rot_n < 0:   # Для негативного сдвига влево
        for i in range(len(text)):
            if text[i] in eng:   # Для ENG
                if text[i].islower():   # Нижний регистр
                    x = chr(ord(text[i]) - abs(rot_n))
                    if ord(x) < ord("a"):
                        new_text += chr(ord("z") - (abs(rot_n) - (ord(text[i]) - ord("a") + 1)))
                    else:
                        new_text += x
                if text[i].isupper():   # Верхний регистр
                    x = chr(ord(text[i]) - abs(rot_n))
                    if ord(x) < ord("A"):
                        new_text += chr(ord("Z") - (abs(rot_n) - (ord(text[i]) - ord("A") + 1)))
                    else:
                        new_text += x
            if text[i] in rus:   # Для RUS
                if text[i].islower():   # Нижний регистр
                    x = chr(ord(text[i]) - abs(rot_n))
                    if ord(x) < ord("а"):
                        new_text += chr(ord("я") - (abs(rot_n) - (ord(text[i]) - ord("а") + 1)))
                    else:
                        new_text += x
                if text[i].isupper():   # Верхний регистр
                    x = chr(ord(text[i]) - abs(rot_n))
                    if ord(x) < ord("А"):
                        new_text += chr(ord("Я") - (abs(rot_n) - (ord(text[i]) - ord("А") + 1)))
                    else:
                        new_text += x
            if text[i].isalpha() == False:
                new_text += text[i]   # Для треша и цифр
        return new_text

def uncoding_cezar(text):
    print("Вот вариант(ы) текста зашифрованного алгоритмом Цезаря, выберите подходящий:")
    list = []
    for i in range(1, 32):
        list.append(ave_cezar(text, i))
    return print(*list, sep='\n')

text = input("Введите ваше сообщение:")
print("1) Зашифровать текст алгоритмом Цезаря;", "\n2) Расшифровать зашифрованный текст алгоритмом Цезаря")
choise = input("Выберите что вы хотите сделать(1/2)?:")
if choise == "1":
    rot_n = int(input("Введите число ROT N (сдвиг в одну из сторон):"))
    print(ave_cezar(text, rot_n))
elif choise == "2":
    print(uncoding_cezar(text))