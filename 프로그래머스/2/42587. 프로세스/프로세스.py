def solution(priorities, location):
    count = 0
    
    # priorities를 (val, index) 형태로 저장
    p = [(p,i) for i,p in enumerate(priorities)]
    # print(p)
    
    # 최대 우선순위
    max_p = max(p[0] for p in p)
    
    # p 를 계속 돌면서
    while p:
        
        # 맨 앞부터 돌아 (2,0) (1,1) (3,2) (2,3)
        priority, index = p.pop(0)

        # 현재 우선순위보다 더 큰 우선순위가 있으면
        if priority < max_p :
            # p 뒤에 붙여주기 
            p.append((priority, index))
            
        # 제일 큰 우선순위이면
        else :
            # 횟수 +1 
            count += 1
            
            # 현재 index랑 리턴해야하는 location이랑 같으면
            if index == location:
                # 지금까지 쌓은 count 리턴
                return count
        
        # p가 계속 있으면
        if p :
            # 최대 우선순위 다시 구하기
            max_p = max(p[0] for p in p)

    return count





