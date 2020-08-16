def trampolineJumper(T, m):
    trampolineJumps = []
    current = 0
    t = T[-1]
    i = 0
    while i < len(T) and current != t:
        i = bestJump(T, m, t, i)
        if i == None:
            return "impossible"
        else:
            trampolineJumps.append(T[i])
            current = T[i]
    return trampolineJumps    

def bestJump(T, m, t, i):
    current = T[i]
    # import pdb; pdb.set_trace()
    while i < len(T) and T[i]-current <= m:
        i += 1
    if T[i-1] == current and i < len(T) and T[i]-current > m:
        return None
    return i-1

print(trampolineJumper([0, 3, 4, 6, 10, 12], 4))
