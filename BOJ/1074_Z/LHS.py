
shape = input().split()
N = int(shape[0])
R = int(shape[1])
C = int(shape[2])


def visit_count(n, r, c):
  if n == 1:
    return 2*r + c
  rsub = r // 2**(n-1)
  csub = c // 2**(n-1)
  base = int((2**n * 2**n)/2*rsub + (2**n * 2**n)/4*csub)
  rnew = r % 2**(n-1)
  cnew = c % 2**(n-1)
  return base + visit_count(n-1, rnew, cnew)

print(visit_count(N, R, C))


 
