# -*- coding: utf-8 -*-

_PREF = {
    "010006": {"name": "北海道", "group1": "01"},
    "020001": {"name": "青森県", "group1": "01"},
    "030007": {"name": "岩手県", "group1": "01"},
    "040002": {"name": "宮城県", "group1": "01"},
    "050008": {"name": "秋田県", "group1": "01"},
    "060003": {"name": "山形県", "group1": "01"},
    "070009": {"name": "福島県", "group1": "01"},
    "080004": {"name": "茨城県", "group1": "02"},
    "090000": {"name": "栃木県", "group1": "02"},
    "100005": {"name": "群馬県", "group1": "02"},
    "110001": {"name": "埼玉県", "group1": "02"},
    "120006": {"name": "千葉県", "group1": "02"},
    "130001": {"name": "東京都", "group1": "02"},
    "140007": {"name": "神奈川県", "group1": "02"},
    "150002": {"name": "新潟県", "group1": "03"},
    "160008": {"name": "富山県", "group1": "03"},
    "170003": {"name": "石川県", "group1": "03"},
    "180009": {"name": "福井県", "group1": "03"},
    "190004": {"name": "山梨県", "group1": "03"},
    "200000": {"name": "長野県", "group1": "03"},
    "210005": {"name": "岐阜県", "group1": "03"},
    "220001": {"name": "静岡県", "group1": "03"},
    "230006": {"name": "愛知県", "group1": "03"},
    "240001": {"name": "三重県", "group1": "04"},
    "250007": {"name": "滋賀県", "group1": "04"},
    "260002": {"name": "京都府", "group1": "04"},
    "270008": {"name": "大阪府", "group1": "04"},
    "280003": {"name": "兵庫県", "group1": "04"},
    "290009": {"name": "奈良県", "group1": "04"},
    "300004": {"name": "和歌山県", "group1": "04"},
    "310000": {"name": "鳥取県", "group1": "05"},
    "320005": {"name": "島根県", "group1": "05"},
    "330001": {"name": "岡山県", "group1": "05"},
    "340006": {"name": "広島県", "group1": "05"},
    "350001": {"name": "山口県", "group1": "05"},
    "360007": {"name": "徳島県", "group1": "05"},
    "370002": {"name": "香川県", "group1": "05"},
    "380008": {"name": "愛媛県", "group1": "05"},
    "390003": {"name": "高知県", "group1": "05"},
    "400009": {"name": "福岡県", "group1": "06"},
    "410004": {"name": "佐賀県", "group1": "06"},
    "420000": {"name": "長崎県", "group1": "06"},
    "430005": {"name": "熊本県", "group1": "06"},
    "440001": {"name": "大分県", "group1": "06"},
    "450006": {"name": "宮崎県", "group1": "06"},
    "460001": {"name": "鹿児島県", "group1": "06"},
    "470007": {"name": "沖縄県", "group1": "06"},
}

def getAreaName(areaCode):
    for code, info in _PREF.items():
        if areaCode == code:
            return info['name']
    assert False, 'no area code : %s' % areaCode

def getAreaGroup(groupCode):
    r = []
    for code, info in _PREF.items():
        if info['group1'] == groupCode:
            r.append({'area_code': code, 'area_name': info['name'], })
    if r:
        return r
    assert False, 'no area group : %s' % groupCode

def getAreaCode(name):
    for c, v in _PREF.items():
        if v['name'] == name:
            return c
    assert False, 'no name : %s' % name

#[EOF]