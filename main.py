# Модуль 4 урок 1 Оптимизация кода.
# >>> aaabca
# <<< a : 4, b : 1, c : 1

'''s = 'aaabca'
for sym in s:
    count = 0
    for sub_sym in s:
        if sub_sym == sym:
            count += 1

    print(sym, count)

# O(N) = N * N = 2 * 2'''

'''s = 'aaabca'
#print(set(s)) # поиск уникальных символов
for sym in set(s):
    count = 0
    for sub_sym in s:
        if sub_sym == sym:
            count += 1

    print(sym, count)

# O(N) = M * N, где M - кол-во  уникальных символов'''

'''s = 'aaabca'
syms_counter = {}
for sym in s:
    syms_counter[sym] = syms_counter.get(sym, 0) + 1

print(syms_counter)'''