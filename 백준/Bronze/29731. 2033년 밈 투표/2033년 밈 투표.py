import sys
input = sys.stdin.readline

promise = set()

promise.add('Never gonna give you up')
promise.add('Never gonna let you down')
promise.add('Never gonna run around and desert you')
promise.add('Never gonna make you cry')
promise.add('Never gonna say goodbye')
promise.add('Never gonna tell a lie and hurt you')
promise.add('Never gonna stop')

answer = []



N = int(input().strip())
is_promise = True

for _ in range(N):
    sentence = str(input().strip())

    if sentence not in promise:
        is_promise = False


if is_promise:
    print('No')

else:
    print('Yes')
