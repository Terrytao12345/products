#二維清單
# class 62

products =[]



while True : 
	name = input('請輸入商品名稱 : \n')
	if name == 'q' :
		break
	price = input('請輸入商品價格 : \n')
	products.append([name, price])	
						# p = [] #小清單在迴圈
						# p.append(name) #加入小清單
						# p.append(price)
						#也等於
						# p = [name, price]
						# products.append(p)	
print(products)
# print(products[0])
# print(products[0][1])

for p in products :
	print(p) #印出products裡的小清單
	print(p[0], '的價格為', p[1]) #用小清單的位置列出商品和價格


# class 63 , 65(+標題和編碼)
# 商品寫入 #w

with open ('products.csv', 'w', encoding = 'utf-8' ) as f : #txt/csv
	f.write('商品,價格\n')#加入欄位名稱
	for p in products :
		f.write(p[0] + ',' + p[1] + '\n') # ',' 是為了檔案可視性分隔和excel 打開方便
