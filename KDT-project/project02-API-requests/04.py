import requests
from pprint import pprint


def recommendation(title):
    
    # 여기에 코드를 작성합니다.  
    try:
        # 영화 번호 불러오기
        BASE_URL = 'https://api.themoviedb.org/3'
        path = '/search/movie'
        URL = BASE_URL + path
        params = {
            'api_key':'bc8f8f1749168f795addaf61d9561f9c',
            'language':'ko-KR',
            'query':title
        }
        movie_id = requests.get(URL, params = params).json().get('results')[0].get('id')

        # 영화 추천목록 가져오기
        URL_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
        params_2 = {
            'api_key':'bc8f8f1749168f795addaf61d9561f9c',
            'language':'ko-KR',
        }
        response = requests.get(URL_2, params = params_2).json().get('results')
        lst = []
        for i in response:
            lst.append(i.get('title'))

        return lst

    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
