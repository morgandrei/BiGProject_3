import json

with open("operations.json", 'rt', encoding='utf-8') as operations:
    # Преобразуем содержимое файла в список со операциями
    all_operations = json.load(operations)

print(all_operations)