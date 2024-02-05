def garbageCollection(garbage, travel):
    last = {c: i for i, g in enumerate(garbage) for c in g if c in "MPG"}
    time = sum(len(g) for g in garbage) + sum(sum(travel[:i]) for i in last.values())
    return time
