import random
# input = '{an apple|can} {dance|extra} fight {{goat|height} ink|{jack|kite} life}'
input = "{I am|I'm} {working on|starting} this {online|internet}interview. I hope Cortx thinks I am {{very|extremely} qualified|great|awesome}{!|.}"
# input = '{this {specific|particular} example|an example {like|such as} this}'


def backtrack(str):
    l = str[1:-1].split("|")
    ran = random.choice(l)
    length = len(str)
    ran = ran.ljust(length)
    return ran


brac_indexs = []
l = len(input)
for i in range(l):
    if input[i] == '{':
        brac_indexs.append(i)
    elif input[i] == '}':
        index = brac_indexs.pop()
        input = input.replace(input[index:i+1],
                              backtrack(input[index:i+1]), 1)
input = input.split()
input = " ".join(input)
print(input)
