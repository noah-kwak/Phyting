#1부터 100까지의 자연수의 합의제곱과 제곱의 합의 차이
sum = 0
powsum = 0
for i in range(1,101):
    sum += pow(i,2)
    powsum += i

print(pow(powsum,2)-sum)
