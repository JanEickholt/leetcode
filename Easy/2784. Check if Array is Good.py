def isGood(nums):
    dic = {}
    n = max(nums)
    if len(nums)<n+1:
        return False
    for i in nums:
        dic[i]= dic.get(i,0)+1
    print dic
    if dic[n]!=2:
        return False
    for i in dic:
        if dic[i]>1 and i!=n:
            return False
    return True

