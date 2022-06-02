# universityproject
Программа принимает на вход название файла с текстом (только кириллица) или путь к нему и выводит информацию о содержании файла, количестве слов, времени, затраченном на работу алгоритма, количестве слов на каждую букву алфавита в файл fanylisis и в консоль, а в файл fresult выводит набор слов, использованных в тексте, отсортированный в порядке алфавита так, что слова, начинающиеся с одной буквы, пишутся в одну строку. Программа игнорирует числа.
Для сортировки списка слов использовалась рекурсивная функция под названием quicksort (метод: быстрая сортировка).
Для работы с программой необходимо иметь файл с текстом (минимум 2 слова, иначе программа просто вернёт слово из файла), название которого необходимо вписать с учётом расширения (txt).
Результат работы программы записывается в два предварительно созданных файла: fresult и fanylisis (то, что записывается в fanylisis дублируется в консоль).

Словесное описание работы алгоритма:

1. Начало;
2. Создание переменной time1 со значением time.time() (эта функция возвращает число секунд, прошедших с начала эпохи). По сути эта переменная является точкой отсчёта для измерения времени работы алгоритма;
3. Ввод названия исходного файла с расширением;
4. Открытие исходного файла;
5. Открытие файла для записи результата (fresult);
6. Открытие файла для записи анализа (fanylisis);
7. Создание функции is_alphabet_or_space, которая распознаёт пробелы между элементами;
8. Создание функции split со значением my_str, которая делит текст на отдельные элементы (слова) и переводит все буквы в нижних регистр;
9. Создание переменной my_text и присваивание ей значения содержимого (текста) исходного файла;
10. Создание переменной words, присваивание ей значения, которая возвращает функция split со значением my_text;
11. Создание функции быстрой сортировки под названием quicksort, принимающей на вход значение words;
12. Создание переменной kolvoslov, значением которой является длина списка words.
13. Создание переменной time2 со значением time.time(). Эта переменная является конечной точкой отсчёта измерения времени работы алгоритма;
14. Вывод в файл fanylisis:
1) Исходного текста;
2) Номера варианта и его условия;
3) Количества слов;
4) Времени сортировки (в миллисекундах), полученного путём разности переменных time2 и time1;
5) Статистики (количества слов на каждую букву алфавита);
15. Вывод результатов, ранее выведенных в fanylisis, в консоль;
16. Создание переменной alphabet, содержащую в себе список всех элементов кириллицы (за исключением цифр);
17. Создание цикла, который считает буквы, встречающиеся в элементах my_words, и выводит результат в файл fanylisis и в консоль;
18. Создание цикла, принимающего на вход результат работы функции quicksort со значением words, который делает так, чтобы слова, начинающиеся с одной буквы, записывались в одну строку, а после этой строки ставился перенос (\n), и выводит результат в fresult.
19. Вывод в fresult последнего слова из words;
20. Закрытие исходного файла;
21. Закрытие файла fresult;
22. Закрытие файла fanylisis;
23. Конец.

Описание всех функций исходного кода:

1. Функция is_alphabet_or_space:
Возвращает true, если символ является буквой алфавита или пробелом.
1) Начало;
2) На вход берётся параметр (символ);
3) Если параметр является буквой алфавита или пробелом, функция возвращает значение True;
4) Конец.

2. Функция split:
Принимает на вход параметр my_str и возвращает список слов.
1) Начало;
2) Создание переменной my_str, которая принимает значение filter со значениями is_alphabet_or_space и my_str, разделяя пустой строкой (filter принимает функцию, по которому мы выбираем, какие объекты нам подходят (если подходят – True) и к чему мы будем применять 1 функцию);
3) Перевод символов, которые хранит переменная my_str в нижний регистр;
4) Функция возвращает значение my_words;
5) Конец.

3. Функция quicksort:
Использование метода быстрой сортировки, реализованного с помощью рекурсивной функции. Функция берёт в качестве параметра переменную words и проверяет, чтобы длина списка слов была больше 1 и фильтрует элементы (слова) списка words, разделяя массив на две части, в одной из которых находятся элементы меньше определённого значения, в другой – больше или равные.
1) Начало;
2) Если длина списка words <= 1, то возвращает words, если же words > 1, то создаёт переменную q, принимающей за значение случайный выбор элемента из списка words и создаёт массивы s_words, m_words и e_words;
3) Распределение элементов списка по ранее упомянутым массивам;
4) Функция возвращает сама себя со значением s_words, потом выводит e_words, а потом снова возвращает себя со значением m_words;
5) Конец.

Тестирование программы проводилось на десяти тестах разной длины: от 491 (3038 символов) слова до 954 (6257 символов).
Результаты тестирования показали, что время работы алгоритма напрямую зависит от объема входящих данных.
После описания работы программы была произведена оценка сложности её алгоритма в О-нотации. Проведённый анализ показал, что сложность алгоритма – линейная, что является наилучшим результатом при применении метода быстрой сортировки.
