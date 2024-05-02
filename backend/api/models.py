from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Budget(models.Model):
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Expense(models.Model):
    newExpense = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    newExpenseAmount = models.DecimalField(max_digits=10, decimal_places=2)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
