from django import forms

#  methods 1, 2, 3, 5, 7, 8, 14

class Single(forms.Form):
    number = forms.IntegerField()

#  method 4, 10

class Double(forms.Form):
    number1 = forms.IntegerField()
    number2 = forms.IntegerField()

#  method 6

class Chinese_Remainder_Theorem(forms.Form):
    list1 = forms.CharField()
    list2 = forms.CharField()

#  method 9

class Determinant(forms.Form):
    list = forms.CharField()

#  method 11

class Josephus_Problem(forms.Form):
    step = forms.IntegerField()
    Sequence = forms.CharField()

#  method 12

class Permutations(forms.Form):
    list = forms.CharField()
    positions = forms.IntegerField()
    Allow_Repetitions = forms.BooleanField()

#  method 13

class Combinations(forms.Form):
    list = forms.CharField()

#  method 15

class ModAll(forms.Form):
    list = forms.CharField()
    number = forms.IntegerField()