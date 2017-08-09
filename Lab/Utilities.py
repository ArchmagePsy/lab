import shutil

def search_until(array, target, key = lambda item: item):
    results = []
    for item in array:
        if key(item) == target:
            results.append(item)
        else:
            break
    return results

def binary_search(array, target, key = lambda item: item):
    results = []
    searching = True
    minimum = 0
    maximum = len(array) - 1
    while True:
        if minimum > maximum:
            break
        mean = (minimum + maximum) // 2
        current = key(array[mean])
        if current == target:
            results += search_until(reversed(array[:mean]), target)
            results.append(array[mean])
            results += search_until(array[mean + 1:], target)
            break
        elif current < target:
            minimum = mean + 1
        elif current > target:
            maximum = mean - 1
    return results

def set_env(name, value):
    shutil.os.environ[name] = str(value)

def get_env(name):
    return shutil.os.environ[name]

def sort_by(array, by = None):
    return sorted(array, key = lambda item: getattr(item, by) if hasattr(item, by) else None) if by != None else sorted(array)

def mutate_dict(func, dictionary):# yeah I stole this, thx gens and Ned Batchelder from SO
    for key, value in dictionary.iteritems():
        dictionary[key] = func(value)
    return dictionary
