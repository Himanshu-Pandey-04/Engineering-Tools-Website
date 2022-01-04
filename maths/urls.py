from os import name
from django.contrib import admin
from django.urls import path
from .views import ( calculation, maths
    # Sieve, signum, Chinese_Remainder, 
    # Prime_Factors, prime_check,
    # euler_totient, inverse_euler_totient, fibonacci,
    # Last_Digit_Determiner,co_prime, determinant, 
    # josephus_problem,permutations, 
    # combinations, modAll
)

urlpatterns = [
    path('', maths, name='maths'),
    path('<str:funcName>/', calculation, name='sieve'),
    # path('sieve/', Sieve, name='sieve'),
    # path('chinese/', Chinese_Remainder),
    # path('signum/', signum, name='signum'),
    # path('prime_factor/', Prime_Factors, name='prime_factors'),
    # path('prime_check/', prime_check, name='prime_check'),
    # path('euler_totient/', euler_totient, name='euler_totient'),
    # path('inverse_euler_totient/', inverse_euler_totient,name='inverse_euler_totient'),
    # path('fibonacci/', fibonacci, name='fibonacci'),
    # path('last_digit_determiner/', Last_Digit_Determiner, name='last_digit_determiner'),
    # path('co_prime/', co_prime, name='co_prime'),
    # path('determinant/', determinant, name='determinant'),
    # path('josephus_problem/', josephus_problem, name='josephus_problem'),
    # path('permutations/', permutations, name='permutations'),
    # path('combinations/', combinations, name='combinations'),
    # path('mod_all/', modAll, name='modAll')
]