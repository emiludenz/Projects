def partition(array,low,high):
	i = (low-1)	
	pivot = array[high]
	for j in range(low,high):
		if array[j] >= pivot:
			i += 1
			array[i],array[j] = array[j],array[i]
	array[i+1],array[high] = array[high],array[i+1]
	return (i+1)


def qsort(array,low,high):
	if low < high:
		pi = partition(array,low,high)
		qsort(array,low,pi-1)
		qsort(array,pi+1,high)


def descending_order(num):
    num = list(str(num))
    qsort(num,0,len(num)-1)
    return int("".join(num))





print(descending_order(0), 0)
print(descending_order(15), 51)
print(descending_order(123456789), 987654321)

#arr = [10, 7, 8, 9, 1, 5] 
#n = len(arr) 
#qsort(arr,0,n-1) 
#print ("Sorted array is:") 
#for i in range(n): 
#    print ("%d" %arr[i]), 