def factorial(x):
  answer = 1

  for i in range(1, x+1):
    answer = answer * i
    print(i)
  return answer
