# Problem: https://docs.google.com/document/d/1970NPDiG0NC0BVW-cPTh7vpueeSqbFmU-xy60EvuqD0/edit?usp=sharing

print(*[[w[0]+str(len(w)-2)+w[-1],w][len(w)<3]for w in input().split()])
