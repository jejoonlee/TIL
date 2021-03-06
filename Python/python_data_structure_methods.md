# ๐Python Methods

[Review](#%EF%B8%8F-review)

[Methods](#%EF%B8%8F-Methods-๋ฉ์๋)

[์ํ์ค](#%EF%B8%8F-์ํ์ค)

- [๋ฌธ์์ด (String Type)](#๋ฌธ์์ด-string-type)
  - [๋ฌธ์์ด ํ์, ๊ฒ์ฆ](#๋ฌธ์์ด-ํ์-๊ฒ์ฆ)
  - [๋ฌธ์์ด ๋ณ๊ฒฝ](#๋ฌธ์์ด-๋ณ๊ฒฝ)
- [๋ฆฌ์คํธ (List)](#๋ฆฌ์คํธ-list)

[์ปฌ๋ ์](#%EF%B8%8F-์ปฌ๋ ์)

- [์ธํธ](#์ธํธ)
- [๋์๋๋ฆฌ (Dictionary)](#๋์๋๋ฆฌ-dictionary)



## โ๏ธReview

> ๋ณ์์ ํ์
>
> `int`, `float`, `complex`, `bool`
>
> `str`, `list`, `tuple`, `range`
>
> `set`, `dictionary`



## โ๏ธ Methods (๋ฉ์๋)

> Methods (๋ฉ์๋)๋ ์ผ์ข์ ํจ์

![methods1](python_data_structure_methods.assets/methods1-16577811908851.png)

![methods2](python_data_structure_methods.assets/methods2.png)



## โ๏ธ ์ํ์ค



### ๋ฌธ์์ด (String Type)

- #### ๋ฌธ์์ด ํ์, ๊ฒ์ฆ

| ๋ฌธ๋ฒ          | ์ค๋ช                                                         |
| ------------- | ------------------------------------------------------------ |
| **.find(x)**  | x์ ์ฒซ ๋ฒ์งธ ์์น๋ฅผ ๋ฐํ. ์์ผ๋ฉด, - 1์ ๋ฐํ                  |
| **.index(x)** | x์ ์ฒซ ๋ฒ์งธ ์์น๋ฅผ ๋ฐํ. ์์ผ๋ฉด, ์ค๋ฅ ๋ฐ์                   |
| .isalpha()    | is alphabet (์ํ๋ฒณ์ผ๋ก ์ด๋ฃจ์ด์ ธ์๋?) / True or False       |
| .isupper()    | is upper (๋ชจ๋ ๋๋ฌธ์์ธ๊ฐ?) / True or False                  |
| .islower      | is lower (๋ชจ๋ ์๋ฌธ์์ธ๊ฐ?) / True or False                  |
| .istitle      | is title (์ ๋ชฉ์ฒ๋ผ, ์์ ๋ฌธ์๊ฐ ๋๋ฌธ์์ธ๊ฐ?) / True or False |

**.find(x)**

```python
print('apple'.find('p'))		# 1
print('apple'.find('k'))		# -1
```

**.index**

```python
print('apple'.find('p'))		# 1
print('apple'.find('k'))		# ValueError ....
```



- #### ๋ฌธ์์ด ๋ณ๊ฒฝ

| **๋ฌธ๋ฒ**                              | **์ค๋ช**                                                     |
| ------------------------------------- | ------------------------------------------------------------ |
| **.replace(old, new [, count])**      | **๋ฐ๊ฟ ๋์ ๊ธ์๋ฅผ ์๋ก์ด ๊ธ์๋ก ๋ฐ๊ฟ์ ๋ฐํ**               |
| **.strip([chars])**                   | **๊ณต๋ฐฑ์ด๋ ํน์  ๋ฌธ์๋ฅผ ์ ๊ฑฐ**                                |
| **.split(sep = None, maxsplit = -1)** | ๊ณต๋ฐฑ์ด๋ ํน์  ๋ฌธ์๋ฅผ ๊ธฐ์ค์ผ๋ก ๋ถ๋ฆฌ                           |
| **'seperator'.join([iterable])**      | ๋ฆฌ์คํธ์ ์๋ ์์ ํ๋ํ๋๋ฅผ ํฉ์ณ์ ํ๋์ ๋ฌธ์์ด๋ก ๋ฐ๊พธ์ด ๋ฐํ |
| .capitalize()                         | ๊ฐ์ฅ ์ฒซ ๋ฒ์งธ ๊ธ์๋ฅผ ๋๋ฌธ์๋ก ๋ณ๊ฒฝ                            |
| .title()                              | '๋ ๊ณต๋ฐฑ ์ดํ ๋๋ฌธ์๋ก ๋ณ๊ฒฝ                                  |
| .upper()                              | ๋ชจ๋ ๋๋ฌธ์๋ก ๋ณ๊ฒฝ                                           |
| .lower()                              | ๋ชจ๋ ์๋ฌธ์๋ก ๋ณ๊ฒฝ                                           |
| .swapcase                             | ๋ โ ์๋ฌธ์ ์๋ก ๋ณ๊ฒฝ                                        |

**.replace(old, new [, count])**

```python
print('manchesterunited'.replace('t' , 'z'))
# mancheszerunized
print('weeeeeheee'.replace('e' , '@' , 4))
# w@@@@ehee			count๋ฅผ ์ง์ ํ์ฌ, ํด๋น ๊ฐฏ์๋งํผ๋ง ์ํ
```

**.strip([chars])**

- ํน์ ํ ๋ฌธ์๋ค์ ์ง์ ํ๋ฉด ์ฃผ๋ณ ๊ณต๋ฐฑ ์ ๊ฑฐ
- ์์ชฝ์ผ๋ก ์ ๊ฑฐํ๊ฑฐ๋ (strip),  ์ผ์ชฝ์ ์ ๊ฑฐํ๊ฑฐ๋ (lstrip), ์ค๋ฅธ์ชฝ์ ์ ๊ฑฐ(rstrip)

```python
print('     ๋จ๋๋ถ๋ถ\n'.strip())				# '๋จ๋๋ถ๋ถ'
print('     ๋จ๋๋ถ๋ถ\n'.lstrip())				# '๋จ๋๋ถ๋ถ\n'
print('     ๋จ๋๋ถ๋ถ\n'.rstrip())				# '     ๋จ๋๋ถ๋ถ'
print('     ๋จ๋๋ถ๋ถ!!!!!!'.rstrip('!'))		# '     ๋จ๋๋ถ๋ถ'
```

**.split(sep=None, maxsplit=-1)**

- ๋ฌธ์์ด์ ํน์ ํ ๋จ์๋ก ๋๋  ๋ฆฌ์คํธ๋ก ๋ฐํ
  - maxsplit์ด -1์ธ ๊ฒฝ์ฐ์๋ ์ ํ์ด ์์

```python
print('a,b,c'.split('_'))
# ['a,b,c']
print('a,b,c'.split())
# ['a', 'b', 'c']
```

**'seperator'.join([iterable])**

- ๋ฐ๋ณต๊ฐ๋ฅํ (iterable) ์ปจํ์ด๋ ์์๋ค์ seperator(๊ตฌ๋ถ์)๋ก ํฉ์ณ **๋ฌธ์์ด ๋ฐํ**
  - iterable์ ๋ฌธ์์ด์ด ์๋ ๊ฐ์ด ์์ผ๋ฉด TypeError ๋ฐ์

```python
print(''.join(['3', '5']))
# 35
```



๊ธฐํ

```python
msg = 'hI! Everyone.'

print(msg)						# hI! Everyone.
print(msg.capitalize())			# Hi! everyone.
print(msg.title())				# Hi! Everyone.
print(msg.upper())				# HI! EVERYONE.
print(msg.lower())				# hi! everyone.
print(msg.swapcase())			# Hi! eVERYONE.
```





### ๋ฆฌ์คํธ (List)

| ๋ฌธ๋ฒ                      | ์ค๋ช                                                         |
| ------------------------- | ------------------------------------------------------------ |
| **.append(x)**            | ๋ฆฌ์คํธ ๋ง์ง๋ง ํญ๋ชฉ์ x ์ถ๊ฐ                                  |
| **.insert(i,x)**          | ๋ฆฌ์คํธ ์ธ๋ฑ์ค i์ ํญ๋ชฉ x ์ฝ์                                |
| **.remove(x)**            | ๋ฆฌ์คํธ ๊ฐ์ฅ ์ผ์ชฝ์ ์๋  ํญ๋ชฉ (์ฒซ๋ฒ์งธ) x๋ฅผ ์ ๊ฑฐ. ํญ๋ชฉ์ด ์กด์ฌํ์ง ์์ ๊ฒฝ, ValueError |
| **.pop()**                | ๋ฆฌ์คํธ ๊ฐ์ฅ ๋ง์ง๋ง์ ์๋ ํญ๋ณต ๋ฐํ ํ ์ ๊ฑฐ                  |
| **.pop(i)**               | ๋ฆฌ์คํธ์ ์ธ๋ฑ์ค i์ ์๋ ํญ๋ชฉ์ ๋ฐํ ํ ์ ๊ฑฐ                 |
| **.clear()**              | ๋ชจ๋  ํญ๋ชฉ์ ์ญ์                                              |
| .extend(m)                | ์ํํ m์ ๋ชจ๋  ํญ๋ชฉ๋ค์ ๋ฆฌ์คํธ ๋์ ์ถ๊ณผ (+=๊ณผ ๊ฐ์ ๊ธฐ๋ฅ)   |
| **.index(x, start, end)** | ๋ฆฌ์คํธ์ ์๋ ํญ๋ชฉ ์ค ๊ฐ์ฅ ์ผ์ชฝ์ ์๋ ํญ๋ชฉ x์ ์ธ๋ฑ์ค๋ฅผ ๋ฐํ |
| **.reverse()**            | ๋ฆฌ์คํธ๋ฅผ ๊ฑฐ๊พธ๋ก ์ ๋ ฌ                                         |
| **.sort()**               | ๋ฆฌ์คํธ๋ฅผ ์ ๋ ฌ                                                |
| **.count(x)**             | ๋ฆฌ์คํธ์์ ํญ๋ชฉ x๊ฐ ๋ช ๊ฐ ์กด์ฌํ๋์ง ๊ฐฏ์๋ฅผ ๋ฐํ             |



**.append(x)**

```python
football = ['manchesterunited', 'suwonbluewings', 'daegufc']
football.append('houstonrockets')

print(football)
# ['manchesterunited', 'suwonbluewings', 'daegufc', 'houstonrockets']
```

**.extend(iterable)**

```python
football = ['manchesterunited', 'suwonbluewings', 'daegufc']
football.extend(['suwonfc', 'realmadrid'])

print(football)
# ['manchesterunited', 'suwonbluewings', 'daegufc', 'suwonfc', 'realmadrid']
```

**.insert(i, x)**

- i ๊ฐ์ด ๋ฆฌ์คํธ ๊ธธ์ด๋ณด๋ค ํฐ ๊ฒฝ์ฐ, ๋งจ ๋ค๋ก ์ฝ์๋๋ค

```python
football = ['manchesterunited', 'suwonbluewings', 'daegufc']
football.insert(1, 'realmadrid')
print(football)
# ['manchesterunited', 'realmadrid', 'suwonbluewings', 'daegufc']

football.insert(10000, 'end')
print(football)
# ['manchesterunited', 'realmadrid', 'suwonbluewings', 'daegufc', 'end']
```

**.remove(x)**

```python
football = ['manchesterunited', 'suwonbluewings', 'liverpool']
football.remove('liverpool')

print(football)
# ['manchesterunited', 'suwonbluewings']

football.remove('liverpool')
# ์ด๋ฏธ ์ง์ด ์ํ๋ผ์, ValueError ๊ฐ ๋ฌ๋ค
```

**.pop(i)**

- index๋ฅผ ์ง์ ํ๋ฉด, ํด๋น ๊ฐ์ ์ญ์ ๋๊ณ , ๊ทธ ํญ๋ชฉ์ ๋ฐํํ๋ค
  - i๊ฐ ์ง์ ๋์ง ์์ผ๋ฉด, ๋งจ ๋ง์ง๋ง์ ์ญ์ ํ๊ณ  ๋ฐํํ๋ค

```python
football = ['manchesterunited', 'suwonbluewings', 'liverpool', 'FCSeoul']
pop_football = football.pop(2)
print(pop_football)		# 'liverpool'
print(football)			# ['manchesterunited', 'suwonbluewings', 'FCSeoul']

pop_football = football.pop()		# ๋งจ ๋ง์ง๋ง ๊ฐ์ ์ญ์ 
print(pop_football)		# 'FCSeoul'
print(football)			# ['manchesterunited', 'suwonbluewings']
```

**.clear()**

```python
football = ['manchesterunited', 'suwonbluewings', 'liverpool', 'FCSeoul']
print(football.clear()) # ๋ชจ๋  ํญ๋ชฉ์ ์ญ์ ํ๋ค
# []	๋ชจ๋  ํญ๋ชฉ ์ ๊ฑฐ
```

**.index(x)**

- x๊ฐ์ ์ฐพ์ ํด๋น index ๊ฐ์ ๋ฐํ

```python
football = ['manchesterunited', 'suwonbluewings', 'daegufc', 'realmadrid']
print(football.index('manchesterunited'))
# 0
print(football.index('google'))
# 'google'์ ์์ผ๋ฏ๋ก ValueError๊ฐ ๋ฌ๋ค
```

**.count(x)**

- ์ํ๋ ๊ฐ์ ๊ฐ์๋ฅผ ๋ฐํํจ

```python
number = [1, 1, 2, 3, 3, 4, 1, 1]
print(number.count(1))
# 4
print(number.count(7))
# 0
```

**.sort()**

- ์๋ณธ ๋ฆฌ์คํธ๋ฅผ ์ ๋ ฌํ๋ค. None ๋ฐํ
- sorted ํจ์์ ๋น๊ตํ  ๊ฒ

```python
number = [1, 7, 3, 2, 6]
result = number.sort()
print(number, result)
# [1, 2, 3, 6, 7] None
print(number.sort())
# None
-------------------------------------------------------------------------
number = [1, 7, 3, 2, 6]
result = sorted(number)
print(number, result)
# [1, 7, 3, 2, 6] [1, 2, 3, 6, 7]
   # ์ ๋ ฌ๋ ๋ฆฌ์คํธ๋ฅผ ๋ฐํ. ์๋ณธ ๋ณ๊ฒฝ ์์
```

**.reverse**

```python
number = [1, 7, 3, 2, 6]
result = number.reverse()
print(number, result)
# [6, 2, 3, 7, 1] None
๋ฆฌ์คํธ์ ์์๋ฅผ ๋ฐ๊พธ๋ ๊ฒ์ด์ง, ์ ๋ ฌํ๋ ๊ฒ์ด ์๋. None์ผ๋ก ๋ฐํ
```





## โ๏ธ ์ปฌ๋ ์



### ์ธํธ

| ๋ฌธ๋ฒ           | ์ค๋ช                                                         |
| -------------- | ------------------------------------------------------------ |
| .copy()        | ์ธํธ์ ์์ ๋ณต์ฌ๋ณธ์ ๋ฐํ                                    |
| .add(x)        | ํญ๋ชฉ x๊ฐ ์ธํธ์ ์๋ค๋ฉด ์ถ๊ฐ                                  |
| .pop()         | ์ธํธ s์์ ๋๋คํ๊ฒ ํญ๋ชฉ์ ๋ฐํํ๊ณ , ํด๋น ํญ๋ชฉ์ ์ ๊ณ . ์ธํธ๊ฐ ๋น์ด์์ ๊ฒฝ์ฐ, KeyError |
| .remove(s)     | ํญ๋ชฉ x๋ฅผ ์ธํธ s์์ ์ญ์ . ํญ๋ชฉ์ด ์กด์ฌํ์ง ์์ ๊ฒฝ์ฐ, KeyError |
| .discard(x)    | ํญ๋ชฉ x๊ฐ ์ธํธ s์ ์๋ ๊ฒฝ์ฐ, ํญ๋ชฉ x๋ฅผ ์ธํธ s์์ ์ญ์         |
| .update(t)     | ์ธํธ t์ ์๋ ๋ชจ๋  ํญ๋ชฉ ์ค ์ธํธ s์ ์๋ ํญ๋ชฉ์ ์ถ๊ฐ         |
| .clear()       | ๋ชจ๋  ํญ๋ชฉ์ ์ ๊ฑฐ                                             |
| .isdisjoint(t) | ์ธํธ s๊ฐ ์ธํธ t์ ์๋ก ๊ฐ์ ํญ๋ชฉ์ ํ๋๋ผ๋ ๊ฐ๊ณ  ์์ง ์์ ๊ฒฝ์ฐ, True ๋ฐํ |
| .issubset(t)   | ์ธํธ s๊ฐ ์ธํธ  t์ ํ์ ์ธํธ์ธ ๊ฒฝ์ฐ, True ๋ฐํ               |
| .issuperset(t) | ์ธํธ s๊ฐ ์ธํธ t์ ์์ ์ธํธ์ธ ๊ฒฝ์ฐ, True ๋ฐํ                |





### ๋์๋๋ฆฌ (Dictionary)

| ๋ฌธ๋ฒ                 | ์ค๋ช                                                         |
| -------------------- | ------------------------------------------------------------ |
| .clear()             | ๋ชจ๋  ํญ๋ชฉ ์ ๊ฑฐ                                               |
| .keys()              | ๋์๋๋ฆฌ ๋ชจ๋  ํค๋ฅผ ๋ด์ ๋ทฐ๋ฅผ ๋ฐํ                            |
| .values()            | ๋์๋๋ฆฌ ๋ชจ๋  ๊ฐ์ ๋ด์ ๋ทฐ๋ฅผ ๋ฐํ                            |
| .items()             | ๋์๋๋ฆฌ ๋ชจ๋  ํค-๊ฐ์ ์์ ๋ด์ ๋ทฐ๋ฅผ ๋ฐํ                    |
| **.get(k)**          | ํค key์ ๊ฐ์ ๋ฐํํ๋๋ฐ, ํค key๊ฐ ๋์๋๋ฆฌ์ ์์ ๊ฒฝ์ฐ None์ ๋ฐํ |
| **.get(k, v)**       | ํค key์ ๊ฐ์ ๋ฐํํ๋๋ฐ, ํค key๊ฐ ๋์๋๋ฆฌ์ ์์ ๊ฒฝ์ฐ value๋ฅผ ๋ฐํ |
| **.pop(k)**          | ํค key์ ๊ฐ์ ๋ฐํํ๊ณ  ํค key์ธ ํญ๋ชฉใ๋ฅด ๋์๋๋ฆฌ์์ ์ญ์ ํ๋๋ฐ, ํค key๊ฐ ๋์๋๋ฆฌ์ ์์ ๊ฒฝ์ฐ KeyError๋ฅผ ๋ฐ์ |
| **.pop(k, v)**       | ํค k์ ๊ฐ์ ๋ฐํํ๊ณ  ํค key์ธ ํญ๋ชฉ์ ๋์๋๋ฆฌ์์ ์ญ์ ํ๋๋ฐ, ํค key๊ฐ ๋์๋๋ฆฌ์ ์์ ๊ฒฝ์ฐ value๋ฅผ ๋ฐํ |
| **.update([other])** | ๋์๋๋ฆฌ์ ๊ฐ์ ๋งคํํ์ฌ ์๋ฐ์ดํธ                            |



**.get(key[, default])**

- key๋ฅผ ํตํด value๋ฅผ ๊ฐ์ ธ์จ๋ค
- KeyError๊ฐ ๋ฐ์ํ์ง ์์ผ๋ฉฐ, default๊ฐ์ ์ค์ ํ  ์ ์์ (๊ธฐ๋ณธ, None)

```python
my_dict = {'football': '์ถ๊ตฌ', 'basketball': '๋๊ตฌ'}
my_dict['rugby']	# my_dict์ 'rugby'๋ผ๋ key๊ฐ ์์ด์, KeyError๊ฐ ๋ฌ๋ค

my_dict = {'football': '์ถ๊ตฌ', 'basketball': '๋๊ตฌ'}
print(my_dict.get('rugby'))					# None
print(my_dict.get('football'))				# ์ถ๊ตฌ
print(my_dict.get('rugby', 0))				# 0
print(my_dict.get('football', 0))			# ์ถ๊ตฌ
```

**.pop(key[, default])**

- key๊ฐ ๋์๋๋ฆฌ์ ์์ผ๋ฉด ์ ๊ฑฐํ๊ณ  ํด๋น ๊ฐ์ ๋ฐํ
- ๊ทธ๋ ์ง ์์ผ๋ฉด default๋ฅผ ๋ฐํ / default ๊ฐ์ด ์์ผ๋ฉด KeyError

```python
my_dict = {'football': '์ถ๊ตฌ', 'basketball': '๋๊ตฌ'}
data = my_dict.pop('basketball')
print(data, my_dict)				# ๋๊ตฌ {'football': '์ถ๊ตฌ'}
--------------------------------------------------------------------------------

my_dict = {'football': '์ถ๊ตฌ', 'basketball': '๋๊ตฌ'}
data = my_dict.pop('rugby')
print(data, my_dict)				# KeyError {'football': '์ถ๊ตฌ', 'basketball': '๋๊ตฌ'}

--------------------------------------------------------------------------------
my_dict = {'football': '์ถ๊ตฌ', 'basketball': '๋๊ตฌ'}
data = my_dict.pop('rugby', '์์')
print(data, my_dict)				# ์์ {'football': '์ถ๊ตฌ', 'basketball': '๋๊ตฌ'}
```

**.update([other])**

- ๊ฐ์ ์ ๊ณตํ๋ key, value๋ก ๋ฎ์ด์ด๋ค

```python
my_dict = {'football': '์ถ', 'basketball': '๋๊ตฌ'}
my_dict.update('football' = '์ถ๊ตฌ')	# 'football' key์ ์๋ ๊ฐ value๋ฅผ '์ถ๊ตฌ'๋ก ๋ฐ๊ฟ๋ผ
print(my_dict)
# {'football': '์ถ๊ตฌ', 'basketball': '๋๊ตฌ'}
```

