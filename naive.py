def naive_search(text, pattern):
    m = len(pattern)
    n = len(text)
    matches = []
    
    if m == 0 or m > n:
        return []
        
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)
            
    return matches
