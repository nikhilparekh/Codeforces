Arr = [1,3,2,2]
Target = 4

def pairSum(arr,target):
	lo = 0
	hi = len(arr)-1
	arr = sorted(arr)
	
	while(lo<hi):
		if(arr[lo]+arr[hi]==target):
			print("({},{})".format(arr[lo],arr[hi]))
			hi-=1
			lo+=1
		elif(arr[lo]+arr[hi]>target):
			hi-=1
		else:
			lo+=1

pairSum(Arr,Target)
