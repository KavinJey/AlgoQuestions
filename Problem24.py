#Borrowed from question 35
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

#turning list of ints into one number
def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)


list_of_items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_perms = []

for perms in all_perms(list_of_items):
    print(perms, len(list_of_perms))
    perms_number = magic(perms)
    list_of_perms.append(perms_number)



list_of_perms.sort()

print(list_of_perms, "\n" ,list_of_perms[999999], list_of_perms[1000000])