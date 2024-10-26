calls = 0


# Задание 1 (счётчик обращения к функциям)
def count_calls():
    global calls
    calls = calls + 1


# задание 2 (измерение длинны слова, верхний и нижние регистры слова)
def string_info(string):
    string_ = ()
    b = (len(string))
    c = string.upper()
    d = string.lower()
    string_ = (b, c, d)
    print(string_)
    count_calls()


# задание 3 (поиск слова в списке без учёта регистра слов)
def is_contains(string, list_to_search):
    string_ = string.lower()
    list_ = []
    for i in list_to_search:
        list_.append(i.lower())

    marker = string_ in list_
    print(marker)
    count_calls()


string_info('Moon')
string_info("Sunday")
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
