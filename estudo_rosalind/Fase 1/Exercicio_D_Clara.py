#-------------Encontro 3---------------#
#---Rabbits and Recurrence Relations---#

# months k-pairs

def fibonacy_rabits(m, k):
  child = 1
  adults = 0
  for n in range(m-1):
     temp = adults*k
     adults += child
     child = temp
     #child, adult = adults*k, adults+=child
  return adults+child

fibonacy_rabits(31, 4)
