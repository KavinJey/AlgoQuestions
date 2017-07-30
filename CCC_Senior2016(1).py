firstString = input().strip()
secondString = input().strip()

def isAnagram(firstString, secondString):
    condition = True
    if len(firstString) != len(secondString):
        return False

    else:
        for b in firstString:
            if b not in secondString:
                return False

    return True


