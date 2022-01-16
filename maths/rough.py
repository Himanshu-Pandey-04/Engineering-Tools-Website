
# functionrom functionusion import *

# functionunc_Lib = { 
#   "sieve": Sieve, "prime_functionactors": Prime_functionactors, "prime_check": Prime_Check, "co_prime": Co_Prime, "signum": Signum, "chinese_remainder_theorem": Chinese_Remainder_Theorem, "euler_totient_functionunction": Euler_Totient_functionunction, "inverse_euler_totient_functionunction": Inverse_Euler_Totient_functionunction, "determinant": Determinant, "last_digit_determiner": Last_Digit_Determiner, "josephus_problem": Josephus_Problem, "permutations": Permutations, "combinations": Combinations, "functionibonacci": functionibonacci, "modall": ModAll 
# }

# functionor key in functionunc_Lib.keys():
#   print(function"<a hrefunction=\"{{% url 'mathsTopcis' {key} %}}\"><li class=\"topic\">{key}</li></a>")



def diff(a, b, x, y):
  return ((abs(a-x)**2) + (abs(b-y)**2))**0.5

points = []
for i in range(int(input())):
  x = int(input())
  y = int(input())
  a = [x, y]
  points.append(a)

max = 0
for i in range(len(points)-1):
  for j in range(i+1, len(points)):
    dis = diff(points[i][0], points[i][1], points[j][0], points[j][1])
    if dis > max: max = dis

print(max)

# points.sort()
# c = diff(points[0][0], points[0][1], points[len(points)-1][0], points[len(points)-1][1])
# sorted(points, key=lambda x: x[1])
# points.sort(key=lambda x:int(x[1]))
# d = diff(points[0][0], points[0][1], points[len(points)-1][0], points[len(points)-1][1])
# print(max(c, d))


# print(diff(315, 271, -952, 482))
# print(diff(-2, -621, -952, 482))

# [315, 271], [-2, -621], [-205, -511], [-952, 482], [165, 463]