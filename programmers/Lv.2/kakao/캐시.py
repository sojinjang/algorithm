def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    time = 0
    cache = []
    for item in cities:
        city = item.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            time += 5

    return time
