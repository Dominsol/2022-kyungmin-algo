Day = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
x, y = map(int,input().split())  # 달, 일 입력
 
# 직전 달까지의 일수 모두 더하기
for i in range(x-1):
    Day = Day + arrList[i]

# 해당 달의 일수 더해 7으로 나눈 나머지 구하기
Day = (Day + y) % 7
 
print(weekList[Day])

"""
방법2
"""

import calendar

arrList = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int,input().split())

Day = calendar.weekday(2007, x, y)
print(arrList[Day])