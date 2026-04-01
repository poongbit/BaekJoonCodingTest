import sys
input = sys.stdin.readline

"""
dp[i][k] : 0~i까지, 0~k까지 범위 내에서 같은 순서로 나온 단어의
길이

"""
word_list = []

for _ in range(2):
    line = str(input().strip())
    word_list.append(line)

word1 = word_list[0]
word2 = word_list[1]

dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]



for i in range(1,len(word1)+1):
    for j in range(1,len(word2)+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]  + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])