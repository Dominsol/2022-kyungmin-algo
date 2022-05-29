n = int(input())   # 수의 개수
array = []

# array라는 배열에 입력 값 모두 담기
for _ in range(n):
    array.append(int(input()))

# 선택정렬
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if array[min_index] > array[j]:  # 가장 작은 수의 인덱스를 찾는다
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 가장 작은 수를 가장 앞에 배치


for i in array:
    print(i)


"""
방법2: sorted을 사용하면 시간복잡도 측면에서 더 좋다
"""
n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = sorted(array)

for i in array:
    print(i)