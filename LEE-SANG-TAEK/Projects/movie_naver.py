import requests
import urllib.request
import csv
import json
from datetime import datetime, timedelta

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
            
    
    movieNm = response['movieNm']

    naver_URI = 'https://openapi.naver.com/v1/search/movie.json?query='
    client_id = 'FaSdalhj1Twe1bDOc9uO'
    client_secret = 'Fjx3tc_Alv'
    headers = {'X-Naver-Client-Id' : client_id, 'X-Naver-Client-Secret': client_secret}
   
    response = requests.get(naver_URI + movieNm, headers=headers)
    response = response.json()
    l = [
        movieCd,
        response['items'][0]['image'],
        response['items'][0]['link'],
        response['items'][0]['userRating'],
    ]

    f = open('movie_naver.csv', 'a+', encoding='utf-8', newline='')
    writer = csv.writer(f)

    writer.writerow(l)

    f.close     

    image_URL = l[1]
#     outpath = '\images'
#     outfile = f'{movieCd}.jpg'
    urllib.request.urlretrieve(image_URL, f'images\{movieCd}.jpg')

     