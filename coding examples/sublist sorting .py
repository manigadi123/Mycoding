def sort(sub_li):
    """
    :param sub_li: pass the sub_li
    :return:return the output assending order
    """
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if sub_li[j][1] > sub_li[j + 1][1]:
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li
print(sort([[1,2,3],[32,34,23],[-9,0,1]]))
