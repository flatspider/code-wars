
s = "bitcoin take over the world maybe who knows perhaps"

s = s.split(" ")

print(s)

print(len(s))

shortest_word = "mostdefinitelythelongestwordofalltime"

for each in range(0, len(s)):
    if len(s[each]) < len(shortest_word):
        shortest_word = s[each]
        print(shortest_word)


l = len(shortest_word)

print(l)

# return l # l: shortest word length
