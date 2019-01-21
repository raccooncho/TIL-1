from datetime import datetime, timedelta
import requests
import csv
import urllib.request
import json

cl = []

start_date = datetime(2018,11,11)
for i in range(10):
    t = start_date + timedelta(days=7 * i)
    target = t.strftime('%Y%m%d')
        
    key = 'e12be2ef03b4294b6b4ca0657423cbc6'
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={target}&weekGb=0'
    response = requests.get(URL).json()
    response = response['boxOfficeResult']['weeklyBoxOfficeList']
    
    for k in range(10):
        moviecode = response[k]['movieCd']
        cl.append(moviecode)

cl = list(set(cl))

 

for movieCd in cl:
    movie_info = [] 
    key = 'e12be2ef03b4294b6b4ca0657423cbc6'
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo?key={key}&movieCd={movieCd}'
    response = requests.get(URL).json()
    response = response['movieInfoResult']['movieInfo']   
            
    movieCd = response['movieCd']
    movieNm = response['movieNm']
    movieNmEn = response['movieNmEn']
    movieNmOg = response['movieNmOg']
    openDt = response['openDt']
    showTm = response['showTm']
    genreNm = response['genres'][0]['genreNm']
    peopleNm = response['directors'][0]['peopleNm']
    watchGradeNm = response['audits'][0]['watchGradeNm']
    
    if len(response['actors']) == 0:
        actor1 = ''
        actor2 = ''
        actor3 = ''
    elif len(response['actors']) == 1:
        actor1 = response['actors'][0]['peopleNm']
        actor2 = ''
        actor3 = ''
    elif len(response['actors']) == 2:
        actor1 = response['actors'][0]['peopleNm']
        actor2 = response['actors'][1]['peopleNm']
        actor3 = ''
    elif len(response['actors']) >= 3:
        actor1 = response['actors'][0]['peopleNm']
        actor2 = response['actors'][1]['peopleNm']
        actor3 = response['actors'][2]['peopleNm']
    
    movie_info.append(movieCd)
    movie_info.append(movieNm)
    movie_info.append(movieNmEn)
    movie_info.append(movieNmOg)
    movie_info.append(openDt)
    movie_info.append(showTm)
    movie_info.append(genreNm)
    movie_info.append(peopleNm)
    movie_info.append(watchGradeNm)
    movie_info.append(actor1)
    movie_info.append(actor2)
    movie_info.append(actor3)    
    
    f = open('movie.csv', 'a+', encoding='utf-8', newline='')
    writer = csv.writer(f)

    writer.writerow(movie_info)

    f.close     


    