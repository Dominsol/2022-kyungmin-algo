# 좌표 정렬하기
import sys
n = int(sys.stdin.readline())
so = []

for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))

# x좌표를 기준으로 먼저 정렬 후 y 좌표를 기준으로 정렬
so.sort(key=lambda x: (x[0], x[1]))
print()
for i in so:
    print(i[0], i[1])