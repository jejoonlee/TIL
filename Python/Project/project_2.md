# ๐ Project 1

[00. API ๋ฌธ์์ requests ํ์ฉ (์ฐ์ต)](#00-api-๋ฌธ์์-requests-ํ์ฉ-์ฐ์ต)

[01. ์ธ๊ธฐ ์ํ ์กฐํ](#01-์ธ๊ธฐ-์ํ-์กฐํ)

[02. ํน์  ์กฐ๊ฑด์ ๋ง๋ ์ธ๊ธฐ ์ํ ์กฐํ](#02-ํน์ -์กฐ๊ฑด์-๋ง๋-์ธ๊ธฐ-์ํ-์กฐํ)

[03. ํน์  ์กฐ๊ฑด์ ๋ง๋ ์ธ๊ธฐ ์ํ ์กฐํ](#03-ํน์ -์กฐ๊ฑด์-๋ง๋-์ธ๊ธฐ-์ํ-์กฐํ)

[04. ์ํ ์กฐํ ๋ฐ ์ถ์ฒ ์ํ ์กฐํ](#04-์ํ-์กฐํ-๋ฐ-์ถ์ฒ-์ํ-์กฐํ)

[05. ์ถ์ฐ์ง ๋ฐ ์ฐ์ถ์ง ๋ฐ์ดํฐ ์กฐํ](#05-์ถ์ฐ์ง-๋ฐ-์ฐ์ถ์ง-๋ฐ์ดํฐ-์กฐํ)





## โ๏ธ ํ์ด์ฌ ๊ธฐ๋ฐ ๋ฐ์ดํฐ ํ์ฉ

### ๋ชฉํ

- Python ๊ธฐ๋ณธ ๋ฌธ๋ฒ(์กฐ๊ฑด๋ฌธ, ๋ฐ๋ณต๋ฌธ) ํ์ฉ
- Python ์ธ๋ถ ๋ผ์ด๋ธ๋ฌ๋ฆฌ ํ์ฉ
- API์ JSON ๋ฐ์ดํฐ์ ํ์ฉ



#### TMDB ํ์ฉ https://www.themoviedb.org/settings/api





## 00. API ๋ฌธ์์ requests ํ์ฉ (์ฐ์ต)

- ์๋์ ๋ฌธ์๋ฅผ ํ์ฉํ์ฌ BTC(๋นํธ์ฝ์ธ)์ KRW(์) ์ ์ผ์ข๊ฐ๋ฅผ ์ถ๋ ฅ
- https://apidocs.bithumb.com/reference/ํ์ฌ๊ฐ-์ ๋ณด-์กฐํ

```python
# pip install requests 
import requests
# URL๋ก
order_currency = 'BTC' 
payment_currency = 'KRW' 
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# ์์ฒญ์ ๋ณด๋ด์
response = requests.get(URL)

# print(response.json())  response๋ฅผ json์ผ๋ก ์ด๊ธฐ

data = response.json()
print(data.get('data').get('prev_closing_price'))
```

- `.get` ์ ๋์๋๋ฆฌ์ ์๋ key์ value๋ฅผ ๊ฐ์ง๊ณ  ์ค๋ ๊ฒ



## 01. ์ธ๊ธฐ ์ํ ์กฐํ

```python
import requests

Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params ={
    'api_key': '652241f716c0f8b8f5006465a644f600',
    'language': 'en-en'
}
# popular๋ TMDB์์ ์๋ ์ํ ์ค ์ ๋ชํ ์ํ๋ฅผ JSON ํํ๋ก ๊ฐ์ง๊ณ  ์จ ๊ฒ
response = requests.get(Base_URL+path, params = params).json()

def popular_count():
    pass
    mov_list = []                           # list๋ฅผ ๋ง๋ค์ด์ค๋ค
    results = response.get('results')       # 1. Page์ Results๋ผ๋ key 2๊ฐ๊ฐ ๋จผ์  ์๋๋ฐ, Results๋ฅผ ๊บผ๋ด์จ๋ค
    for r in results:                       # 2. results๋ ๋ฆฌ์คํธ์ด๋ผ์, ๋์๋๋ฆฌ๋ก ํ์ ๋ณํ์ ํด์ค๋ค
        movies = r.get('original_title')    # 3. ๋์๋๋ฆฌ์ ์๋ key๋ค ์ค 'original_title'์ ๊ฐ์ง๊ณ  ์จ๋ค
        mov_list.append(movies)             # 4. ์ํ ์ ๋ชฉ๋ค์ ๋ง๋ค์ด ๋์ ๋ฆฌ์คํธ์ ๋ฃ์ด ๋๋ค
    return len(mov_list)                    # 5. ๋ฆฌ์คํธ์ ๊ธธ์ด๋ฅผ ๊ตฌํ๋ฉด, ๊ทธ๊ฒ์ด ์ ๋ชํ ์ํ ๊ฐ์์ด๋ค


# ์๋์ ์ฝ๋๋ ์์ ํ์ง ์์ต๋๋ค.
if __name__ == '__main__':
    """
    popular ์ํ๋ชฉ๋ก์ ๊ฐ์ ๋ฐํ
    """
print(popular_count())
```

- base_URL๋ ๊ธฐ๋ณธ URL์ด๋ค. ๋์ค์ `path`๊ฐ 2๊ฐ ์ด์์ผ ๋์, ๊ณ์ ์ฌ์ฉํ  ์ ์๋ค.
- JSON ํํ๋ฅผ ๊ฐ์ง๊ณ  ์ฌ๋, ๋ฆฌ์คํธ ์์ ๋์๋๋ฆฌ๊ฐ ์๋์ง ํ์ธ (๋ฆฌ์คํธ ์์ ์์ผ๋ฉด, ๋์๋๋ฆฌ๋ฅผ ๋ฆฌ์คํธ ๋ฐ์ผ๋ก ๊บผ๋ด์ผ ํ๋ค)





## 02. ํน์  ์กฐ๊ฑด์ ๋ง๋ ์ธ๊ธฐ ์ํ ์กฐํ

```python
import requests
from pprint import pprint

Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
  'api_key': '652241f716c0f8b8f5006465a644f600',
  'language': 'en-en'
}

response = requests.get(Base_URL+path, params = params).json()


def vote_average_movies():
    pass 
    l = []
    result = response.get('results')
    for i in result:
      if i['vote_average'] >= 8:
        l.append(i)
    
    return(l)

pprint(vote_average_movies())
```

- `ใฃ=[]` ์ ๋ฆฌ์คํธ ๋ง๋๋ ๊ฒ
- `result = response.get('results')` ๋ `response` ๋ผ๋ ๋ฆฌ์คํธ ์์ `results`๋ผ๋ ๋ฆฌ์คํธ๋ฅผ ๊ฐ์ง๊ณ  ์ค๋ ๊ฒ

```python
for i in result:
  if i['vote_average'] >= 8:
    l.append(i)
```

- `i` ๋ `result` ์์ ์๋ ๋์๋๋ฆฌ๋ค์ ํ๋์ฉ ๋ฐํํ๋ ๊ฒ
- ๊ทธ ์ค `i['vote_average']` ๋ฅผ ํตํด `i`์ key ์ค `'vote_average'`๋ผ๋ ํค์ ๊ฐ์ ๊ฐ์ง๊ณ  ์จ๋ค
- ๊ทธ ํ ๊ฐ์ด 8 ์ด์์ด๋ฉด `l` ๋ฆฌ์คํธ์ ๋ฃ์๋ค

```python
response = requests.get(Base_URL+path, params = params).json().get('results')
# .get('results')๋ฅผ ์จ์ 'results'๋ผ๋ ๋ฆฌ์คํธ๋ฅผ ๋ฐํํ๋ค

def vote_average_movies():
# ์์ 'result'๊ฐ 'response'๋ก ๋ฐ๋๋ค
    l = []
    for i in response:
      if i['vote_average'] >= 8:
        l.append(i)
    
    return(l)

pprint(vote_average_movies())
```





## 03. ํน์  ์กฐ๊ฑด์ ๋ง๋ ์ธ๊ธฐ ์ํ ์กฐํ

```python
import requests
from pprint import pprint

Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '652241f716c0f8b8f5006465a644f600',
    'language': 'en-en'
}

response = requests.get(Base_URL+path, params = params).json().get('results')

def ranking():
    ranking = []
    for i in response:
      ranking.append(i)
      rank = sorted(ranking, key = lambda r: r['vote_average'], reverse = True)
    return rank[0:5]

# ์๋์ ์ฝ๋๋ ์์ ํ์ง ์์ต๋๋ค.
if __name__ == '__main__':
    """
    popular ์ํ๋ชฉ๋ก์ ์ ๋ ฌํ์ฌ ํ์ ์์ผ๋ก 5๊ฐ ์ํ ๋ฐํ
    (์ฃผ์) popular ์ํ๋ชฉ๋ก์ ๊ฒฝ์ฐ ์๊ธฐ์ ๋ฐ๋ผ ์๋ ์์ ์ถ๋ ฅ๊ณผ ์ฐจ์ด๊ฐ ์์ ์ ์์
    """
    pprint(ranking())
```

- response๋ ์ต๊ทผ ์ธ๊ธฐ ๋ง์ ์ํ๋ค์ ์ ๋ณด์ด๋ค.
- ๊ทธ ์ ๋ณด๋ค์ `sorted` ํตํด ๋์ดํ ํ, [0:5]๋ฅผ ํด์ ํ์ ์ด ์ข์ 5๊ฐ์ ์ํ๋ค์ ๋ฐํ ํ๋ค



**`rank = sorted(ranking, key = lambda r: r['vote_average'], reverse = True)`**

- rank == ๋ณ์
- sorted == ๋ฎ์ ์ ๋ถํฐ ์ ๋ ฌํ๋ ๋ณ์ (์ค๋ฆ์ฐจ์)
- `ranking`์ ์ ๋ ฌํ๊ณ , `reverse = True` ๋ ๋ฐ๋๋ก ์ ๋ ฌ์ ํ๋ค
- `key = lambda r: r['vote_average']`
  - lambda๋ผ๋ ์ด๋ฆ ์๋ ํจ์๋ฅผ ๋ง๋ ๋ค
  - key ์ธ์์ ํจ์๋ฅผ ๋๊ฒจ์ฃผ๋ฉด ์ฐ์ ์์๊ฐ ์ ํด์ง๋ค
  - ์ด ์ฝ๋์ ๊ฒฝ์ฐ `['vote_average']`์ ์ซ์๋ค์ ๋น๊ตํด์ ์์๋ฅผ ์ ํด์ค๋ค



**`rank = sorted(ranking, key = lambda r: -r['vote_average'])`**

- `reverse = True` ๋์  `key = lambda r: -r['vote_average']` ์ฒ๋ผ `r`์ `-r` ๋ก ๋ฐ๊พธ๋ฉด ๋ด๋ฆผ์ฐจ์์ผ๋ก ๋ฐ๋๋ค



## 04. ์ํ ์กฐํ ๋ฐ ์ถ์ฒ ์ํ ์กฐํ

```python
import requests
from pprint import pprint

def recommendation(title):
    base_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'

    params = {
        'api_key' : '652241f716c0f8b8f5006465a644f600',
        'language': 'ko-KR',
        'query': f'{title}'      
        # query๊ฐ ํ์์ด๊ณ , title์ ๋ฃ์ผ๋ฉด ์ํ ์ ๋ชฉ์ ๊ฒ์ํ  ์ ์๋ค
        # recommendation(title) ํจ์๋ฅผ ๋ง๋  ํ ๊ดํธ ์์ ์ํ ์ ๋ชฉ์ ์๋ ฅํ๋ฉด ๋๋ค
    }
    
    # ๋ง์ง๋ง์ .get('results')๋ผ๊ณ  ํ๋ ๊ฒ์, response ์์ฒด๊ฐ ํ์ฌ List์ด๊ธฐ ๋๋ฌธ์ด๋ค
    # List์ ์๋ dict ์ค 'result' dictionary๋ฅผ ๊ฐ์ ธ์ค๋ ๊ฒ
    response = requests.get(base_URL + path, params = params).json().get('results')

    # response์ ์๋ฌด๊ฒ๋ ์์ผ๋ฉด None์ ๋ฐํํ๋ค
    if len(response) == 0:
        return None
    # response๋ ๋ฆฌ์คํธ, ์ฒซ๋ฒ์งธ ๋ฆฌ์คํธ element ์ค 'id'๋ผ๋ key์ value๋ฅผ ๊ฐ์ ธ์จ๋ค
    else:
        id = response[0]['id']

    # f-string์ ์ ์ฐ๋ฉด ์์์ ์ฐพ์ id์ ์ฐ๊ฒฐ์ด ์ ๋๋ค
    path = f'/movie/{id}/recommendations'

    response = requests.get(base_URL + path, params = params).json().get('results')

    result = []
    for i in response:
        result.append(i['title'])

    return result


# ์๋์ ์ฝ๋๋ ์์ ํ์ง ์์ต๋๋ค.
if __name__ == '__main__':
#     """
#     ์ ๋ชฉ์ ํด๋นํ๋ ์ํ๊ฐ ์์ผ๋ฉด ํด๋น ์ํ์ id๋ฅผ ๊ธฐ๋ฐ์ผ๋ก ์ถ์ฒ ์ํ ๋ชฉ๋ก ๊ตฌ์ฑ
#     ์ถ์ฒ ์ํ๊ฐ ์์ ๊ฒฝ์ฐ []๋ฅผ ๋ฐํ
#     ์ํ id ๊ฒ์์ ์คํจํ  ๊ฒฝ์ฐ None์ ๋ฐํ
#     (์ฃผ์) ์ถ์ฒ ์ํ์ ๊ฒฝ์ฐ ์๋ ์์ ์ถ๋ ฅ๊ณผ ์ฐจ์ด๊ฐ ์์ ์ ์์
#     """
    pprint(recommendation('๊ธฐ์์ถฉ'))
#     # ['์กฐ์ปค', '1917', '์กฐ์กฐ ๋๋น', ..์๋ต.., '์ด์ธ์ ์ถ์ต', 'ํํ ํฝ์']
    pprint(recommendation('๊ทธ๋๋นํฐ'))
#     # []
    pprint(recommendation('๊ฒ์ํ  ์ ์๋ ์ํ'))
    # None
```

- **path** ์์ ๋ฃ๋ ์ ๋ณด๊ฐ, ๊ทธ ์ ์ ์ฐพ์ ์ ๋ณด์ ์ผ์นํ๋์ง ํ์ธํ๋ฉด์ ์งํ!!!



## 05. ์ถ์ฐ์ง ๋ฐ ์ฐ์ถ์ง ๋ฐ์ดํฐ ์กฐํ

```python
import requests
from pprint import pprint


def credits(title):

    # ์ํ ์ ๋ชฉ์ ํตํด ์ํ ID ๊ฐ์ ธ์ค๊ธฐ
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '652241f716c0f8b8f5006465a644f600',
        'language': 'ko-KR',
        'query' : title
    }

    response = requests.get(base_url + path, params = params).json().get('results')

    if len(response) == 0:
        return None
    else:
        id = response[0]['id']

    # ์ฌ๊ธฐ์๋ถํฐ๋ ์ํ credits ๊ด๋ จ
    path = f'/movie/{id}/credits'
    
    response = requests.get(base_url + path, params = params).json()
    
    # response_cast (ํ์: ๋ฆฌ์คํธ)๋ฅผ 'i' ๋์๋๋ฆฌ๋ก ๋ง๋  ํ,
    # ๋์๋๋ฆฌ ์์ ์๋ key ์ค 'cast_id'์ value๋ฅผ ์ฐพ๊ณ 
    # ๊ทธ value๊ฐ 10๋ฏธ๋ง์ด๋ฉด
    # 'cast', ๋ฆฌ์คํธ ๋ณ์ ์์ ๋ฐฐ์ฐ ์ด๋ฆ 'name' ๋ค์ ๋ฃ์๋ค.
    cast = []
    response_cast = response.get('cast')

    for i in response_cast:
        if i['cast_id'] < 10:
            cast.append(i['name'])
    
    # response_crew (ํ์: ๋ฆฌ์คํธ)๋ฅผ 'i' ๋์๋๋ฆฌ๋ก ๋ง๋  ํ,
    # ๋์๋๋ฆฌ ์์ ์๋ key ์ค 'department'์ value๋ฅผ ์ฐพ๊ณ 
    # ๋ฌธ์์ด์ด ('Directing') ๋์ผํ๋ฉด 
    # 'crew', ๋ฆฌ์คํธ ๋ณ์ ์์ ์ฐ์ถ์ง ์ด๋ฆ 'name' ๋ค์ ๋ฃ์๋ค.
    crew = []
    response_crew = response.get('crew')
    for i in response_crew:
        if i['department'] == 'Directing':
            crew.append(i['name'])

    return {
        'cast': cast,
        'crew': crew
    }


# ์๋์ ์ฝ๋๋ ์์ ํ์ง ์์ต๋๋ค.
if __name__ == '__main__':
    """
    ์ ๋ชฉ์ ํด๋นํ๋ ์ํ๊ฐ ์์ผ๋ฉด ํด๋น ์ํ id๋ฅผ ํตํด ์ํ ์์ธ์ ๋ณด๋ฅผ ๊ฒ์ํ์ฌ ์ฃผ์ฐ๋ฐฐ์ฐ ๋ชฉ๋ก(cast)๊ณผ ์คํํ(crew) ์ค ์ฐ์ถ์ง ๋ชฉ๋ก์ ๋ฐํ
    ์ํ id ๊ฒ์์ ์คํจํ  ๊ฒฝ์ฐ None์ ๋ฐํ
    """
    pprint(credits('๊ธฐ์์ถฉ'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    # pprint(credits('๊ฒ์ํ  ์ ์๋ ์ํ'))
    # None

```

