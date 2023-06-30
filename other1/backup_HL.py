import os
import shutil
import time
import zipfile


def backup_files(source_dir, destination_dir):
    timestamp = time.strftime('%Y%m%d%H%M%S')
    backup_folder_name = f'backup_{timestamp}'
    backup_path = os.path.join(destination_dir, backup_folder_name)

    # Створюємо директорію для резервної копії
    os.makedirs(backup_path)

    # Копіюємо файли
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            destination_path = os.path.join(backup_path, os.path.relpath(file_path, source_dir))
            # Копіюємо файл зі збереженням метаданих
            shutil.copy2(file_path, destination_path)

    # Створюємо архів з резервною копією
    shutil.make_archive(backup_path, 'zip', backup_path)

    print(f'Створено резервну копію у файлі: {backup_path}.zip')


# Вказуємо директорії для резервного копіювання
source_directory = "C:/Users/tonko/AppData/Local/Phoenix"
destination_directory = "G:/Мой диск/BackUpGamesSaved/Phoenix"

# Виклик функції для створення резервної копії
backup_files(source_directory, destination_directory)
