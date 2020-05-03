products = []

while True:
	name = input('請輸入商品名稱：')
	if name == 'q': #逃出迴圈
		break
	price = input('請輸入商品價格：') # 2維度清單
	p = [] # 建立一個新清單（清單中的清單）
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

# line 8-11 可寫成 products.append([name, price])

# products[0][0] # 第一個[0]為products的第0格,第二個[0]是products清單中第0格中p清單中的第0格

for p in products:
	print(p[0], '的價格是', p[1])