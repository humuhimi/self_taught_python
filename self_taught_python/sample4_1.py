# try:
#     d = "tryerror"
#     10 / 0
#     c = "I will never get defined"#例外前に定義していない変数は定義されない
# except (ZeroDivisionError,ValueError):
#     print(d)
#     print(c)

#
# def Sample(x,y,z,a=1,b=2,c=3):
#     pass
#
# def Sample2(x):
#     return x / 2
#
# def Sample3(y):
#     return y * 4
#
# x = Sample2(2)
#
# y = Sample3(x)
#
# print(y)
#
# def convert(string):
#     try:
#         return float(string)
#
#     except(SyntaxError,TypeError):
#         print('型か値が間違っています')
#
# c = convert("123")
# print(c)

# colors = ["purple","orange","green"]
# guess = input("何色でしょうか(入力してください)")
# if guess in colors:
#     print('当たり!')
# else:
#     print('外れまた今度ね')
#
# samp = ("1984","aa","bb")
# print("a" in samp)#in taple
# print("1985" not in samp)#not in taple
#
# bill = {"Bill Gates" : "charitable"}
# "Bill Gates" in bill
# print(bill)
#
# del bill["Bill Gates"]
# print(bill)
tv = ["a","B","c"]
# i = 0;
# for show in tv:
#     new = tv[i]
#     new = new.upper()
#     tv[i] = new;
#     i += 1
# print(tv)
for i,new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)








