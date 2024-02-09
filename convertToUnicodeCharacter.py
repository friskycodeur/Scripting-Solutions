import unicodedata

file_path = input()
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            unicode_character = unicodedata.lookup(line)
            print(f'{line}: {unicode_character}')
except FileNotFoundError:
    print(f"Error: File not found - {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")



