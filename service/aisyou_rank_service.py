pointlist =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 50, 100, 20, 20, 50, 100, 0, 20, 30, 20, 50, 50, 40],
    [0, 100, 50, 50, 40, 50, 50, 20, 30, 20, 40, 50, 20, 10],
    [0, 0, 60, 70, 10, 40, 20, 90, 30, 10, 10, 20, 20, 50],
    [0, 20, 70, 40, 60, 20, 20, 20, 0, 100, 70, 10, 20, 10],
    [0, 80, 0, 80, 20, 0, 70, 70, 30, 10, 10, 40, 10, 40],
    [0, 90, 30, 80, 40, 40, 30, 0, 0, 40, 40, 10, 20, 40],
    [0, 10, 50, 80, 30, 90, 0, 60, 30, 20, 40, 20, 10, 50],
    [0, 30, 100, 60, 10, 20, 30, 20, 60, 10, 10, 40, 50, 20],
    [0, 10, 100, 30, 60, 0, 70, 60, 10, 100, 40, 10, 20, 50],
    [0, 20, 90, 20, 60, 10, 40, 40, 0, 50, 50, 10, 10, 20],
    [0, 50, 90, 10, 60, 40, 10, 20, 40, 20, 10, 40, 10, 40],
    [0, 70, 20, 90, 20, 50, 50, 0, 50, 20, 40, 10, 40, 10],
    [0, 40, 0, 40, 80, 20, 40, 100, 10, 50, 10, 20, 10, 10]
]

members = [
    {'id':0, 'name':'水野ふえ', 'birthday':'19950422', 'soulno':5},
    {'id':1, 'name':'森下舞桜', 'birthday':"20021111", 'soulno':8},
    {'id':2, 'name':'月野もあ', 'birthday':"19940307", 'soulno':33},
    {'id':3, 'name':'小島夕佳', 'birthday':"19960320", 'soulno':3},
    {'id':4, 'name':'猪狩ともか', 'birthday':"19911206", 'soulno':11},
    {'id':5, 'name':'涼邑芹', 'birthday':"19980805", 'soulno':4},
    {'id':6, 'name':'陽向こはる', 'birthday':"19980729", 'soulno':9},
    {'id':7, 'name':'蒼井乃々愛', 'birthday':"20020405", 'soulno':4},
    {'id':8, 'name':'波澄あいる', 'birthday':"20061211", 'soulno':4},
    {'id':9, 'name':'田中玲衣奈', 'birthday':"20001031", 'soulno':7},
    {'id':10, 'name':'野崎ゆりか', 'birthday':"20001029", 'soulno':5},
    {'id':11, 'name':'大神彩', 'birthday':"19990705", 'soulno':4},
]

def aisyou_check(no):
    for member in members:
        soulno = member['soulno']

        if soulno == 11:
            soulno = 10
        elif soulno == 22:
            soulno = 11
        elif soulno == 33:
            soulno = 12
        elif soulno == 44:
            soulno =13
        soulpoint = pointlist[no][soulno]
        member['point'] = soulpoint
        #member.append(soulpoint)

    sort_members = sorted(members, key=lambda x: x['point'], reverse=True)
    
    rank = 0
    previous_point = 0
    for sort_member in sort_members:
        if previous_point != sort_member['point']:
            rank += 1
        sort_member['rank'] = rank
        previous_point = sort_member['point']
    
    return sort_members
