import os
import sys
import datetime

# Путь к директории, которую нужно анализировать
path = '/'

def analyze_directory(path):
    total_files = 0
    top_files = []
    for root, dirs, files in os.walk(path, followlinks=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if not os.path.islink(file_path):
                    file_size = os.path.getsize(file_path) / 1024
                    top_files.append((file_path, file_size))
                    total_files += 1
            except OSError as e:
                print(f"Ошибка при обработке {file_path}: {e}")
                continue

    top_files = sorted(top_files, key=lambda x: x[1], reverse=True)[:10]
    return total_files, top_files

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Привет, {name}! Текущее время: {current_time}\n")
    else:
        print("Привет! Вы не указали имя. Используйте `python app.py [Имя]` чтобы задать имя.\n")

    total_files, top_files = analyze_directory(path)

    print(f"Общее количество файлов: {total_files}")
    print("Топ-10 файлов по размеру:")
    for file_path, size in top_files:
        print(f"{file_path}: {size:.2f} KB")
