from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
import bcrypt

emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def registerUser(self, name, alias, email, password, confirmpass):
		errors = []

		if len(name) < 2: 
			errors.append("Name no fewer than two characters.")
		if len(alias) < 2:
			errors.append("Alias no fewer than two characters")	
		if not emailRegex.match(email):
			errors.append("Email not valid")	
		if len(password) < 8:
			errors.append("Password must be more than eight characters.")
		if not password == confirmpass:
			errors.append("Passwords do not match")
		return errors

		password = bcrypt.hashpw("password".encode(), bcrypt.gensalt())

	def loginUser(self, email, password):
		user = self.filter(email="email")
		if not user:
			return False
		else:
			user = user[0]

		if bcrypt.hashpw("password".encode(), user.password.encode()) == user.password:
			return user
		else:
			return False

	def poking(self, name, pokes): 
		pass

class User (models.Model):
	name = models.CharField(max_length=20)
	alias = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	confirmpass = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Pokes (models.Model):
	pokes = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
