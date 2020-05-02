def fibb(a):
	num = []
	b=0
	while b<a:
		if b==0 or b==1:
			num.append(1)
		else:
			num.append(num[b-2] + num[b-1])
		b=b+1
	return num
print(fibb(15))