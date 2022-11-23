def odwracanie(napis):
    if napis == "":
        return napis
    return odwracanie(napis[1:])+napis[0]


napis = str(input())
print(odwracanie(napis))
