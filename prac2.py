
'''找出一串字符中最大和最小数字并输出

way1
def high_and_low(numbers):
  a = ' '.join(numbers.split())
  '先去掉空格，将string转化成数组'
  l = list(map(int, a.split()))
  '排序'
  m = sorted(l)
  d = str(m[-1]) + " " + str(m[0])
  return d

way2

def high_and_low(numbers):
    numbers.split(" ")
    n=[int(x)for x in numbers.split(" ")]
    print(max(n))

'''



numbers="4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
high_and_low(numbers)

