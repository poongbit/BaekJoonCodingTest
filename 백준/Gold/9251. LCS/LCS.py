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

# if word[i] == word[j]

for row in range(1,len(word1)+1):
    for column in range(1,len(word2)+1):
        
        # 글자가 같으면
        if word1[row-1] == word2[column-1]:
            dp[row][column] = dp[row-1][column-1] + 1

        else:
            dp[row][column] = max(dp[row-1][column],dp[row][column-1])


print(dp[-1][-1])