def is_prime(num):
	if num == 1 or num == 2:
		return True
	for i in range(2,num):
		if num%i == 0:
			return False
	return True

def main():
	for i in range(1,100):
		if is_prime(i):
			print(i)

if __name__ == '__main__':
	main()