# Problem 1
#
# What option should I add in a field if I want to allow null values in that column?
# Bring an example.

# class Musician(models.Model):
#     first_name = models.CharField(max_length=50, null=True)

# Problem 2
#
# What options should I add in a field if I want to allow the user not to insert anything but I dont want that field to be null so I give it a default value.
# Bring an example.

# class Musician(models.Model):
#     first_name = models.CharField(null=False)


# Problem 3
#
# If I created two new apps (user and car) what should I add in INSTALLED_APPS list of settings.py?
#
# INSTALLED_APPS = [
#
#     'user.apps.UserConfig',
#     'car.apps.CarConfig'
# ]

# Problem 4
#
# After changes were made in the models.py what commands I should run to syncronize the db with the new changes?
# set DJANGO_SETTIGS_MODULE=user.settings
# set DJANGO_SETTINGS_MODULE=car.settings


# Problem 5
#
# Imagine you have to create a table for university students. The field 'student_year' should be either Freshman, Sophomore, Junior or Senior.
# Make the model class. (Student can also have name, surname and major).

# class Student(models.Model):
#     student_year = models.DateField()
#     freshman = models.CharField(max_length=50)
#     sophomore = models.CharField(max_length=50)
#     junior = models.CharField(max_length=50)
#     senior = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     major = models.DateField()

# Problem 6
#
# Create a Person and Address classes. Each person can have only one address but there can be more than one person who can have the same address.
# Address has fields street, house, city and person. Person has fields first_name and last_name.
# Create 2 person objects. Then create 2 address objects for those 2 person objects where the street, house, city are the same. (Do this in shell and paste your commands here.)

# class Person(models.Model):
#     fn = models.CharField(max_length=50)
#     ln = models.CharField(max_length=100)
#
#
# class Adress(models.Model):
#     street = models.CharField(max_lenghth=100)
#     city = models.CharField(max_lenghth=100)
#     person = models.ForreignKey(Person, on_delete=models.CASCADE)
