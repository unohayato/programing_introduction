
n = int(input("数値を入力してください"))
ret = 0
while ret**3 < abs(n):
  ret += 1
if ret**3 != abs(n):
  print(n, "は完全立方ではないです")
else:
  if n < 0:
    ret = -ret
  print(n, "の立方根は", ret, "です") 