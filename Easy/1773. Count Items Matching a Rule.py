def countMatches(items, ruleKey, ruleValue):
    cnt = 0
    for item in items:
        product = {"type": item[0], "color": item[1], "name": item[2]}
        if product[ruleKey] == ruleValue:
            cnt += 1

    return cnt
