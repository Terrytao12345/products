#練習寫入檔案
#假設有一些整數裝在data清單裡，你想要一行一行的把這些數字寫到test.txt檔去，請寫出這樣的程式碼

data = [1, 3, 5, 7, 9] # 清單中裝著一些整數

with open('data_test.txt', 'w') as a :
	for i in data :
		a.write( str(i) + '\n')
		print(i)
	
