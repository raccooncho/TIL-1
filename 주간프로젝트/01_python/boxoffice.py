import datetime
import requests
import csv

movie_dict = []

start_date = datetime.datetime(2018,11,11)
for i in range(10):
    t = start_date + datetime.timedelta(days=7 * i)
    target = t.strftime('%Y%m%d')
    
    key = 'e12be2ef03b4294b6b4ca0657423cbc6'
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={target}&weekGb=0'
    response = requests.get(URL).json()
    recorded_at = response['boxOfficeResult']['showRange']
    response = response['boxOfficeResult']['weeklyBoxOfficeList']



    for i in range(10):
        boxoffice = []
        results = {
            'movie_code': response[i]['movieCd'],
            'title': response[i]['movieNm'],
            'audience': response[i]['audiAcc'],
            'recorded_at': recorded_at
        }
        if response[i]['movieCd'] not in movie_dict:     
        
            movie_dict.append(results['movie_code'])
            movie_dict.append(results['title'])
            movie_dict.append(results['audience'])
            movie_dict.append(results['recorded_at'][9:])
            boxoffice.append(results['movie_code'])
            boxoffice.append(results['title'])
            boxoffice.append(results['audience'])
            boxoffice.append(results['recorded_at'][9:])
        else:
            pass
a = len(movie_dict) / 4

for i in range(int(a)):    
    a = movie_dict[4 * i: 4 * (i + 1)]
    f = open('boxoffice.csv', 'a+', encoding='utf-8', newline='')
    writer = csv.writer(f)

    writer.writerow(
        a
    )

    f.close