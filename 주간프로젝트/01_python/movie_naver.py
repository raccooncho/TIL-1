import datetime
import requests
import csv

movies_name = []
movies_code = []

start_date = datetime.datetime(2019,1,13)
for i in range(10):
    t = start_date - datetime.timedelta(days=7 * i)
    target = t.strftime('%Y%m%d')
    
    key = 'e12be2ef03b4294b6b4ca0657423cbc6'
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={target}&weekGb=0'
    response = requests.get(URL).json()    
    response = response['boxOfficeResult']['weeklyBoxOfficeList']    

    for i in range(10):        
        movie_code = response[i]['movieCd']
        movies_code.append(movie_code)
        movie_name = response[i]['movieNm']
        movies_name.append(movie_name)
        
movies_name = list(set(movies_name))         
movies_code = list(set(movies_code))

naver_uri = 'https://openapi.naver.com/v1/search/movie.json?query='

client_id = 'FaSdalhj1Twe1bDOc9uO'
client_secret = 'Fjx3tc_Alv'
headers = { 
    'X-Naver-Client-Id': client_id, 
    'X-Naver-Client-Secret': client_secret
}

for movie in movies_name:
    response = requests.get(naver_uri + movie, headers=headers).json()
    movie_naver = []
    n = movies_name.index(movie)
    movie_naver.append(movies_code[n])    
    movie_naver.append(response['items'][0]['image'])
    movie_naver.append(response['items'][0]['link'])
    movie_naver.append(response['items'][0]['userRating'])
    
    f = open('movie_naver.csv', 'a+', encoding='utf-8', newline='')
    writer = csv.writer(f)

    writer.writerow(        
        movie_naver
    )

    f.close