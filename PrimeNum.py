
def isPrime(num):
    isPrime = True
    for i in range(2,num/2):
        if num%i==0:
          isPrime = False
          break
    return isPrime
    

def Main():
  n = int(raw_input("Enter range: "))
  for i in range(2,n+1):
      if(isPrime(i)):
          print "The number ",i,"is Prime",isPrime(i)


Main()
