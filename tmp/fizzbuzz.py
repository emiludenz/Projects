def main():
	
	for i in range(100):
		print(fizzbuzz(3,5,i))


def fizzbuzz(f,b,count):
	res = ""
	print()
	if count % f == 0:
		res += "fizz"
	if count % b == 0:
		res += "buzz"
	if res == "":
		res = count
	return res


if __name__ == '__main__':
	main()