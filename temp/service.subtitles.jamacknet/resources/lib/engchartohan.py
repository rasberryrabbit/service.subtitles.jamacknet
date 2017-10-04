# -*- coding: utf-8 -*-


# import unicodedata

engkey = "rRseEfaqQtTdwWczxvgkoiOjpuPhynbml"
kor_key = unicode(("ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ").decode('utf-8'))
cho_data = unicode(("ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ").decode('utf-8'))
jung_data = unicode(("ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ").decode('utf-8'))
jong_data = unicode(("ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ").decode('utf-8'))

def makehangul(ncho, njung, njong):
    return unichr(0xac00 + ncho * 21 * 28 + njung * 28 + njong + 1)

# english key string to hangul
def engtypetokor(src):
    res = ''
    if len(src)==0:
        return res
    ncho = -1
    njung = -1
    njong = -1
    for i in range(0, len(src)):
        ch = src.decode('utf-8')[i]
        p = engkey.find(ch)
        if p == -1:
            if ncho != -1:
                if njung != -1:
                    res += makehangul(ncho, njung, njong)
                else:
                    res += cho_data[ncho]
            else:
                if njung != -1:
                    res += jung_data[njung]
                elif njong != -1:
                    res += jong_data[njong]
            ncho = -1
            njung = -1
            njong = -1
            res += ch
        elif p < 19:
            if njung != -1:
                if ncho == -1:
                    res += jung_data[njung]
                    njung = -1
                    ncho = cho_data.find(kor_key[p])
                else:
                    if njong == -1:
                        njong = jong_data.find(kor_key[p])
                        if njong == -1:
                            res += makehangul(ncho,njung,njong)
                            ncho = cho_data.find(kor_key[p])
                            njung = -1
                    elif njong == 0 and p == 9:
                        njong = 2
                    elif njong == 3 and p == 12:
                        njong = 4
                    elif njong == 3 and p == 18:
                        njong = 5
                    elif njong == 7 and p == 0:
                        njong = 8
                    elif njong == 7 and p == 6:
                        njong = 9
                    elif njong == 7 and p == 7:
                        njong = 10
                    elif njong == 7 and p == 9:
                        njong = 11
                    elif njong == 7 and p == 16:
                        njong = 12
                    elif njong == 7 and p == 17:
                        njong = 13
                    elif njong == 7 and p == 18:
                        njong = 14
                    elif njong == 16 and p == 9:
                        njong = 17
                    else:
                        res += makehangul(ncho, njung, njong)
                        ncho = cho_data.find(kor_key[p])
                        njung = -1
                        njong = -1
            else:
                if ncho == -1:
                    if njong != -1:
                        res += jong_data[njong]
                        njong = -1
                    ncho = cho_data.find(kor_key[p])
                elif ncho == 0 and p == 9:
                    ncho = -1
                    njong = 2
                elif ncho == 2 and p == 12:
                    ncho = -1
                    njong = 4
                elif ncho == 2 and p == 18:
                    ncho = -1
                    njong = 5
                elif ncho == 5 and p == 0:
                    ncho = -1
                    njong = 8
                elif ncho == 5 and p == 6:
                    ncho = -1
                    njong = 9
                elif ncho == 5 and p == 7:
                    ncho = -1
                    njong = 10
                elif ncho == 5 and p == 9:
                    ncho = -1
                    njong = 11
                elif ncho == 5 and p == 16:
                    ncho = -1
                    njong = 12
                elif ncho == 5 and p == 17:
                    ncho = -1
                    njong = 13
                elif ncho == 5 and p == 18:
                    ncho =-1
                    njong = 14
                elif ncho == 7 and p == 9:
                    ncho = -1
                    njong = 17
                else:
                    res += cho_data[ncho]
                    ncho = cho_data.find(kor_key[p])
        else:
            if njong != -1:
                newcho = 0
                if njong == 2:
                    njong = 0
                    newcho = 9
                elif njong == 4:
                    njong = 3
                    newcho = 12
                elif njong == 5:
                    njong = 3
                    newcho = 18
                elif njong == 8:
                    njong = 7
                    newcho = 0
                elif njong == 9:
                    njong = 7
                    newcho = 6
                elif njong == 10:
                    njong = 7
                    newcho = 7
                elif njong == 11:
                    njong = 7
                    newcho = 9
                elif njong == 12:
                    njong = 7
                    newcho = 16
                elif njong == 13:
                    njong = 7
                    newcho = 17
                elif njong == 14:
                    njong = 7
                    newcho = 18
                elif njong == 17:
                    njong = 16
                    newcho = 9
                else:
                    newcho = cho_data.find(jong_data[njong])
                    njong = -1
                if ncho != -1:
                    res += makehangul(ncho,njung,njong)
                else:
                    res += jong_data[njong]
                ncho = newcho
                njung = -1
                njong = -1
            if njung == -1:
                njung = jung_data.find(kor_key[p])
            elif njung == 8 and p == 19:
                njung = 9
            elif njung == 8 and p == 20:
                njung = 10
            elif njung == 8 and p == 32:
                njung = 11
            elif njung == 13 and p == 23:
                njung = 14
            elif njung == 13 and p == 24:
                njung = 15
            elif njung == 13 and p == 32:
                njung = 16
            elif njung == 18 and p == 32:
                njung = 19
            else:
                if ncho != -1:
                    res += makehangul(ncho,njung,njong)
                    ncho = -1
                else:
                    res += jung_data[njung]
                njung = -1
                res += kor_key[p]
    if ncho != -1:
        if njung != -1:
            res += makehangul(ncho,njung,njong)
        else:
            res += cho_data[ncho]
    else:
        if njung != -1:
            res += jung_data[njung]
        else:
            if njong != -1:
                res += jong_data[njong]
    return res.encode('utf-8')


