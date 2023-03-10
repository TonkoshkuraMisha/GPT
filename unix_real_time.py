import time

current_time = time.time()
unix_time = int(current_time)
print("Текущее время в формате Unix: ", unix_time)


import datetime

# unix_time = 1646850445
# converted_time = datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
# print("Конвертированное время: ", converted_time)



saves = [1678479565, 1678438567, 1678458534, 1678378589]
saves.sort(reverse=True)

for i in saves:
    converted_time = datetime.datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S')
    print("Конвертированное время: ", converted_time)