word = 'banana'

result = {}

for char in word:
    #만약에 기존에 키가 없으면 1으로 초기화 하고
    if char not in result:
        result[char] = 1
    #키가 있으면 기존 값에 더하자!
    else:
        result[char] = result[char] + 1

print(result)




