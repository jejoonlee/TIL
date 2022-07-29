# 📋Algorithm - 문자열 (String)

#### Category

[문자열](#%EF%B8%8F-문자열)

[문자열 슬라이싱](#%EF%B8%8F-문자열-슬라이싱)

[문자열 메서드](#%EF%B8%8F-문자열 메서드)

[아스키(ASCII) 코드](#%EF%B8%8F-아스키-ASCII-코드)



## ✔️ 문자열

> 문자열은 immutable (변경이 불가능 하다) - 즉 바뀌면 새로운 데이터가 생성되고, 원래 있던 데이터는 없어진다
>
> 문자열은 순회가 가능하다 (Iterable)



## ✔️ 문자열 슬라이싱

> 문자열 슬라이싱을 할 때 문자열은 변경되지 않는다
>
> 문자열은 0으로 시작하고 -1이 제일 마지막 값이다
>
> 문자열 개수에 음수를 더하면 양수가 된다

**s = 'abcdefgh'**

|       |  a   |  b   |  c   |  d   |  e   |  f   |  g   |  h   |
| :---: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| index |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |
| index |  -8  |  -7  |  -6  |  -5  |  -4  |  -3  |  -2  |  -1  |

```python
s[2:5] 		 # 'cde'
s[-6:-2] 	 # 'cdef'
s[2:-4] 	 # 'cd'
s[2:5:2]	 # 'ce' 2이상 5미만, 인덱스 2씩 띄어서
s[-6:-1:3]	 # 'cf'
s[2:5:-1]	 # '' 2이상 5미만인데, -1 뒤로 가는건 불가능
s[5:2:-1]	 # 'fed'
s[:3]		 # 'abc'
s[5:]		 # 'fgh'
s[:]		 # 'abcdefgh'
s[::-1]		 # 'hgfedcba'
```



## ✔️ 문자열 메서드

| Method       | Time Complexity | Function                                                     |
| ------------ | --------------- | ------------------------------------------------------------ |
| `.split()`   | O(N)            | 문자열을 일정 기준으로 나누어 리스트로 반환 / 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 기준으로 설정 |
| `.strip()`   | O(N)            | 양쪽 끝에 있는 특정 문자를 모두 제거한 **새로운 문자열 반환** / 아무것도 안 넣으면 자동으로 공백만 제거 문자로 설정 |
| `.find()`    | O(N)            | 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환 / 찾는 문자가 없다면 -1을 반환 / 찾아도 계속 실행한다 |
| `.index()`   | O(N)            | 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환 / 찾는 문자가 없으면 오류 발생 |
| `.count()`   | O(N)            | 문자열에서 특정 문자가 몇 개인지 반환 / 문자 뿐만 아니라, 문자열의 개수도 확인 가능 |
| `.replace()` | O(N)            | (기존 문자, 새로운 문자) 로 수정한 새로운 문자열 반환        |
| `''.join()`  | O(N)            | 각각 원소 사이에 특정 문자를 삽입한 새로운 문자열 반환       |



## ✔️ 아스키(ASCII) 코드

> 컴퓨터는 숫자만 읽을 수 있어, 아스키 코드를 통해 숫자를 문자로 변환해준다

### ord(문자)

### chr(아스키코드)

- #### A ~ Z     👉    65 ~ 90

- #### a ~ z      👉    97 ~ 122


