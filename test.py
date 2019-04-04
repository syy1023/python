def high_and_low(numbers):
  a = ' '.join(numbers.split())
  l = list(map(int, a.split()))
  m = sorted(l)
  d = str(m[-1]) + " " + str(m[0])
  return d




  # ...
  #return numbers
numbers="4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");

high_and_low(numbers)