def solution(priorities, location):
    count = 0
    
    p = [(p,i) for i,p in enumerate(priorities)]
    max_p = max(p[0] for p in p)
    
    while p:
        priority, index = p.pop(0)

        if priority < max_p :
            p.append((priority, index))
        else :
            count += 1
            if index == location:
                return count
        
        if p :
            max_p = max(p[0] for p in p)

    return count





