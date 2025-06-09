from bs4 import BeautifulSoup

with open('weather.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

forecast_data = []
rows = soup.find('tbody').find_all('tr')

for row in rows:
    cols = row.find_all('td')
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace('°C', ''))
    condition = cols[2].text.strip()
    forecast_data.append({'day': day, 'temperature': temp, 'condition': condition})

print("Weather Forecast:")
for entry in forecast_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")

max_temp = max(entry['temperature'] for entry in forecast_data)
hottest_days = [entry['day'] for entry in forecast_data if entry['temperature'] == max_temp]

sunny_days = [entry['day'] for entry in forecast_data if entry['condition'] == 'Sunny']

average_temp = sum(entry['temperature'] for entry in forecast_data) / len(forecast_data)

print("\nDay(s) with the highest temperature:")
for day in hottest_days:
    print(day)

print("\nDay(s) with 'Sunny' condition:")
for day in sunny_days:
    print(day)

print(f"\nAverage temperature for the week: {average_temp:.2f}°C")
