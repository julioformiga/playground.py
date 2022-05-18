def googleColors(string):
    """
    Exercise function for print Google colors logo from an string
    """
    vogal = "aeiouAEIOU"
    string_out = ""
    a = ""
    for i in string:
        if i in vogal:
            if a in vogal:
                string_out += "\033[33m" + i
            else:
                string_out += "\033[31m" + i
        else:
            if a not in vogal and a != " ":
                string_out += "\033[32m" + i
            else:
                string_out += "\033[34m" + i
        a = i
    print(string_out)


googleColors("Google feat Microsoft feat Yahooooooo!!!")
