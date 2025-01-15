
def eosum(lst):
  esum=0
  osum=0
  for i in lst:
    if i%2==0:
      esum=esum+i
    else:
      osum=osum+i
  return esum,osum      


