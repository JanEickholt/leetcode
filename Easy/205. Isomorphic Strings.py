def isIsomorphic(s, t):
    return len(set(s))==len(set(zip(s,t))) and len(set(t))==len(set(zip(s,t)))

