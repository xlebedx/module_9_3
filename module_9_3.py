first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(fir) - len(sec) for fir, sec in zip(first, second) if len(fir) != len(sec))
second_result = (len(first[i]) == len(second[i]) for i in range(3))

if __name__ == '__main__':
    print(list(first_result))
    print(list(second_result))
