
result = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ln = line.split()
        result.append((ln[0], ln[5].strip('"'), ln[6]))

print(result)
