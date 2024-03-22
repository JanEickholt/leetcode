def calculateTime(keyboard: str, word: str) -> int:
    time = 0
    prev = 0
    for i in word:
        time += abs(prev - keyboard.index(i))
        prev = keyboard.index(i)
    return time
