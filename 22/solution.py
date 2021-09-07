with open("22/names.txt", "r") as f:
    raw = f.read()
raw = raw.split(",")
for i in range(len(raw)):
    raw[i] = raw[i].replace('"','')

s = sorted(raw)

sol = 0
for i, v in enumerate(s):
    # print(i,v)
    score = 0
    for j in v:
        score += ord(j) - 64
        # print("score", score)
    score *= i+1
    # print(sol, score)
    sol += score

print(sol)
