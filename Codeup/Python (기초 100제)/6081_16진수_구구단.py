a = int(input(), 16)      

for i in range(1,16):
    print('%X'%a, '*%X'%i, '=%X'%(a*i), sep='')

# '%X'%a : a에 입력된 값을 16진수 형태로 출력
# '*%X'%i : i에 입력된 값은 16진수로 출력하고 '*'도 포함
# '=%X'%(a*i) : a와 i 값을 곱하고 16진수로 출력 '='도 포함