def targetIndices(nums, target):
    return [i for i, j in enumerate(sorted(nums)) if j == target]
