# ๐ Project 1

[00. ํ์คํธ ๋ฐ์ดํฐ ์ถ๋ ฅ (์ฐ์ต)](#00-ํ์คํธ-๋ฐ์ดํฐ-์ถ๋ ฅ-์ฐ์ต)

[01. ํ์คํธ ๋ฐ์ดํฐ ์๋ ฅ (์ฐ์ต)](#01-ํ์คํธ-๋ฐ์ดํฐ-์๋ ฅ-์ฐ์ต)

[02. ํ์คํธ ๋ฐ์ดํฐ ํ์ฉ - ํน์  ๋จ์ด ์ถ์ถ](#02-ํ์คํธ-๋ฐ์ดํฐ-ํ์ฉ---ํน์ -๋จ์ด-์ถ์ถ)

[03. ํ์คํธ ๋ฐ์ดํฐ ํ์ฉ - ๋ฑ์ฅ ํ์](#03-ํ์คํธ-๋ฐ์ดํฐ-ํ์ฉ---๋ฑ์ฅ-ํ์)

[04. JSON ๋ฐ์ดํฐ ํ์ฉ - ์ํ ๋จ์ผ ์ ๋ณด](#04-json-๋ฐ์ดํฐ-ํ์ฉ---์ํ-๋จ์ผ-์ ๋ณด)

[05. JSON ๋ฐ์ดํฐ ํ์ฉ - ์ํ ๋จ์ผ ์ ๋ณด ์์ฉ](#05-json-๋ฐ์ดํฐ-ํ์ฉ---์ํ-๋จ์ผ-์ ๋ณด-์์ฉ)

[06. JSON ๋ฐ์ดํฐ ํ์ฉ - ์ํ ๋ค์ค ์ ๋ณด ํ์ฉ](#06-json-๋ฐ์ดํฐ-ํ์ฉ---์ํ-๋ค์ค-์ ๋ณด-ํ์ฉ)



## โ๏ธ ํ์ด์ฌ ๊ธฐ๋ฐ ๋ฐ์ดํฐ ํ์ฉ

### ๋ชฉํ

- Python ๊ธฐ๋ณธ ๋ฌธ๋ฒ(์กฐ๊ฑด๋ฌธ, ๋ฐ๋ณต๋ฌธ) ํ์ฉ
- ํ์ผ ์์ถ๋ ฅ์ ํตํ ๋ฐ์ดํฐ ํ์ฉ
- ํ์คํธ ๋ฐ JSON ๋ฐ์ดํฐ์ ํ์ฉ



## 00. ํ์คํธ ๋ฐ์ดํฐ ์ถ๋ ฅ (์ฐ์ต)

```python
with open('text.txt', 'w', encoding='utf-8') as f:
# with open์ ํตํด์ 'text.txt'๋ฅผ ๋ง๋ ๋ค. 
# ์ฌ๊ธฐ์ 'w'๋ write์ ์ค์๋ง, ์ฐ๊ธฐ ๋ชจ๋
    
    f.write('2ํ์ฐจ ์ด์ ์ค\nHello, Python!\n')
    for i in range(1,6):					# range(1,6)๋ 1์ด์ 6๋ฏธ๋ง
        f.write(f'{i}์ผ์ฐจ ํ์ด์ฌ ๊ณต๋ถ ์ค\n')

# f.write๋ 'text.txt'์ ์ด๋ค ๋ด์ฉ์ด ์ฐ์ฌ์ผ ํ ์ง ๋ช๋ นํ๋ค. print()์ ๋น์ทํ๋ค๊ณ  ํด์ผํ๋
```

- `f-string`์ ๋ฌธ์์ด ๊ฐ์ฅ ์์ `f`๋ฅผ ๋ถ์ฌ์ฃผ๊ณ , `{}`์ ์ด๋ค ๊ฐ์ `{}`์ด ์์นํ ์๋ฆฌ์ ํํํ ์ง ์ ์ด๋๋ฉด ๋๋ค
  - ๋ฌธ์์ด ์์ ๋ณ์๋ฅผ ๋ฃ์ด ์ค๋ค!!!



## 01. ํ์คํธ ๋ฐ์ดํฐ ์๋ ฅ (์ฐ์ต)

```python
with open('fruits.txt', 'r', encoding = 'utf-8') as f:
# 'r'์ read, ์ฝ๊ธฐ ์ ์ฉ
	fruits = f.read()			# f.read()๋ ํ์ผ์ ๋ด์ฉ ์ ์ฒด๋ฅผ ๋ฌธ์์ด๋ก ๋ฐํ
	list = fruits.split('\n')	# .split() ํตํด ๋ฌธ์์ด์ ๋ฆฌ์คํธ๋ก ๋ฐํ

cnt = 0
for i in list:
    cnt += 1
print(cnt)

with open('01.txt', 'w', encoding = 'utf-8')as f:
    f.write(f'{cnt}')
```





## 02. ํ์คํธ ๋ฐ์ดํฐ ํ์ฉ - ํน์  ๋จ์ด ์ถ์ถ

```python
with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read().split('\n')

cnt = 0
berry_list = []
final_list = []

for i in fruits:
    if i.endswith('berry'):
        berry_list.append(i)            # berry๋ก ๋๋๋ ๋จ์ด๋ฅผ berry_list์ ์ถ๊ฐํ๋ค
    for result in berry_list:           # berry_list์ ์๋ ๋จ์ด๋ฅผ ํ๋์ฉ ๊บผ๋
        if result not in final_list:    # final_list์ result์ ๋๊ฐ์ ๊ฐ์ด ์์ผ๋ฉด,
            cnt += 1
            final_list.append(i)        # final_list์ ๋จ์ด๋ฅผ ๋ฃ๋๋ค

list = '\n'.join(final_list)			# ๋ฆฌ์คํธ๋ฅผ ํ์ค์ฉ str์ผ๋ก ๋ฐํ

print(cnt)
print(list)

# '02.txt'๋ผ๋ ์ฐ๊ธฐ ๋ชจ๋์ ํ์ผ์ ๋ง๋ค์ด, ์์ ์ถ๋ ฅ๋ ๊ฒฐ๊ณผ๋ฅผ ๋ฃ์ด์ค๋ค
with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{cnt}\n{list}')
```

- `.startswith` ~๋ก ์์ํ๋ / `.endswith` ~๋ก ๋๋๋
- `' '.join()` ๋ฆฌ์คํธ๋ฅผ ๋ฌธ์์ด๋ก ๋ฐํ



## 03. ํ์คํธ ๋ฐ์ดํฐ ํ์ฉ - ๋ฑ์ฅ ํ์

```python
with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read().split('\n')

    dict = {}

for i in fruits:
    if i in dict:
        dict[i] += 1               # ์ด๋ฏธ 'i'๊ฐ 'dict'์ ์กด์ฌํ๋ฉด ๊ฐ์ 1์ ๋ํด์ค๋ค
    else:
        dict[i] = 1

for x, y in dict.items():     # .item()์ ์ฌ์ฉํ์ฌ dictionary์ key์ value๋ฅผ ์ถ๋ ฅํ  ์ ์๋ค
    print(x, y)


with open('03.txt', 'w', encoding='utf-8') as f:
    for x, y in dict.items():    
        f.write(f'{x} {y}\n')   # print ๋์  f.write๋ฅผ f-string์ ์ฌ์ฉํด์ ๋ฌธ์์ด ์์ ๋ณ์๋ฅผ ๋ฃ์ด ์ค๋ค
```





## 04. JSON ๋ฐ์ดํฐ ํ์ฉ - ์ํ ๋จ์ผ ์ ๋ณด

```python
import json
from pprint import pprint


def movie_info(movie):
    return {                                        # return์ ํตํด output์ ์ ํ๋ค
        'genre_ids': movie.get('genre_ids'),
        'id': movie.get('id'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview')
    }


# ์๋์ ์ฝ๋๋ ์์ ํ์ง ์์ต๋๋ค.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))
```





## 05. JSON ๋ฐ์ดํฐ ํ์ฉ - ์ํ ๋จ์ผ ์ ๋ณด ์์ฉ

```python
def movie_info(movie, genres):
    list = movie.get('genre_ids')       
    genre_names = []                    


    for i in list:                     
        for names in genres_list:    
            if names['id'] == i:        
                genre_names.append(names['name'])   
    return{
        'id': movie.get('id'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_names': genre_names
    }
```

![project 1-5](project_1.assets/project 1-5.png)

1. `list` ๋ผ๋ ๋ณ์ ์์ฑ. ('genre_ids'๊ฐ ๋ฆฌ์คํธ ํ์์ผ๋ก ์กด์ฌ)
2. `genre_names`๋ผ๋ ๋ฆฌ์คํธ ์์ฑ
3. 'movie.json'์ ์๋ `genre_ids` ์์ ๋ฆฌ์คํธ๋ก ์กด์ฌํ๋ [18, 80]์ `int`๋ก ๋ฐํํ๋ค (List โ int)
4. <type 'list'>ํํ์์, <type 'dict'>๋ก ๋ฐํ. `names`๊ฐ `genre-list`๋ฅผ ์ํํ๋ฉด์, ๋ฆฌ์คํธ ์์ ์๋ ๋์๋๋ฆฌ๋ค์ ๋ฐํ
5. `names`์ key ์ค, 'id'์ value๋ฅผ ๊ฐ์ ธ์ค๊ณ , ๊ทธ value๊ฐ `i` (18 80)๊ณผ ๊ฐ์ผ๋ฉด
6. `genre_names`๋ผ๋ ๋ฆฌ์คํธ ์์ `names`์ key ์ค, 'name'์ value๋ฅผ `.append`๋ฅผ ํตํด ์ถ๊ฐํ๋ค



## 06. JSON ๋ฐ์ดํฐ ํ์ฉ - ์ํ ๋ค์ค ์ ๋ณด ํ์ฉ

```python
import json
from pprint import pprint


def movie_info(movies, genres):
    
    info = []
    
    for dict in movies:
        first = {
            'id': dict.get('id'),
            'title': dict.get('title'),
            'vote_average': dict.get('vote_average'),
            'overview': dict.get('overview')
        }

        genre_names = []
        for ids in dict['genre_ids']:
            for id in genres:
                if id['id'] == ids:
                    genre_names.append(id['name'])

        first['genre_names'] = genre_names              

        info.append(first)

    return info
    


        
# ์๋์ ์ฝ๋๋ ์์ ํ์ง ์์ต๋๋ค.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```

![project 1-6](project_1.assets/project 1-6.jpg)

1. `movies`๋ฅผ list ํ์์์ dict ํ์์ผ๋ก ๋ฐํ
2. ๋ฐํ๋ ๋์๋๋ฆฌ ์ค , `id`, `title`, `overview`, `vote-average`๋ฅผ key๋ก, ํด๋น ๊ฐ๋ค์ `.get`์ ํตํด `dict`์์ ๊ฐ์ง๊ณ  ์จ๋ค
3. `ids`๋ `dict` ์์ ๋ฆฌ์คํธ ํ์์ผ๋ก ์กด์ฌํ๋ `'genre_ids'`๋ฅผ `int`๋ก ๋ฐํ
4. `genre`๋ฅผ listํ์์์ dict ํ์์ผ๋ก ๋ฐํ
5. ๋ง์ฝ `genres`ํ์ผ ์์ ์๋ `id` (key)์ ๊ฐ์ด, `ids`์ ๋์ผํ๋ฉด
6. `genre_names`๋ผ๋ ๋ฆฌ์คํธ์ `genres` ํ์ผ์ ์กด์ฌํ๋ `name` (key)์ ๊ฐ์ ์ถ๊ฐํ๋ค
7. ๊ตฌํ ๋ชจ๋  20๊ฐ์ ๋์๋๋ฆฌ(`first`)๋ค์ `info` (list)์ ๋ฃ์ด์ค๋ค
