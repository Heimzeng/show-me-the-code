def gcd(a,b):
  if a < b:
    a,b = b,a
  while b != 0:
    print (a,b)
    temp = a % b
    a = b
    b = temp
  return a
if __name__ == '__main__':
  a = input('please input the first number:')
  b = input('please input the second number:')
  print ('the gcd is %d' %gcd(a,b))
