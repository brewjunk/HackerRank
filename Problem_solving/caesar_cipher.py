#Caesar Cipher | HackerRank

s = '!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U'
k = 62%26
abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesarCipher(s, k):
    result = ''
    for sub in s:
        if sub.isalpha():
            if sub.isupper():
                L = (ABC.find(sub))
                #print(ABC[L+k])
                result += ABC[L+k]
            else:
                U = (abc.find(sub))
                if U + k > 25:
                    x = ((U+k)-25)
                    #print(abc[x-1])
                    result += abc[x-1]
                else:
                    #print(abc[U+k])
                    result += abc[U+k]
        else:
            result += sub

    return result

print(caesarCipher(s,k))

