lowerCase = []
upperCase = []
names = []

def greet(name):
    names.clear()
    upperCase.clear()
    lowerCase.clear()

    if(name == None):
        return "Hello, my friend."

    if (isinstance(name, list)):
        parse_list(name)
    else:
        parse_string(name)
    parse_names()
    return return_string()

def parse_list(nameList):
    for i in nameList:
        parse_string(i)

def parse_string(string):
    quote = string.find('"')
    if(quote != -1):
        string = eval(string)
        names.append(string)
    else:
        names.extend(string.split(', '))

def parse_names():
    for i in names:
        if i.isupper():
            upperCase.append(i)
        else:
            lowerCase.append(i)


def return_string():
    result = ""

    if len(lowerCase) > 0:
        result += "Hello, "
    for i in range(len(lowerCase)-1):
        result += (lowerCase[i] + ", ")
    if len(lowerCase) > 1:
        result += "and "
    if len(lowerCase) > 0:
        result += lowerCase[-1]
    if len(lowerCase) > 0:
        result += "."

    if len(lowerCase) > 0 and len(upperCase) > 0:
        result += " AND "
    if len(upperCase) > 0:
        result += "HELLO, "
    for i in range(len(upperCase)-1):
        result += (upperCase[i] + ", ")
    if len(upperCase) > 1:
        result += "AND "
    if len(upperCase) > 0:
        result += upperCase[-1]
    if len(upperCase) > 0:
        result += "!"

    return result
    