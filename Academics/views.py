from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail, get_connection, EmailMessage
from final import get_html
from emails.models import Querie
from users.models import Customer
# Create your views here.

code = get_html()

def home(request):
    context = {
        'links': code,
    }
    return render(request, 'index.html', context)

# def contact(request):
#     if request.method == "POST":
#         # connection = get_connection()
#         # connection.open()
#         message_query = request.POST['query']
#         message_email = request.POST['email']
#         send_mail("Customer query", message_query, message_email, ['janhavihimanshu@gmail.com'], fail_silently=False)
#         # connection.close()
#     return render(request, 'email.html', {})

def contactus(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        message_query = request.POST.get('query')
        message_email = request.POST.get('email')
        try:
            user = Customer.objects.filter(username=request.user.username).get()
            email = Querie.objects.create(fname=fname, lname=lname, email=message_email, QueryDesc=message_query)
            user.queries.add(email)
        except Customer.DoesNotExist:
            try:
                email = Querie.objects.filter(email=message_email).get()
                messages.error(request, "Sorry you can only make one query without an account.")
            except Querie.DoesNotExist:
                email = Querie.objects.create(fname=fname, lname=lname, email=message_email, QueryDesc=message_query)
        context = {
            'email' : email,
            }

    return render(request, 'email.html', context)

def calculation(request, subName, funcName):
    # result, breadcrumbs, code, number = [], [], [], []
    # breadcrumbs.append(subName)
    # breadcrumbs.append(funcName)
    # for key, value in dictionary[subName][funcName]['params'].items():
    #     code.append(f'<input name="{key}" type="{value}"/><br>')
    # if request.method == 'POST':
    #     for key, value in dictionary[subName][funcName]['params'].items():
    #         number.append(request.POST[key])
    #     print(type(number[0]))
    #     result = funclib[funcName](*number)
    # context = {
    #     'htmlcode': code,
    #     'result': result,
    #     'BC' : breadcrumbs,
    # }
    return render(request, 'subjectTopicsTemp.html', {})


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
