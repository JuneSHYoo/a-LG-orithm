puzzle = ['ABCD','EFGH','IJKL','MNO.']
inpuz = []

orign_pos = {}
change_pos ={}
answer = 0 
for _ in range(4):
    inpuz.append(input())


for i in range(4):
    for j in range(4):
        if puzzle[i][j] != inpuz[i][j]:
            orign_pos[puzzle[i][j]] = (i, j)
            change_pos[inpuz[i][j]] = (i, j)


for k, v in change_pos.items():
    if k != '.':
        x1, y1 = orign_pos[k]
        x2, y2 = v
        answer += abs(x1 - x2) + abs(y1 - y2)
    
print(answer)            