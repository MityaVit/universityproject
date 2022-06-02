import random
import time
time1 = time.time()

def is_alphabet_or_space(char): # функция возвращает true, если символ - буква алфавита или пробел, пробел учитывается для разделения слов
    return str.isalpha(char) or char == " "


def split(my_str):  # функция возвращает список слов
    my_str = ''.join(filter(is_alphabet_or_space, my_str)) # filter принимает 1 - функцию, по которому мы выбираем, какие обьекты нам подходят (если true - подходит), 2 - к чему мы будем принимать 1 функцию
    my_str = my_str.lower() # затем мы соединяем результаты фильтрации в строку
    my_words = my_str.split()
    return my_words


source = open(input("Введите файл: "), encoding="utf-8")
fresult = open('fresult.txt', 'w+', encoding='utf-8')
fanylisis = open('fanalysis.txt', 'w+', encoding='utf-8')
my_text = source.read()
words = split(my_text)


def quicksort(words): # сортировка
    if len(words) <= 1:
        return words
    else:
        q = random.choice(words)
        s_words = []
        m_words = []
        e_words = []
        for n in words:
            if n < q:
                s_words.append(n)
            elif n > q:
                m_words.append(n)
            else:
                e_words.append(n)
        return quicksort(s_words) + e_words + quicksort(m_words)


kolvoslov = len(words)
time2 = time.time()
fanylisis.write(f"Введённый текст:\n{my_text}\n\n")
fanylisis.write(f"Вариант 17: кириллица, по алфавиту, по возрастанию, игнорировать числа, быстрая сортировка\n")
fanylisis.write(f"Количество слов: {kolvoslov}\n")
fanylisis.write(f"Время сортировки: {time2 - time1} мс\n")
fanylisis.write(f"Статистика (количество слов на каждую букву алфавита):\n")
print(f"Введённый текст:\n{my_text}\n\nВариант 17: кириллица, по алфавиту, по возрастанию, игнорировать числа, быстрая сортировка\nКоличество слов: {kolvoslov}\nВремя сортировки: {time2 - time1} \nСтатистика (количество слов на каждую букву алфавита):\n")

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

for i in range(len(alphabet)): # подсчёт букв, которые встречаются в тексте
    kvo = 0
    for j in range(len(my_text)):
        if my_text[j][0].lower() == alphabet[i]:
            kvo += 1
    fanylisis.write(f"{alphabet[i]} - {kvo} \n")
    print(f"{alphabet[i]} - {kvo} \n")

for ops in range(len(quicksort(words)) - 1): # это для того, чтобы слова, начинающиеся с одной буквы писались в одну строку
    fresult.write(quicksort(words)[ops] + " ")
    if quicksort(words)[ops][0] != quicksort(words)[ops+1][0]:
        fresult.write("\n")
fresult.write(quicksort(words)[-1])

source.close()
fresult.close()
fanylisis.close()
