# π Python (Basic 1)



## βοΈ Category

[Comment](#comment)

[Print](#print)

[Variables](#variables)

[Error](#error)

[String](#string)

[Number](#number)

[Calculation](#calculation)

[Concatenation](#concatenation) λ¬Έμμ΄ μ ν©

[Plus Equal](#plus-equal)

[Multi-line Strings](#multi-line-strings)



## βοΈ Content



#### Comment

```python
# Here computer will ignore texts written in the program. This is called comment used with '# hashtag'
```





#### Print

```python
print('Hello World!')		# 'Hello World!' will be printed.
```

- `print()` function is used to tell a computer to talk





#### Variables

```python
have_a_good_day = 'sunny_day'
print='have_a_good_day'

# this will print 'sunny_day'
```

- We assign variables by using `=` 





#### Error

> When there is an error `^` character will point to the location of the error
>
> `SyntaxError` : something wrong with the way program is written 
>
> `NameError` : word it does not recognize





#### String

> It is used with variable 
>
> A string is how programming languages store text

```python
name = 'Je Joon Lee'

print(name)		# Je Joon Lee will be printed
```





#### Number

> `int`, integer, contains all numbers without decimal points
>
> `float`, float, can be used for fractional quantities (decimal) as well as precise measurements (1~10)





#### Calculation

> `+` `-` `*` `/` 
>
> `**` exponent (μ κ³±) 		ex) 2^3 β print(2 ** 3)
>
> `%` Modulo Operator (remainder of a division calculation) / λλ μ΄ν λ¨λ μ«μ

```python
print(25 * 2)
	# prints '50'
    
print(25 * 2 + 5)
	# prints '55'
```

```python
A = 1.5
B = 2
print(A * B)
	#prints '3'
```

```python
#μ κ³±
print(2 ** 3)
	# prints '8' which is 2*2*2
```

```python
#modulo operator
print(11 % 2)
	# prints '1' β 11 λλκΈ° 2λ 5---1, 1μ΄ λ¨μμ '1'μ΄ μΆλ ₯λλ€
    
my_team = 27 % 4
print(my_team)
	# prints '3'
```





#### Concatenation

```python
string1 = 'I love football.'
string2 = 'I play football every week.'
string3 = 'My position is winger'

message = string1 + " " + string2 + " " + string3

print(message)
# prints 'I love football. I play football every week. My position is winger'
```

- `" "` μ¬μ΄μ κ³΅κ°μ λ§λ€μ΄μ€λ€. (spacebar κ°μ κΈ°λ₯). μλλ©΄ λ³μμ λ§μ§λ§μ κ³΅κ°μ μ€λ€.



```python
string1 = 'I love '
string2 = 'lucky number '
number = '7'

message = string1 + string2 + str(number)
# messageλ₯Ό λ³μλ‘ λλ κ²½μ° μ«μλ₯Ό λ¬Έμμ΄λ‘ λ§λ€μ΄μΌ νλ€. κ·Έλμ str(number) κ° μλ κ²

print(message)
# prints 'I love lucky number 7'

-----------------------------------------------------------------------------------------------------------

# message λ³μκ° μλ κ²½μ°, μ«μλ₯Ό λ¬Έμμ΄λ‘ μ λ§λ€μ΄λ λ¨

string1 = 'I love '
string2 = 'lucky number '
number = '7'

print(string1, number, string2)
```





#### Plus Equal

> Shorthand for updating variables
>
> `+=` when you have a number saved in a variable and want to add to the current value of the variable
>
> `+=` adds the value afterwards to the variable and then updates the variable to be the sum
>
> Can also be used in concatenation

```python
total_price = 0
# 0 will be printed

new_cloths = 20 

total_price += new_cloths 		# += used
# 20 will be printed

new_shoes = 30
new_book = 10

total_price += new_shoes + new book			# += used

print(total_price)	# this will print 60
```





#### Multi-line Strings

> `'''....'''` or `"""..."""`

```python
to_you = '''Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
'''
print(to_you)
```

π¨If multi-line is not assigned a variable, it is treated as comment

