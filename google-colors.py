def googleColors(s):
    """ Exercise function for print Google colors logo from an string """
    vogal = "aeiouAEIOU"
    str = ""
    a = ""
    for i in s:
        if i in vogal:
            if a in vogal:
                str += "\033[33m" + i
            else:
                str += "\033[31m" + i
        else:
            if a not in vogal and a != " ":
                str += "\033[32m" + i
            else:
                str += "\033[34m" + i
        a = i
    print(str)


st = "Google feat Microsoft feat Yahooooooo!!!"
googleColors(st)
