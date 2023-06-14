from datetime import datetime


def last_five(all_operations):
    '''
    Функция возврвщает даты 5 выполненных последних операций
    :param all_operations: необработанный файл с всеми операциями
    '''

    # Исправляем файл с всеми операциями, оставляем только те операции, где есть дата
    execution_oper = []
    for dict in all_operations:
        for k, v in dict.items():
            if v == "EXECUTED":
                execution_oper.append(dict)

    # Создаем список, где будут находиться только даты последных 5 операций
    date_list = []
    for el in execution_oper:
        date_list.append(el["date"])

    date_list.sort(reverse=True)

    return date_list[:5]


def correct_date(date):
    """
    Функция преобразует строку с датой в нужный формат
    :param date: входит тип данных строка с датой
    """
    date = datetime.strptime("".join(date[:10]), "%Y-%m-%d")
    return "{}.{}.{}".format(date.day, date.month, date.year)


def correct_card(from_):
    """
    Функция преобразует входящую строку с номером карты в нужный формат
    """
    #  Тип источника (MAESTRO, VISA, и т.п.) складываем в отдельный список, который потом склеим методом join в строку
    from_type = []
    for i in from_:
        if i.isalpha() or i == " ":
            from_type.append(i)

    card_number = from_.split()[-1]

    #Получаем номер карты с * вместо цифр
    private_number = card_number[:-10] + len(card_number[-10:-4]) * '*' + card_number[-4:]

    # Определяем, подгруппы по сколько цифр будет разделяться номер карты
    n = 4

    # Возвращаем склееную строку из типа источника и номера карты, разделенного на подгруппы и
    return "".join(from_type) + " ".join([private_number[i:i + n] for i in range(0, len(private_number), n)])


def correct_count(to):
    """
    Функция преобразует входящую строку с номером счета получателя в нужный формат
    """
    to_type = []

    for i in to:

        if i.isalpha() or i == " ":
            to_type.append(i)

    to_number = to.split()[-1]

    private_number = len(to_number[-6:-4]) * '*' + to_number[-4:]

    return "".join(to_type) + private_number
