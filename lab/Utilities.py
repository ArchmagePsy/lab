def binary_search(array, target, key = lambda item: item):
    results = []
    tmpArray = array
    while True:
        index = len(tmpArray // 2)
        current = key(tmpArray[index])
        if current == target:
            results.append((current, index))
        elif current > target:
            tmpArray = tmpArray[:index]
        elif current < target:
            tmpArray = tmpArray[index + 1:]
