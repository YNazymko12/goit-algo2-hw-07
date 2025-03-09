import random
import time
from functools import lru_cache

# Генерація масива
N = 100000
array = [random.randint(1, 1000) for _ in range(N)]

# Генерація випадковий запитів
Q = 50000
queries = []
for _ in range(Q):
    if random.random() < 0.5:
        L, R = sorted(random.sample(range(N), 2))
        queries.append(('Range', L, R))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 1000)
        queries.append(('Update', index, value))

# Функція без кеша
def range_sum_no_cache(arr, L, R):
    return sum(arr[L:R+1])

def update_no_cache(arr, index, value):
    arr[index] = value

# Кеш для суми діапазонів
cache_size = 1000
@lru_cache(maxsize=cache_size)
def range_sum_with_cache(L, R):
    return sum(array[L:R+1])

def update_with_cache(index, value):
    global array, range_sum_with_cache
    array[index] = value
    range_sum_with_cache.cache_clear()

# Тестування без кеша
start_no_cache = time.time()
for query in queries:
    if query[0] == 'Range':
        range_sum_no_cache(array, query[1], query[2])
    else:
        update_no_cache(array, query[1], query[2])
end_no_cache = time.time()

time_no_cache = end_no_cache - start_no_cache

# Тестування з кешем
start_with_cache = time.time()
for query in queries:
    if query[0] == 'Range':
        range_sum_with_cache(query[1], query[2])
    else:
        update_with_cache(query[1], query[2])
end_with_cache = time.time()

time_with_cache = end_with_cache - start_with_cache

print(f"Час виконання без кешування: {time_no_cache:.2f} секунд")
print(f"Час виконання з LRU-кешем: {time_with_cache:.2f} секунд")
