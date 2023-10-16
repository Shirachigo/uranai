"""
 doulnoの計算をする。
 数値の配列を取得し、１件ずつ足す。
"""
def soulno_keisan(numbers):
    soulno = 0
    for number in numbers:
        soulno = soulno + int(number)
    return soulno


"""
　soulno計算のメイン関数。
　こちらの関数を呼び出して、soulnoを取得する。
"""
def get_soulno(birthday):
    birthday_list = list(birthday)
    soulno = soulno_keisan(birthday_list)
    if soulno == 11:
        return soulno
    elif soulno == 22:
        return soulno
    elif soulno == 33:
        return soulno
    elif soulno == 44:
        return soulno
    elif soulno < 10:
        return soulno
    else:
        soulno_list = list(str(soulno))
        soulno = soulno_keisan(soulno_list)
        if soulno == 11:
            return soulno
        elif soulno == 22:
            return soulno
        elif soulno == 33:
            return soulno
        elif soulno == 44:
            return soulno
        elif soulno < 10:
            return soulno
        else:
            soulno_list = list(str(soulno))
            soulno = soulno_keisan(soulno_list)
            return soulno
