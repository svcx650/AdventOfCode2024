target = 33411698619881

for i in range(100):
	x = (5**i)
	if x >= target:
		print('5 to the ', i, ' power')
		print('is ', x,' which is ',x-target,' above target')
		break
''' 5 to the 20 is 95367431640625 which is
87914899426 above the target '''