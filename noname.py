def digital_root(n: int):
    num = str(n)
    new = []
    for i in num:
        new.append(int(i))
    if len(new) >= 2:
        return digital_root(sum(new))
    else:
        return new[0]


print(digital_root(132189))
