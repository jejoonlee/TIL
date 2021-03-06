# πPython Basic 1

#### Category

[μ»΄ν¨ν° νλ‘κ·Έλ­ μΈμ΄](#%EF%B8%8F-μ»΄ν¨ν°-νλ‘κ·Έλλ°-μΈμ΄)

[νμ΄μ¬μ΄λ](#%EF%B8%8F-νμ΄μ¬μ΄λ)

[μ½λ μ€νμΌ κ°μ΄λ](#%EF%B8%8Fμ½λ-μ€νμΌ-κ°μ΄λ)

[λ³μ](#%EF%B8%8F-λ³μ-variable)

[μλ³μ (Identifiers)](#%EF%B8%8F-μλ³μ-identifiers) 

[μ¬μ©μ μλ ₯ (input)](#--μ¬μ©μ-μλ ₯-input)

[μ£Όμ (Comment)](#%EF%B8%8F-μ£Όμ-comment)

[νμ΄μ¬ κΈ°λ³Έ μλ£ν](#%EF%B8%8F-νμ΄μ¬-κΈ°λ³Έ-μλ£ν)    β λΆλ¦°ν, μμΉν, λ¬Έμμ΄, None

- [None](#-none)
- [λΆλ¦°ν Boolean Type](#-λΆλ¦°ν-boolean-type)
- [μμΉν Numeric Type](#-μμΉν-numeric-type)
- [λ¬Έμμ΄](#-λ¬Έμμ΄-string)

[ν λ³ν](#%EF%B8%8F-ν-λ³ν)

[μ»¨νμ΄λ (Container)](#%EF%B8%8F-μ»¨νμ΄λ-container)

[μνμ€ (Sequence Container)](#-μνμ€-sequence-container)

[λΉμνμ€ν μ»¨νμ΄λ (Associative Container)](#-λΉμνμ€ν-μ»¨νμ΄λ-associative-container))





## βοΈ μ»΄ν¨ν° νλ‘κ·Έλλ° μΈμ΄

> **μ»΄ν¨ν° Computer** : Calculation + Remember
>
> **νλ‘κ·Έλλ° Programming** : λͺλ Ήμ΄μ λͺ¨μ(μ§ν©)μ μ΄μ©νλ κ²
>
> **μΈμ΄** : μμ μ **μκ°μ λνλ΄κ³  μ λ¬νκΈ°** μν΄ μ¬μ©νλ μ²΄κ³ (**λ¬Έλ²μ **μΌλ‘ λ§λ λ§μ μ§ν©)



**μ»΄ν¨ν° νλ‘κ·Έλλ° μΈμ΄** : μ»΄ν¨ν°μκ² λͺλ Ήνλ λ§ 

- λͺλ Ήμ  μ§μ (imperative knowledge) : 'How-to'





## βοΈ νμ΄μ¬μ΄λ

**Easy to learn**

- λ¬Έλ² ννμ΄ λ§€μ° κ°κ²°
- λμ  νμ΄ν μΈμ΄



**μΈν°νλ¦¬ν° μΈμ΄ (Interpreter)**

- μ½λλ₯Ό λννλ― ν μ€ μλ ₯νκ³  μ€νν ν, λ°λ‘ νμΈμ΄ κ°λ₯



**κ°μ²΄ μ§ν₯ νλ‘κ·Έλ¨ (Object Oriented Programming)**

- κ°μ²΄ (Object): μ«μ, λ¬Έμ ν΄λμ€ λ± κ°μ κ°μ§κ³  μλ λͺ¨λ  κ²
- λ¬Όκ±΄, λμ (μ΄λ ν κ², ~ κ²)





## βοΈμ½λ μ€νμΌ κ°μ΄λ

```python
print('Hello')
print('World')

a = 'apple'

if True:
    print(True)
else:
    print(False)
    
b = 'banana'
```

**π¨ λ€λ₯Έ μ¬λλ€μ΄ μμλ³Ό μ μλλ‘, μΌκ΄μ± μκ² μμ±**

- **λ€μ¬μ°κΈ°**
  - 4μΉΈ (space ν€ 4λ²) νΉμ 1ν­ (tab 1λ²)μ μλ ₯





## βοΈ λ³μ (Variable)

> λ³ν  μ μλ μ
>
> λ³μλ ν λΉ μ°μ°μ (=)λ₯Ό ν΅ν΄ κ°μ ν λΉ (assignment)
>
> **type()** μ ν΅ν΄ λ³μμ ν λΉλ κ°μ νμμ νμΈν  μ μλ€

```python
a = 7
a = a + 10
print(a)
# 17λ‘ μΆλ ₯μ΄ λλ€

x = y = 7
print(x, y)
# κ°μ κ°μ λμμ ν λΉν  μ μλ€

x, y = 1, 2
print(x, y)
# λ€λ₯Έ κ°μ λμμ ν λΉ ν  μ μμ (multiple assignment)
-----------------------------------------------------------------------------

x, y = 10, 20					# κ°κ° κ°μ λ°κΏμ μ μ₯νλ μ½λ

tmp = x							# x κ°μ΄ tmpλΌλ μμ κ³΅κ°μ λ€μ΄κ°λ€
x = y							# y κ°μ΄ xλ‘ λ€μ΄κ°λ€
y = tmp							# tmpμ μλ x κ°μ΄ yλ‘ λ€μ΄κ°λ€

print(x, y)						# 20 10 μ΄ μΆλ ₯μ΄ λλ€
-----------------------------------------------------------------------------

x = 10
y = 20

y, x = x, y

print(x, y)						# 20 10 μ΄ μΆλ ₯λλ€
```

**π¨ (κΈ°λ³Έ) μ½λλ μμμλΆν° μλλ‘ μ€ν**





## βοΈ μλ³μ (Identifiers)

> νμ΄μ¬ κ°μ²΄ (λ³μ, ν¨μ, λͺ¨λ, ν΄λμ€ λ±)λ₯Ό μλ³νλλ° μ¬μ©νλ μ΄λ¦

**π¨κ·μΉπ¨**

- μλ³μμ μ΄λ¦μ μλ¬Έ μνλ²³, μΈλμ€μ½μ΄(_), μ«μλ‘ κ΅¬μ±
- μ²« κΈμμ μ«μκ° μ¬ μ μμ
- λμλ¬Έμλ₯Ό κ΅¬λ³
- μμ½μ΄λ€μ μ¬μ©ν  μ μμ

```python
# μμ½μ΄/ν€μλ νμΈ λ°©λ²

import keyword
print(keyword.kwlist)
```





## β  μ¬μ©μ μλ ₯ (input)

> μ¬μ©μλ‘λΆν° μ¦μ μλ ₯ λ°μ μ μλ λ΄μ₯ν¨μ
>
> Input()μ κΈ°λ³Έμ μΌλ‘ λ¬Έμμ΄μ ννλ€. λ°λΌμ μ«μλ‘ λ°κΎΈλ €λ©΄ 'int' λλ 'float' λ₯Ό μλ ₯ν΄μΌνλ€

```python
name = input('μ΄λ¦μ μλ ₯ν΄μ£ΌμΈμ: ')
print(name)
# μ΄λ¦μ μλ ₯ν΄μ£ΌμΈμ: ~~~

type(name)
# str β string
```





## βοΈ μ£Όμ (Comment)

> μ»΄ν¨ν°κ° μ½μ§ λͺ» νλ€

```python
# μ»΄ν¨ν°κ° μ½μ§ λͺ» νλ€. μ£Όλ‘ μ½λ λ΄μ©μ μΈ μ μλ€
```



## βοΈ νμ΄μ¬ κΈ°λ³Έ μλ£ν

> **λΆλ¦°ν (Boolean Type)**, **μμΉν (Numeric Type)**, **λ¬Έμμ΄ (String Type)**, **None** μ΄ μλ€



#### π None

- κ°μ΄ μμμ νννλ€



#### π λΆλ¦°ν (Boolean Type)

- `True` / `False` κ°μ κ°μ§ νμμ `bool` λλ λΆλ¦°μ΄λΌκ³  νλ€
  - 0, 0.0 , (), [], {}, ", None μ λͺ¨λ `False`

| μ°μ°μ  |                             λ΄μ©                             |
| :-----: | :----------------------------------------------------------: |
| A and B |      Aμ B λͺ¨λ Trueμ, `True` / κ·Έλ μ§ μμΌλ©΄ `False`       |
| A or B  | Aμ B μ€ νλλ§μ΄λΌλ Trueλ©΄, `True` / Aμ B λͺ¨λ Falseμ, `False` |
|   Not   |                Trueλ₯Ό Falseλ‘, Falseλ₯Ό Trueλ‘                |

```python
num = 100
num >= 100 and num % 3 == 1
# numμ 100μ΄κ³  100κ³Ό 3μ λλλ©΄ 1μ΄ λ¨μΌλ―λ‘, λ λ€ Trueμ΄λ―λ‘ True λ€
```



#### π μμΉν (Numeric Type)

- **Integer (int, μ μ)**
  - λͺ¨λ  μ μμ νμμ int
  - μ€λ²νλ‘μ°κ° λ°μνμ§ μμ
- **Float (μ€μ)**
  - μ μκ° μλ λͺ¨λ  μ€μ (real number), μ¦ μμλ Float
  - Floating point rounding errorλ₯Ό μ£Όμ
- λ³΅μμ (Complex)
  - μ€μλΆμ νμλΆλ‘ κ΅¬μ±λ λ³΅μμλ λͺ¨λ complex νμ

| μ°μ°μ  |    λ΄μ©    |
| :-----: | :--------: |
|   `+`   |    λ§μ    |
|   `-`   |    λΊμ    |
|   `*`   |    κ³±μ    |
|   `%`   |   λλ¨Έμ§   |
|   `/`   |   λλμ   |
|  `//`   |     λͺ«     |
|  `**`   |  κ±°λ­μ κ³±  |
|         |            |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a// b  |
|  a%=b   | a = a % b  |
| a **=b  | a = a ** b |
|         |            |
|    <    |    λ―Έλ§    |
|   <=    |    μ΄ν    |
|    >    |    μ΄κ³Ό    |
|   >=    |    μ΄μ    |
|   ==    |    κ°μ    |
|   !=    | κ°μ§ μμ  |



#### π λ¬Έμμ΄ (String)

- λͺ¨λ  λ¬Έμλ str νμ

- λ¬Έμμ΄μ μμ λ°μ΄ν('')λ ν° λ°μ΄ν("")λ₯Ό νμ©

  - νλλ‘ ν΅μΌνκΈ°
  - μ€μ²©λ°μ΄ν

  ```python
  print('λ¬Έμμ΄ μμ"ν° λ°μ΄ν"λ₯Ό μ¬μ©νλ €λ©΄ μμ λ°μ΄νλ‘ λ¬Άλλ€')
  print("λ¬Έμμ΄ μμ'μμ λ°μ΄ν'λ₯Ό μ¬μ©νλ €λ©΄ ν° λ°μ΄νλ‘ λ¬Άλλ€")
  ```

  - μΌμ€λ°μ΄ν

  ```python
  print('''λ¬Έμμ΄ μμ 'μμ λ°μ΄ν'λ "ν° λ°μ΄νλ₯Ό"λ₯Ό μ¬μ©ν  μ μκ³ 
  μ¬λ¬ μ€μ μ¬μ©ν  λλ νΈλ¦¬νλ€''')
  ```

- **μΈλ±μ±/ μ¬λΌμ΄μ±**
  - μΈλ±μ€λ₯Ό ν΅ν΄ νΉμ  κ°μ μ κ·Όν  μ μμ

```python
a = 5 						# int
b = '5' 					# str, 'λ°μ΄ν' μμ λ€μ΄κ°μ 5λ λ¬Έμμ΄λ‘ κ΅¬λΆ
print(a, type(a))			# 5, <class 'int'>
print(b, type(b))			# 5, <class 'str'>

# κΈΈμ΄ - len
fruit = 'abcde'
print(len(fruit)) 			# 5, fruitμ valueλ abcdeκ³  5κ°μ λ¬Έμλ‘ μ΄λ£¨μ΄μ Έμμ

# μ κ·Ό/μΈλ±μ±
print(fruit[1]) 			# b, abcde μ€ 1λ²μ§Έλ bμ΄λ€. μ»΄ν¨ν°μμ μ«μλ 0λΆν° 

# μ¬λΌμ΄μ±
print(fruit[1:3]) 			# bc, 1 μ΄μ 3 λ―Έλ§
								# a b c d e
								# 0 1 2 3 4

print(fruit[1:4:2])			# bd, 1μ΄μ 4 λ―Έλ§ μ€ 2μ© μ ν

print(fruit[4:1:-1])		# edc, 4μ΄ν 1μ΄κ³Ό (-1) λ€λ‘

print(fruit[:2])			# ab, 0μ΄μ 2 λ―Έλ§

print(fruit[3:])			# de, 3μ΄μ
        
# νμ΄μ¬μ μμ μΈλ±μ€λ κ°μ§κ³  μλ€!
print(fruit[len(fruit)-1])		# e, 
print(fruit[-1])				# e, -1 λ§¨ λ§μ§λ§ λ¨μ΄λΌλ λ»
```



- κΈ°ν

```python
# κ²°ν© (concatenation)
'hello, ' + 'python!'		# 'hello, python!'

# λ°λ³΅ (Repetition)
'hi' * 3					# 'hihihi'

# ν¬ν¨ (Membership)
'a' in 'apple'				# True
'app' in 'apple'			# True
'b' in 'apple'				# False
```



- **Escape Sequence**

| μμ½λ¬Έμ |   λ΄μ©(μλ―Έ)    |
| :------: | :-------------: |
|   `\n`   |     μ€ λ°κΏ     |
|   `\t`   |       ν­        |
|   `\r`   |   μΊλ¦¬μ§λ¦¬ν΄    |
|   `\0`   | λ (null, none) |
|   `\\`   |       `\`       |
|   `\'`   | λ¨μΌμΈμ©λΆνΈ(') |
|   `\"`   | μ΄μ€μΈμ©λΆνΈ(") |

```python
print('Alex \'Hello\'')
# Alex 'Hello'

print('Next is enter.\nand tab\ttab')
# Next is enter.
# And tab	tab
```





## βοΈ ν λ³ν

> νμ΄μ¬μμ λ°μ΄ν° ννλ μλ‘ λ³νν  μ μμ
>
> - μμμ  ν λ³ν (νμ΄μ¬ λ΄λΆμ μΌλ‘ μλ£νμ λ³ννλ κ²½μ°)
> - λͺμμ  ν λ³ν (μ¬μ©μκ° μ§μ  νμμ λ§λ λ¬Έμμ΄μ λ³ννλ κ²½μ°)

- μμμ  ν λ³ν
  - bool / numeric type (int, float, complex)
- λͺμμ  ν λ³ν
  - int : str, float  β int
  - float: str, int  β float
  - str: int, float, list, tuple, dict β str





## βοΈ μ»¨νμ΄λ (Container)

> μ¬λ¬ κ°μ κ°μ λ΄μ μ μλ κ²μΌλ‘, μλ‘ λ€λ₯Έ μλ£νμ μ μ₯ν  μ μμ

**μ»¨νμ΄λ λΆλ₯**

- μνμ€: μμκ° μμ (indexλ‘ μ κ·Ό, 0μΌλ‘ μμ)
  - λ¬Έμμ΄ (immutable) : λ¬Έμλ€μ λμ΄
  - λ¦¬μ€νΈ (mutable) : λ³κ²½ κ°λ₯ν κ°λ€μ λμ΄
  - νν (immutable) : λ³κ²½ λΆκ°λ₯ν κ°λ€μ λμ΄
  - λ μΈμ§ (immutable) : μ«μμ λμ΄
- μ»¬λ μ/ λΉμνμ€: μμκ° μμ
  - μΈνΈ : μ μΌν κ°λ€μ λͺ¨μ (μ€λ³΅μ΄ μμΌλ©΄, νλλ‘ λ§λ€μ΄ μ€λ€)
  - λμλλ¦¬ : ν€-κ°λ€μ λͺ¨μ



### π μνμ€ (Sequence Container)

**μνμ€ν μ£Όμ κ³΅ν΅ μ°μ°μ**

| μ°μ°             | κ²°κ³Ό                                                     |
| ---------------- | -------------------------------------------------------- |
| s[i]             | sμ i λ²μ§Έ ν­λͺ©, 0μμ μμ                              |
| s[i:j]           | sμ i μμ jκΉμ§μ μ¬λΌμ΄μ€                              |
| s[i:j:k]         | s μ i μμ jκΉμ§ μ€ν­ kμ μ¬λΌμ΄μ€                      |
| s + t            | sμ tμ μ΄μ΄ λΆμ΄κΈ°                                      |
| s * n λλ n * s | s λ₯Ό κ·Έ μμ μ n λ² λνλ κ²                            |
| x in s           | s μ ν­λͺ© μ€ νλκ° xμ κ°μΌλ©΄ True, κ·Έλ μ§ μμΌλ©΄ False |
| x not in s       | s μ ν­λͺ© μ€ νλκ° xμ κ°μΌλ©΄ False, κ·Έλ μ§ μμΌλ©΄ True |
| len(s)           | s μ κΈΈμ΄                                                |
| min(s)           | s μ κ°μ₯ μμ ν­λͺ©                                      |
| max(s)           | s μ κ°μ₯ ν° ν­λͺ©                                        |



**λ¦¬μ€νΈ(List)μ μ μ [ ]**

- λ³κ²½ κ°λ₯ν κ°λ€μ λμ΄λ μλ£ν / λκ΄νΈ `[0, 1, 2]` ννλ‘ μ μνλ©°, μ½€λ§λ‘ κ΅¬λΆ
- λ³κ²½ κ°λ₯ + λ°λ³΅ κ°λ₯

```python
Li = ['a', 'b', 'c', 'd', 'e', 'f']			# λ¦¬μ€νΈ μμ±

print(list[0])								# λ¦¬μ€νΈμ 0λ²μ§Έ μΆλ ₯, a

Li[0] = 'g'									# 0λ²μ§Έ κ° λ³κ²½
print(list)									# ['g', 'b', 'c', 'd', 'e', 'f']

Li.append('h')								# .appendλ₯Ό μ΄μ©ν΄ λ¦¬μ€νΈμ 'h' μΆκ°

Li.pop(0)									# .popλ₯Ό μ΄μ©ν΄ λ¦¬μ€νΈμ 'g' μ­μ 

len(list)		# 6

Li[2]			# 'c'

Li[3][0]		# 'd'
```



**νν (Tuple)**

- λΆλ³ν κ°λ€μ λμ΄ 
- λ¦¬μ€νΈλ λκ°μ§λ§, *λ³κ²½μ΄ λΆκ°* (μΆκ°, μ­μ λ λΆκ°λ₯)



**λ μΈμ§ (Range)** - λ³κ²½ λΆκ°λ₯, λ°λ³΅ κ°λ₯

- κΈ°λ³Έν : range(n)
  - 0 λΆν° n-1 κΉμ§μ μ«μμ μνμ€
- λ²μ μ§μ  : range(n, m)
  - n λΆν° m-1 κΉμ§μ μ«μμ μνμ€
- λ²μ λ° μ€ν μ§μ  : range(n, m, s)
  - n λΆν° m-1 κΉμ§ sλ§νΌ μ¦κ°μν€λ©° μ«μμ μνμ€

```python
list(range(3))
# [0, 1, 2]

list(range(1, 5))
# [1, 2, 3, 4]

list(range(1, 5, 2))
# [1, 3]

list(range(6, 1, -1))
# [6, 5, 4, 3, 2]

list(range(6, 1, 1))
#[]
```



### π λΉμνμ€ν μ»¨νμ΄λ (Associative Container)

> μΈνΈ (Set) μ λμλλ¦¬ (Dictionary)κ° μλ€

**μΈνΈ (Set)**

- μ μΌν κ°λ€μ λͺ¨μ
- μμκ° μκ³ , μ€λ³΅λ κ°μ νλλ‘ λ§λ€μ΄μ§λ€

```python
{1, 2, 3, 1, 4}				# {1, 2, 3, 4} μ€λ³΅ κ°μΈ 1μ μ κ±°
set(1, 2, 3, 1, 4)			# {1, 2, 3, 4}, set()λ₯Ό ν΅ν΄μλ μΈνΈλ₯Ό μμ±ν  μ μλ€
-----------------------------------------------------------------------------

numbers = {1, 2, 3}
numbers.add(7)				# μ«μλ₯Ό .add λ₯Ό ν΅ν΄ μΆκ°ν  μ μλ€
numbers. remove(1)			# .removeλ₯Ό ν΅ν΄ κ°μ λΊ μ μλ€
#{2, 3, 7}

len(set(numbers))			# κ³ μ ν μ«μμ κ°μλ₯Ό νμΈ
set(numbers)				# {2, 3, 7}
```



**λμλλ¦¬ (Dictionary) { }** 

- ν€ (key)μ κ° (value) μμΌλ‘ μ΄λ£¨μ΄μ§ λͺ¨μ
  - ν€ : λΆλ³ μλ£νλ§ κ°λ₯ (λ¦¬μ€νΈ, λμλλ¦¬ λ±μ λΆκ°λ₯)
  - κ° : μ΄λ ν ννλ  κ΄κ³ μμ
- ν€μ κ°μ `:` λ‘ κ΅¬λΆλλ©°, κ°λ³ μμλ `,` λ‘ κ΅¬λΆ λλ€

```python
student = {'Alex': 77, 'Bob': 27}
student['Alex']						# 77

#μΆκ° λ° λ³κ²½
student['Alex'] = 7						# {'Alex': 7, 'Bob': 27}
student['Chris'] = 17					# {'Alex': 7, 'Bob': 27, 'Chris': 17}

#μ­μ 
student.pop('Bob')						# .popμ μ΄μ©ν΄ 'Bob'μ μ­μ 
student									# {'Alex': 7, 'Chris': 17}
```

