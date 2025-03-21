def solution(n, words):
    
    preword = []
    
    for i,w in enumerate(words):
        
        if (i+1) % n == 0 :
            player = n
        else : 
            player = (i+1) % n
        
        if i > 0 and words[i][0] != words[i-1][-1] :
            # print(">>>", player)
            # print( i // n)
            return [player, i//n +1]
            
        ## words[i] in words[:i] :
        # 따로 리스트에 append 하지 않고 조건문 한줄로 해결하는 방법 대애박~
        if w in preword :
            # print("###", player)
            # print( i //n )
            return [player, i//n +1 ]
        
        preword.append(w)

    return [0,0]

        
        