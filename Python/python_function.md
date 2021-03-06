# π Python Function

#### Category

[Why Function?](#%EF%B8%8F-why-function)

[ν¨μ](#%EF%B8%8F-ν¨μ)

- [μ¬μ©μ ν¨μ](#μ¬μ©μ-ν¨μ)
- [ν¨μ κΈ°λ³Έ κ΅¬μ‘°](#ν¨μ-κΈ°λ³Έ-κ΅¬μ‘°)
- [μ μΈκ³Ό νΈμΆ](#μ μΈκ³Ό-νΈμΆ)

[ν¨μμ κ²°κ³Όκ° (Output)](#%EF%B8%8F-ν¨μμ-κ²°κ³Όκ°-output)

[ν¨μμ μλ ₯ (Input)](#%EF%B8%8F-ν¨μμ-μλ ₯-input)

- [Positional Arguments](#positional-arguments)
- [Keyword Arguments](#keyword-arguments)
- [Default Arguments Values](#default-arguments-values)
- [μ ν΄μ§μ§ μμ κ°μμ Argument](#μ ν΄μ§μ§-μμ-κ°μμ-argument)
- [μ ν΄μ§μ§ μμ κ°μμ Keyword Argument](#μ ν΄μ§μ§-μμ-κ°μμ-keyword-argument)

[ν¨μμ λ²μ (Scope)](#%EF%B8%8F-ν¨μμ-λ²μ-scope)

[ν¨μ μμ©](#%EF%B8%8F-ν¨μ-μμ©)

- [map](#map)



## βοΈ Why Function?

> Decomposition : κΈ°λ₯μ λΆν΄ν΄μ, μ¬μ¬μ©μ΄ κ°λ₯νλ€
>
> Abstraction : μΆμν (λ³΅μ‘ν λ΄μ©μ μ¨κΈ°κ³ , κΈ°λ₯μ μ§μ€νμ¬ μ¬μ©ν  μ μμ)



- Abstraction
  - μ΄λ€ κΈ°λ₯μ΄ λ€μ΄κ°λμ§λ λͺ¨λ₯΄μ§λ§, inputμ λ£μΌλ©΄ outputμ΄ κ²°κ³Όλ‘ λμ¨λ€

βββ **Input** ββ  π  ββ **Output** βββ



## βοΈ ν¨μ

> ν¨μ (Function)λ νΉμ ν κΈ°λ₯μ νλ μ½λμ μ‘°κ° (λ¬Άμ)
>
> μ¬μ©μκ° νμ μμλ§ νΈμΆνμ¬ κ°νΈν μ¬μ©μ΄ κ°λ₯νλ€

#### μ¬μ©μ ν¨μ(Custom Function)

```python
def function_name					# function_name μ μλ ₯ν  κ°μ λ³μλ₯Ό λ£λλ€
	# code block
    return returning_value			# λ°νν  κ°μ μ€μ νλ€
-----------------------------------------------------------------------------------------------------------
# μ)
def add(a, b):
    return a + b

print(add(a, b))
```



#### ν¨μ κΈ°λ³Έ κ΅¬μ‘°

![function_1](python_function.assets/function_1.png)

- μ μΈκ³Ό νΈμΆ (Define & call)
- μλ ₯ (Input)
- λ²μ (Scope)
- κ²°κ³Όκ° (Output)



#### μ μΈκ³Ό νΈμΆ

> μ μΈν  λμλ `def` ν€μλλ₯Ό νμ©νλ€
>
> νΈμΆμ ν¨μλͺ() μΌλ‘ νΈμΆνλ€

```python
# def == μ μΈ / func(a, b) == νΈμΆ
def func(a, b):
    return a + b
```





## βοΈ ν¨μμ κ²°κ³Όκ° (Output)

> λ°λμ κ°μ **νλλ§ return** νλ€.
>
> 'μ½€λ§'λ₯Ό νμ©νμ¬ ννλ‘ λ°νν  μ μλ€

```python
def double(a, b):
    return a + b
	return a * b

print(double(1, 1))
# 2, λ§¨ μμ 'return' κ°λ§ λ°νλλ€
--------------------------------------------------------------------------------

def double(a, b):
    return a + b, a * b
print(double(1, 1))
# (2, 1) , μ»΄λ§λ₯Ό μ΄μ©ν¨μΌλ‘ ννλ‘ λ°νλλ€
```

#### return vs print

> **return**μ ν¨μ μμμ κ°μ λ°ννκΈ° μν΄ μ¬μ©λλ ν€μλ
>
> **print**λ μΆλ ₯μ μν΄ μ¬μ©λλ ν¨μ



## βοΈ ν¨μμ μλ ₯ (Input)

> Parameter : ν¨μλ₯Ό μ€νν  λ, ν¨μ λ΄λΆμμ μ¬μ©λλ μλ³μ
>
> Argument : ν¨μλ₯Ό νΈμΆ ν  λ, λ£μ΄μ£Όλ κ°

```python
def function(ham):		# parameter : ham
    return ham

function('spam')		# argument : 'spam'
```

#### Argument

- ν¨μ νΈμΆ μ ν¨μμ parameterλ₯Ό ν΅ν΄ μ λ¬λλ κ°
- value sent to the function when it is called



#### Positional Arguments

> μμΉμ λ°λΌ ν¨μ λ΄μ μ λ¬

```python
def add(x, y):
    return x + y

add(2, 3)
# μμΉμ λ°λΌ ν¨μκ° μ λ¬λλ€. x = 2 / y = 3
```



#### Keyword Arguments

> μ§μ  λ³μμ μ΄λ¦μΌλ‘ νΉμ  Argumentλ₯Ό μ λ¬

```python
def add(x, y):
    return x + y

add(y=5, x=2) or add(2, y=5)
# x, yμ κ°μ μ€μ μ ν΄μ€λ€. x = 2 / y = 5
```



#### Default Arguments Values

> κΈ°λ³Έκ°μ μ μν΄λλ κ²

```python
def add(x, y=0):
    return x + y

add(2)
# yλ μ΄λ―Έ 0μΌλ‘ μ μκ° λμ΄ μλ€. x = 2 / y = 0
```



#### μ ν΄μ§μ§ μμ κ°μμ Argument

> μ¬λ¬ κ°μ Positional Argumentλ₯Ό νλμ νμ parameterλ‘ λ°μμ μ¬μ©
>
> Argumentλ€μ ννλ‘ λ¬Άμ¬ μ²λ¦¬λλ©°, parameterμ *λ₯Ό λΆμΈλ€

```python
def add(*args):
    for arg in args:
        print(arg)
add(2)				# 2
add(2, 3, 4, 5)		# 2 3 4 5
```



#### μ ν΄μ§μ§ μμ κ°μμ Keyword Argument

> ν¨μκ° μμμ κ°μ Argumentλ₯Ό Keyword Argumentλ‘ νΈμΆλ  μ μλλ‘ μ§μ 
>
> λ΄λΆμμ Keyword Argument λμλλ¦¬ νμ©
>
> parameterμ **λ₯Ό λΆμ¬ νν

```python
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# His last name is Refsnes
```





## βοΈ ν¨μμ λ²μ (Scope)

> μ½λ λ΄λΆμ local scopeλ₯Ό μμ±νλ©°, κ·Έ μΈ κ³΅κ°μΈ global scopeλ‘ κ΅¬λΆ

- Scope
  - Global Scope : μ½λ μ΄λμμλ  μ°Έμ‘°ν  μ μλ κ³΅κ°
  - Local Scope : ν¨μκ° λ§λ  scope. ν¨μ λ΄λΆμμλ§ μ°Έμ‘° κ°λ₯

- κ°μ²΄ μλ³μ£ΌκΈ°
  - Built-in Scope : νμ΄μ¬μ΄ μ€νλ μ΄νλΆν° μμν μ μ§
  - Global Scope : λͺ¨λμ΄ νΈμΆλ μμ  μ΄ν νΉμ μΈν°νλ¦¬ν°κ° λλ  λκΉμ§ μ μ§
  - Local Scope : ν¨μκ° νΈμΆλ  λ μμ±μ΄λκ³ , ν¨μκ° μ’λ£λ  λκΉμ§ μ μ§



#### μ΄λ¦ κ²μ κ·μΉ (Name Resolution)

> LEGB Rule : Local scope β Enclosed Scope β Global Scope β Built-in scope
>
> μ΄ μμλ‘ μ΄λ¦μ μ°Ύμ λ€λλ€

**Local Scope** : ν¨μ

**Enclosed Scope** : νΉμ  ν¨μμ μμ ν¨μ

**Global Scope** : ν¨μ λ°μ λ³μ, Import λͺ¨λ

**Built-in Scope** : νμ΄μ¬ μμ λ΄μ₯λμ΄ μλ ν¨μ λλ μμ±



## βοΈ ν¨μ μμ©

> νμ΄μ¬ μΈν°νλ¦¬ν°μλ μ¬μ©ν  μ μλ λ§μ ν¨μμ ν(type)μ΄ λ΄μ₯λμ΄ μμ

#### map

`map(function, iterable)` : μν κ°λ₯ν λ°μ΄ν°κ΅¬μ‘°(iterable)μ λͺ¨λ  μμμ ν¨μ(function)λ₯Ό μ μ©νκ³ , κ·Έ κ²°κ³Όλ₯Ό map objectλ‘ λ°ν

```python
number = ['1', '2', '3']
# λ¦¬μ€νΈλ₯Ό μ«μλ‘ ν λ³ν λΆκ°λ₯/ μ«μμμ λ¬Έμλ κ°λ₯

a = int(number[0])
b = int(number[1]) .... # μ΄λ κ² ν΄μΌ μ«μλ‘ λ³κ²½λλ€

new_num = map(int, number)
print(new_num) / print(list(new_num)) 
# map μ μ΄μ©ν΄μ λ¦¬μ€νΈλ₯Ό μ«μ νμΌλ‘ λ³ννλ€
```

