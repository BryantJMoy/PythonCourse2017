def hasNumber(inputString):
    return any(char.isdigit() for char in inputString)


#Hello. to HELLO!
def shout(txt):
    if txt[-1] == ".":
        new_txt = txt.upper()
        new_txt = new_txt[:-1]
        new_txt = new_txt + "!"
        return new_txt
    elif hasNumber(txt) == True:
        raise Exception, "Cannot include numbers"
    else:
        raise Exception, "Must end with a period"




# Name to emaN
def reverse(txt):
    txt = str(txt)
    n1_txt = txt.split()
    if len(n1_txt) == 1:
        new_txt = txt[::-1]
    else:
        raise Exception, "Must be one word"
    return str(new_txt)



# Hello world! to world! Hello
def reversewords(txt):
    if hasNumber(txt) == True:
        raise Exception, "Cannot include numbers"
    else:
        new_txt = txt.split()
        new_txt = new_txt[::-1]
        new_txt = " ".join(new_txt)
        return new_txt

# Hello world! to !dlrow olleH
def reversewordletters(txt):
    if hasNumber(txt) == True:
        raise Exception, "Cannot include numbers"
    else:
        new_txt = txt[::-1]
        return new_txt


#To try out try and except(if this error, print)
def test_func(txt):
    try:
        int(txt)
    except ValueError:
        print "We'd handle this here..."
    return txt
