# 密碼重試
# 正確密碼為a123456
x = 0
while x < 3:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功!')
		break
	else: 
		x = x + 1
		if x == 3:
			print('密碼已被鎖定，請洽櫃台解鎖!')
			break
		else:
			print('密碼錯誤! 還有', 3 - x, '次機會。')