import sys
input = sys.stdin.readline


keys = ['Algorithm','DataAnalysis','ArtificialIntelligence','CyberSecurity',
        'Network','Startup','TestStrategy']

values = [204,207,302,'B101',303,501,105]

data_class = dict(zip(keys,values))

N = int(input())

for _ in range(N):
    the_class = str(input()).strip()
    print(data_class[the_class])