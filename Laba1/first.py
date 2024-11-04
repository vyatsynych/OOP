from datetime import datetime

name = "Владислав"
location = "Kyiv"
current_date = datetime.now()
month = current_date.month

# Визначення пори року
if month in [12, 1, 2]:
    season = "Зима"
elif month in [3, 4, 5]:
    season = "Весна"
elif month in [6, 7, 8]:
    season = "Літо"
else:
    season = "Осінь"

print(f"{name} почала програмувати {current_date.strftime('%Y-%m-%d %H:%M:%S')}. {location} - найкраще місто!")
print(f"Поточний рік: {current_date.year}, Пора року: {season}")
