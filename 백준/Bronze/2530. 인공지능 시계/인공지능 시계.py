import sys
input = sys.stdin.readline

# 시간
# 60*60 = 3600초

# 분
# 60 -> 몫 / 초 :나머지

hour, min, sec = map(int,input().split())

cooking = int(input().strip())

add_hour = cooking // 3600
add_min = (cooking % 3600) // 60
add_sec = (cooking % 3600) % 60

sec += add_sec

if sec >=60:
    sec = sec % 60
    min += 1

min += add_min

if min >= 60:
    min = min % 60
    hour +=1

hour += add_hour

if hour>=24:
    hour = hour % 24

print(hour,min,sec)