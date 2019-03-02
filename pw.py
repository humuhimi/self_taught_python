#! /usr/bin/env python3
# pw.py - パスワード管理プログラム(脆弱性あり)

PASSWARDS = {'email' : 'abwwofns','blog' : 'amendsa','luggage' : '12345'}

import sys
import pyperclip


if len(sys.argv) < 2:
    print('使い方:python pw.py [アカウント名]')
    print('パスワードをコピーします')
    sys.exit()

account = sys.argv[1] # 最初のコマンドライン引数がアカウント名

if account in PASSWARDS:
    pyperclip.copy(PASSWARDS[account])
    print(account + 'のパスワードはコピーされました')
else:
    print(account + 'というアカウントは存在しません')


