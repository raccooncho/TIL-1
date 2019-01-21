import datetime
import requests
import csv

movies = []

start_date = datetime.datetime(2019,1,13)
for i in range(10):
    t = start_date - datetime.timedelta(days=7 * i)
    target = t.strftime('%Y%m%d')
    
    key = 'e12be2ef03b4294b6b4ca0657423cbc6'
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={target}&weekGb=0'
    response = requests.get(URL).json()
    recorded_at = response['boxOfficeResult']['showRange']
    response = response['boxOfficeResult']['weeklyBoxOfficeList']    

    for i in range(10):        
        a = response[i]['movieCd'] 
        movies.append(a) 
movies = list(set(movies))

for i in movies:
    key = 'e12be2ef03b4294b6b4ca0657423cbc6'
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={i}'
    
    response = requests.get(URL).json()
    response = response['movieInfoResult']['movieInfo']
    output = []
    output.append(response['movieCd'])
    output.append(response['movieNm'])
    if response['movieNmEn'] != '':
        output.append(response['movieNmEn'])
    if response['movieNmOg'] != '':
        output.append(response['movieNmOg'])
    output.append(response['openDt'])
    output.append(response['genres'][0]['genreNm'])
    output.append(response['directors'][0]['peopleNm'])
    output.append(response['audits'][0]['watchGradeNm'])    

    for i in range(len(response['actors'])):
        output.append(response['actors'][i]['peopleNm'])
        if i == 2:
            break
        # if response['actors'][i]['peopleNm'] == '':
        #     break 
        # elif response['actors'][i]['peopleNm'] != '':
            


    f = open('movie.csv', 'a+', encoding='utf-8', newline='')
    writer = csv.writer(f)

    writer.writerow(        
        output
    )

    f.close