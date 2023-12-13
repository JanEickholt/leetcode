def sortPeople(names, heights):
    return [name for _, name in sorted(zip(heights, names), reverse=True)]
