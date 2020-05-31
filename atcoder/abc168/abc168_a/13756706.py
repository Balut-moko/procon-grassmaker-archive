N = int(input())
ans = N%10
if ans== 3:
	print('bon')
elif ans == 0 or ans == 1 or ans == 6 or ans == 8:
	print('pon')
else:
    print('hon')