import json
from func.func import last_five, correct_date, correct_card, correct_count

with open("operations.json", 'rt', encoding='utf-8') as operations:
    # Преобразуем содержимое файла в список со операциями
    all_operations = json.load(operations)

last_five_date = last_five(all_operations)
print(last_five_date)
# Запускаем цикл перебора по последним 5 датам
for date in last_five(all_operations):

    # Запускаем цикл перебора списка с всеми операциями
    for dict in all_operations:

        # Берем дату из списка последних 5 операций и ищем эту операцию в списке со всеми операциями
        if date == dict['date']:
            date = correct_date(date)

            if "description" in dict:
                description = dict["description"]

            if "from" in dict:
                if "Счет" in dict["from"]:
                    from_ = correct_count(dict["from"]) + " -> "
                else:
                    from_ = correct_card(dict["from"]) + " -> "
            else:
                from_ = ""

            if "to" in dict:
                if "Счет" in dict["to"]:
                    to = correct_count(dict["to"])
                else:
                    to = correct_card(dict["to"])


            if "amount" in dict["operationAmount"]:
                amount = dict["operationAmount"]["amount"]

            if "code" in dict["operationAmount"]["currency"]:
                code = dict["operationAmount"]["currency"]["code"]

            print(f"{date}  {description}\n{from_}{to}\n{amount} {code}\n")

            break
