# 2805번 나무 자르기
# 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. 
# (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
# 나머지를 집에 갖고감

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)                # 이분탐색 검색 범위 설정

while start <= end:                      # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    log = 0                              # 벌목된 나무 총합: M이 log보다 작으면 안된다.
    for i in tree:
        if i >= mid:
            log += i - mid
    
    # 벌목 높이를 이분탐색
    # end를 최대로 하기 위한 방법
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)