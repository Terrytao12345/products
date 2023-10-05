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
print(products[0])
print(products[0][1])
