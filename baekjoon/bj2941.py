# arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# cand = set(["c", "d", "l", "n", "s", "z"])
# word = input()
# cnt = len(word)
# for i in range(len(word)):
#     if word[i] in cand:
#         if word[i : i + 2] in arr:
#             cnt -= 1
#         elif word[i : i + 3] == "dz=":
#             cnt -= 1
# print(cnt)
word = input()
for i in range(len(word)):
    if "dz=" in word:
        word = word.replace("dz=", "1")
    elif "z=" in word:
        word = word.replace("z=", "2")
    elif "c=" in word:
        word = word.replace("c=", "3")
    elif "c-" in word:
        word = word.replace("c-", "4")
    elif "s=" in word:
        word = word.replace("s=", "5")
    elif "d-" in word:
        word = word.replace("d-", "6")
    elif "lj" in word:
        word = word.replace("lj", "7")
    elif "nj" in word:
        word = word.replace("nj", "8")
print(word)
