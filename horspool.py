def build_shift_table(pattern):
    table = {}
    m = len(pattern)
    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i
    return table

def horspool_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0 or m > n:
        return []
        
    table = build_shift_table(pattern)
    matches = []
    
    i = m - 1
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
            
        if k == m:
            matches.append(i - m + 1)
            
        i += table.get(text[i], m)
        
    return matches
