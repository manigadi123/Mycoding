def printValue(s1,s2):
    len1=len(s1)
    len2=len(s2)
    if len1>len2:
        return s1
    elif len1<len2:
        return s2
    else:
        return s1+s2

print printValue("manikanta","manichandhan")
