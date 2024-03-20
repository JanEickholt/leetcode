def findContentChildren(g, s):
    g.sort()[::-1]
    greed = 0
    for i in g:
        for j in s:
            if j >= i:
                greed += 1
                s.remove(j)
                break
    return greed
