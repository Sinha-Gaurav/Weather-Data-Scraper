from bs4 import BeautifulSoup
import requests

def rain():
    html_text = requests.get('https://www.eldoradoweather.com/climate/world-extremes/world-temp-rainfall-extremes.php').text
    soup = BeautifulSoup(html_text, 'lxml')
    rainfall = soup.find_all('table', style='width: 99%;')
    rows = rainfall[1].find_all('tr')
    open(f'rain.txt', 'w')
    for row in rows:
        place = row.find('a', target='_blank')
        if(place!=None):
            amount = row.find('font', color='#FFFFFF')
            more_data = place['href']
            print(f"Place: {place.text.strip()}")
            print(f"Amount of Rainfall: {amount.text.strip()}")
            print(f"Summarised Data Link: {more_data}")
            print("\n")
            with open(f'rain.txt', 'a') as f:
                f.write(f"Place: {place.text.strip()} \n")
                f.write(f"Amount of Rainfall: {amount.text.strip()} \n")
                f.write(f"Summarised Data Link: {more_data} \n\n")
    print(f'File saved')

def coldest():
    html_text = requests.get('https://www.eldoradoweather.com/climate/world-extremes/world-temp-rainfall-extremes.php').text
    soup = BeautifulSoup(html_text, 'lxml')
    cool = soup.find_all('table', style='width: 99%;')
    rows = cool[0].find_all('tr')
    open(f'coldest.txt', 'w')
    for row in rows:
        place = row.find('a', target='_blank')
        if(place!=None):
            temp = row.find('font', color='#FFFFFF')
            more_data = place['href']
            print(f"Place: {place.text.strip()}")
            print(f"Temperature: {temp.text.strip()}")
            print(f"Summarised Data Link: {more_data}")
            print("\n")
            with open(f'coldest.txt', 'a') as f:
                f.write(f"Place: {place.text.strip()} \n")
                f.write(f"Temperature: {temp.text.strip()} \n")
                f.write(f"Summarised Data Link: {more_data} \n\n")
    print(f'File saved')

def hottest():
    html_text = requests.get('https://www.eldoradoweather.com/climate/world-extremes/world-temp-rainfall-extremes.php').text
    soup = BeautifulSoup(html_text, 'lxml')
    hot = soup.find_all('table', border='0')
    rows = hot[1].find_all('tr')
    open(f'hottest.txt', 'w')
    for row in rows:
        place = row.find('a', target='_blank')
        if(place!=None):
            temp = row.find('font', color='#FFFFFF')
            more_data = place['href']
            print(f"Place: {place.text.strip()}")
            print(f"Temperature: {temp.text.strip()}")
            print(f"Summarised Data Link: {more_data}")
            print("\n")
            with open(f'hottest.txt', 'a') as f:
                f.write(f"Place: {place.text.strip()} \n")
                f.write(f"Temperature: {temp.text.strip()} \n")
                f.write(f"Summarised Data Link: {more_data} \n\n")
    print(f'File saved')

if __name__ == '__main__':
    print(f'''Enter the number corresponding to the type of data you want:
    1. Heat
    2. Cold
    3. Rain''')
    i = input()
    
    if(i=='1'): hottest()
    elif(i=='2'): coldest()
    elif(i=='3'): rain()