#피보나치 수열은 각 항이 바로 앞 두 항의 합
#1,2,3,5,8,13,21....
#짝수이면서 4백만 이하인 모든 항을 더하면 얼마?
fibo = [1,2]
i=1
while True:
     t = fibo[i] + fibo[i-1]
     i += 1
     if t>4000000:
         break
     fibo.append(t)

for j in range(len(fibo)):
    if fibo[j] % 2 !=0:
        fibo[j]=0
new_fibo = sum(fibo)
print(new_fibo)

'''전문가 답변
x = 0
y = 1
s = 0
while y < 40000001:
    x = x + y
   y, x = x, y
   if y % 2 == 0: s += y
print(s) '''

