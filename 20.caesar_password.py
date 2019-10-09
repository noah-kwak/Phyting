#시저암호 풀기
#시저 암호는 알파벳을 입력하고 n값을 입력하면 입력한 알파벳의 n번째 뒤에 있는 알파벳으로 변환
#cat,5 - hey

a = input("변환할 암호를 입력하시오\n")
n = int(input("n값을 입력하시오\n"))
cae =""

for i in range(len(a)):
    char = a[i]
    char_number = ord(char)
    if char.islower():
        char_number = (char_number + n - ord('a'))%26 + ord('a')
    if char.isupper():
        char_number = (char_number + n - ord('A')) % 26 + ord('A')
    cae += chr(char_number)
print(cae)
