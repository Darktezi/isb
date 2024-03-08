
def write_to_file(filename, content):
    try:
        with open(filename, 'w', encoding="utf8") as file:
            file.write(content)
        print(f"Файл '{filename}' успешно записан.")
    except IOError:
        print(f"Ошибка при записи файла '{filename}'.")

def read_from_file(filename):
    try:
        with open(filename, 'r', encoding="utf8") as file:
            content = file.read()
        return content
    except IOError:
        print(f"Ошибка при чтении файла '{filename}'.")