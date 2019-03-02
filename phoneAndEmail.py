#! usr/bin/env python3

import re ,pyperclip

# 電話番号の正規表現
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\)? # 市外局番　()があってもなくてもいい
    (\s|-|\.)? # スペースかハイフンかドット
    (\d{3}) # 3桁の番号
    (\s|-|\.)? # スペースかハイフンかドット 区切り
    (\d{4}) # 4桁の番号
    (\s*(ext|x|.ext)\s*(\d{2,5}))? に2から5桁の内線(extention)番号
    )''',re.VERBOSE)

# メールの正規表現

mail_regex = re.compile(r'''(
    [A-Za-z0-9._%+-]+ # ユーザー名 
    @ # @記号
    [A-Za-z0-9.-] # ドメイン名
    (\.[a-zA-Z]{2,4}) # comやjpなど
    )''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phone_num += 'x' + groups[8]
    matches.append(phone_num)
for groups in mail_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました:')
    print('\n'.join(matches))
else:
    print('番号やメールアドレスは見つかりませんでした')

