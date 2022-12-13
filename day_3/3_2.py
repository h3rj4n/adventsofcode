answer = 0

with open("3_data.txt") as f:
    cache = []
    for i, line in enumerate(f):
        cache.append(line)
        if i + 1 > 0 and (i + 1) % 3 == 0:
            for char in cache[0]:
                val = 0

                for search in cache[1:]:
                    if search.find(char) >= 0:
                        val += 1

                if val == 2:
                    c = ord(char)

                    if c > 96:
                        answer += c - 96
                    else:
                        answer += c - 38
                    
                    break
            cache = []

print(answer)