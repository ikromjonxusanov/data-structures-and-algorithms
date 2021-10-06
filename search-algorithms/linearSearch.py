

def linearSearch(list, item):
    for n in range(len(list)):
        if list[n]==item:
            return n
    return None