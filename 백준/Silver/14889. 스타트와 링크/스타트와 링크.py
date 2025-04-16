from itertools import combinations

n = int(input())
sum = []

for i in range(n):
    sum.append(list(map(int, input().split())))
# sum = [[0, 1, 2, 3, 4, 5],
#         [1, 0, 2, 3, 4, 5],
#         [1, 2, 0, 3, 4, 5],
#         [1, 2, 3, 0, 4, 5],
#         [1, 2, 3, 4, 0, 5],
#         [1, 2, 3, 4, 5, 0]]



lst = [i for i in range(n)]
comb_lst = list(combinations(lst,len(lst)//2)) 

pre_comb = comb_lst[:len(comb_lst)//2]
pos_comb = comb_lst[len(comb_lst)//2:]

min = 1000

for i in range(len(pre_comb)):
    sum1 = 0
    sum2 = 0
    # print( "팀 1: " , list(combinations(pre_comb[i], 2) ) )
    sum_lst1 = list(combinations(pre_comb[i],2)) 

    # print( "팀 2: " , list(combinations(pos_comb[-(i+1)], 2) ) )
    sum_lst2 = list(combinations(pos_comb[-(i+1)],2)) 

    for s in sum_lst1 :
        sum1 += sum[s[0]][s[1]]+ sum[s[1]][s[0]]
    
    for s in sum_lst2 :
        sum2 += sum[s[0]][s[1]]+ sum[s[1]][s[0]]

    # print(">> 팀 1 합 : " , sum1)
    # print(">> 팀 2 합 : " , sum2)
    # print("차이 :" , abs(sum1 - sum2))

    dif = abs(sum1 - sum2)

    if dif < min :
        min = dif

    
print(min)