# Сделайте так, чтобы число секунд отображалось в в иде дни:часы:минуты:секунды
Sec = int(input('введите число секунд '))
Days = Sec // 86400
rest = Sec % 86400
Hours = rest // 3600
rest = rest % 3600
minutes = rest // 60
seconds = rest % 60
print(f'{Days} days, {Hours} hours, {minutes} minutes, {seconds} seconds')

