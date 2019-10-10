a = int(input("2진법으로 변환할 숫자를 입력해주세요\n"))
b=[]
while a:
    b.append(a%2)
    a = int(a/2)
b.reverse()
print(b)
