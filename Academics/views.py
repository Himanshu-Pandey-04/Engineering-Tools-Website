from django.shortcuts import render
from Fusion import *
# Create your views here.

Dict = {
    'Maths': {
        'sieve': {
            'docS': 'SIEVE OF ERASTOSTHENES :- Computes Sieve of Eratosthenes',
            'params': {'Number': 'number'},
            'returns': {'r1': 'list'}
        },
        'prime_factors': {
            'docS': 'PRIME FACTORS :- Computes List of Prime Factors',
            'params': {'Number': 'number'},
            'returns': {'r1': 'list'}
        },
        'prime_check': {
            'docS': 'PRIME CHECK :- Checks if a Number is Prime / Composite / Neither Prime nor Composite',
            'params': {'Number': 'number'},
            'returns': {'r1': 'int'}
        },
        'co_prime': {
            'docS': 'CO-PRIME :- Checks Whether Given Pair of Numbers are Co-Prime',
            'params': {'Number_1': 'number', 'Number_2': 'number'},
            'returns': {'r1': 'unknown'}
        },
        'signum': {
            'docS': 'SIGNUM :- Checks Sign of Number   Range = { -1, 0, 1 }',
            'params': {'Number': 'number'},
            'returns': {'r1': 'number'}
        },
        'chinese_remainder_theorem': {
            'docS': 'CHINESE REMAINDER THEOREM :- Implements CRT on Given Divisor and Remainder Arrays',
            'params': {'Divisor_Array': 'range', 'Remainder_Array': 'range'},
            'returns': {'r1': 'number'}
        },
        'euler_totient_function': {
            'docS': 'EULER TOTIENT FUNCTION :- Computes ETF for given Number',
            'params': {'Number': 'number'},
            'returns': {'r1': 'number'}
        },
        'inverse_euler_totient_function': {
            'docS': 'INVERSE EULER TOTIENT FUNCTION :- Computes IETF for given Number',
            'params': {'Number': 'number'},
            'returns': {'r1': 'number'}
        },
        'determinant': {
            'docS': 'JUST ONE LINE DETERMINANT CALCULATOR :- Calculates Determinant of given Matrix',
            'params': {'Mat': 'range'},
            'returns': {'r1': 'number'}
        },
        'last_digit_determiner': {
            'docS': 'PRINTS LAST DIGIT OF EXPONENTIAL RESULT :- Determines Last Digit of Result (Base ^ Exp)',
            'params': {'Base': 'number', 'Exponent': 'number'},
            'returns': {'r1': 'number'}
        },
        'josephus_problem': {
            'docS': 'JOSEPHUS PROBLEM :- Theoretical problem related to a certain counting-out game',
            'params': {'Step': 'number', 'Sequence': 'range'},
            'returns': {'r1': 'number'}
        },
        'permutations': {
            'docS': 'PERMUTATIONS :- Returns List of All Possible Permutations of Input Data',
            'params': {'Elements': 'range',
            'Positions': 'number',
            'Allow_Repetitions': 'unknown'},
            'returns': {'r1': 'range'}
        },
        'combinations': {
            'docS': 'COMBINATIONS :- Returns List of All Possible Combinations of Input Data',
            'params': {'Elements': 'range', 'Positions': 'number'},
            'returns': {'r1': 'range'}
        },
        'fibonacci': {
            'docS': 'FIBONACCI :- Provides fibonacci result upto 998\n    n -> depicts element position in the fibonacci sequence\n    ',
            'params': {'n': 'number'},
            'returns': {'r1': 'number'}
        },
        'modall': {
            'docS': "MODALL :- Performs modulus(%) operation on given elements in 'List' w.r.t. 'Number'",
            'params': {'List': 'range', 'Number': 'number'},
            'returns': {'r1': 'range'}
        },
        'congruent_modulo': {
            'docS': "CONGRUENT_MODULO :- Groups 'List' elements giving identical modulus value w.r.t. 'Number'",
            'params': {'List': 'range', 'N': 'number'},
            'returns': {'r1': 'unknown'}
        }
    },
    'LDCO': {

    },
    'BCN': {
        
    }
}

Func_Lib = { 
    "sieve": Sieve, "prime_factors": Prime_Factors, "prime_check": Prime_Check, "co_prime": Co_Prime, "signum": Signum, "chinese_remainder_theorem": Chinese_Remainder_Theorem, "euler_totient_function": Euler_Totient_Function, "inverse_euler_totient_function": Inverse_Euler_Totient_Function, "determinant": Determinant, "last_digit_determiner": Last_Digit_Determiner, "josephus_problem": Josephus_Problem, "permutations": Permutations, "combinations": Combinations, "fibonacci": Fibonacci, "modall": ModAll 
}


def home(request):
    context = {
        'links': Dict,
    }
    return render(request, 'index.html', context)


def calculation(request, subName, funcName):
    result, breadcrumbs, code, number = [], [], [], []
    breadcrumbs.append(subName)
    breadcrumbs.append(funcName)
    for key, value in Dict[subName][funcName]['params'].items():
        code.append(f'<input name="{key}" type="{value}"/><br>')
    if request.method == 'POST':
        for key, value in Dict[subName][funcName]['params'].items():
            number.append(request.POST[key])
        print(type(number[0]))
        result = Func_Lib[funcName](*number)
    context = {
        'htmlcode': code,
        'result': result,
        'BC' : breadcrumbs,
    }
    return render(request, 'subjectTopicsTemp.html', context)


# def calculation(request, funcName):
#     Func_Lib = { 
#         "sieve": [Sieve, Double], "prime_factors": Prime_Factors, "prime_check": Prime_Check, "co_prime": Co_Prime, "signum": Signum, "chinese_remainder_theorem": Chinese_Remainder_Theorem, "euler_totient_function": Euler_Totient_Function, "inverse_euler_totient_function": Inverse_Euler_Totient_Function, "determinant": Determinant, "last_digit_determiner": Last_Digit_Determiner, "josephus_problem": Josephus_Problem, "permutations": Permutations, "combinations": Combinations, "fibonacci": Fibonacci, "modall": ModAll 
#     }
#     result = []
#     form = Func_Lib[funcName][1](request.POST or None)
#     # 1 form, 
#     if funcName == 'sieve':
#         form.fields['number2'].required = False
#     if request.method == 'POST':
#         # multiple forms, 
#         number = request.POST.get('number1')
#         result = Func_Lib[funcName][0](int(number))
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/sieve.html', context)

#region Functions

# def Sieve(request):
#     result = []
#     form = Single(request.POST or None)
#     if request.method == 'POST':
#         number = request.POST.get('number')
#         result = f.Sieve(int(number))
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/sieve.html', context)

# def Prime_Factors(request):
#     result = ''
#     form = Single(request.POST or None)
#     if request.method == 'POST':
#         number = request.POST.get('number')
#         result = f.Prime_Factors(int(number))
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/prime_factors.html', context)

# # prime_check
# def prime_check(request):
#     result = ''
#     form = Single(request.POST or None)
#     if request.method == 'POST':
#         number = request.POST.get('number')
#         result = f.Prime_Check(int(number))
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/prime_check.html', context)

# # signum
# def signum(request):
#     result = ''
#     form = Single(request.POST or None)
#     if request.method == 'POST':
#         number = request.POST.get('number')
#         result = f.Signum(int(number))
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/signum.html', context)

# # euler_totient
# def euler_totient(request):
#     result = ''
#     form = Single(request.POST or None)
#     if request.method == 'POST':
#         number = request.POST.get('number')
#         result = f.Euler_Totient_Function(int(number))
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/euler_totient.html', context)

# # inverse_euler_totient
# def inverse_euler_totient(request):
#     result = ''
#     form = Single(request.POST or None)
#     if request.method == 'POST':
#         number = request.POST.get('number')
#         result = f.Inverse_Euler_Totient_Function(int(number))
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/inverse_euler_totient.html', context)

# # fibonacci
# def fibonacci(request):
#     result = ''
#     form = Single(request.POST or None)
#     if request.method == 'POST':
#         number = request.POST.get('number')
#         result = f.Fibonacci(int(number))
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/fibonacci.html', context)

# def Chinese_Remainder(request):
#     result = ''
#     form = Chinese_Remainder_Theorem(request.POST or None)
#     if request.method == 'POST':
#         list1 = request.POST.get('list1')
#         list2 = request.POST.get('list2')
#         a = list1.strip().split()
#         b = list2.strip().split()
#         # result = f.Chinese_Remainder_Theorem(a.list1.strip().split(),b.list2.strip().split())
#         result = a
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/chinese_remainder.html', context)

# def Last_Digit_Determiner(request):
#     result = ''
#     form = Double(request.POST or None)
#     if request.method == 'POST':
#         number1 = request.POST.get('number1')
#         number2 = request.POST.get('number2')
#         result = f.Last_Digit_Determiner(number1, number2)
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/last_digit_determiner.html', context)

# def co_prime(request):
#     result = ''
#     form = Double(request.POST or None)
#     if request.method == 'POST':
#         number1 = request.POST.get('number1')
#         number2 = request.POST.get('number2')
#         result = f.Co_Prime(number1, number2)
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/co_prime.html', context)

# def determinant(request):
#     result = ''
#     form = Determinant(request.POST or None)
#     if request.method == 'POST':
#         list1 = request.POST.get('list1')
#         result = f.Determinant(list1.strip().split())
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/determinant.html', context)

# def josephus_problem(request):
#     result = ''
#     form = Josephus_Problem(request.POST or None)
#     if request.method == 'POST':
#         step = request.POST.get('step')
#         sequence = request.POST.get('sequence')
#         result = f.Josephus_Problem(step, sequence.strip().split())
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/josephus_problem.html', context)

# def permutations(request):
#     result = ''
#     form = Permutations(request.POST or None)
#     if request.method == 'POST':
#         list = request.POST.get('list')
#         positions = request.POST.get('positions')
#         Allow_Repetitions = request.POST.get('allow_repetitions')
#         result = f.Permutations(list.strip().split(), positions, Allow_Repetitions)
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/permutations.html', context)

# def combinations(request):
#     result = ''
#     form = Combinations(request.POST or None)
#     if request.method == 'POST':
#         list = request.POST.get('list')
#         result = f.Combinations(list)
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/combinations.html', context)

# def modAll(request):
#     result = ''
#     form = ModAll(request.POST or None)
#     if request.method == 'POST':
#         list = request.POST.get('list')
#         number = request.POST.get('number')
#         # result = f.ModAll(list.strip().split(), number)
#         result = list.strip().split()
#     context = {
#         'form':form,
#         'result': result
#     }
#     return render(request, 'maths/modAll.html', context)

#endregion
