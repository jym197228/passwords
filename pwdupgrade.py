# 用while true
# 正確密碼為a123456
pwd = 'a123456' # 正確密碼
x = 3 # 剩餘次數
while True:
	password = input('請輸入密碼: ')
	if password == pwd:
		print('登入成功!')
		break
	else:
		x = x - 1
		if x == 0:
			print('密碼已被鎖定，請洽櫃台解鎖!')
			break
		else:
			print('密碼錯誤! 還有', x, '次機會。')