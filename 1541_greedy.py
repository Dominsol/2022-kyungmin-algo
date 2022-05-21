# 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.


# 더하기 끼리 괄호로 묶어 최대한 큰 수를 만든 다음에 빼준다

a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)