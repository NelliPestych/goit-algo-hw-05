import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    def build_last(pattern):
        last = {}
        for i in range(len(pattern)):
            last[pattern[i]] = i
        return last

    last = build_last(pattern)
    n = len(text)
    m = len(pattern)
    i = m - 1
    j = m - 1
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            lo = last.get(text[i], -1)
            i = i + m - min(j, 1 + lo)
            j = m - 1
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256
    q = 101
    n = len(text)
    m = len(pattern)
    h = 1
    p = 0
    t = 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1

# Вимірювання часу виконання
def measure_time(algorithm, text, pattern):
    start = timeit.default_timer()
    algorithm(text, pattern)
    end = timeit.default_timer()
    return end - start

with open('data/стаття 1.txt', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open('data/стаття 2.txt', 'r', encoding='utf-8') as f:
    text2 = f.read()

patterns = ["алгоритм", "немає у тексті"]

results = []

for text, name in [(text1, 'стаття 1'), (text2, 'стаття 2')]:
    for pattern in patterns:
        bm_time = measure_time(boyer_moore, text, pattern)
        kmp_time = measure_time(kmp_search, text, pattern)
        rk_time = measure_time(rabin_karp, text, pattern)
        results.append((name, pattern, bm_time, kmp_time, rk_time))

for result in results:
    print(f"Текст: {result[0]}, Підрядок: {result[1]}, Боєр-Мур: {result[2]:.6f}s, КМП: {result[3]:.6f}s, Рабін-Карп: {result[4]:.6f}s")
