original_pwd = 'a123456'
try_count = 3 #剩餘機會
 
while try_count>0:
    trial = input ('what is your password ?')
    if trial == original_pwd:
        print('sucessfully login')
        break # 跳出迴圈
    elif trial != original_pwd and try_count > 1 :
        try_count = try_count - 1
        print ('password is not correct, you still can try',try_count, 'times')
    else:
        print ('game over')