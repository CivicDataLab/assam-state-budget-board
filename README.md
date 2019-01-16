# Assam State Budget Board

The Assam State Budget Board is a collaborative effort as part of OpenBudgetsIndia initiative to facilitate an informed discussion on the Assam State Budget, by improving the accessibility of budget data.  

### Features
List coming Soon!

### Requirenments
Refer to Django/Python compatibility for Django-CMS - [Link](http://docs.django-cms.org/en/latest/#django-python-compatibility-table)
This project uses MySQL as it database. If you want to connect it to different database, you can refer to [Django Documentation](https://docs.djangoproject.com/en/2.1/ref/databases/). SQLite is a good alternative for simpler use cases, which also comes as a default database.   

### Installation

```
# Setup MySQL(Optional - You can use a different database as per your liking. Just make the suitable changes in settings.py)
$ sudo apt-get install mysql-server 
(Additional for Python 3)
$ sudo apt-get install libmysqlclient-dev

# Setup Development environment
$ virtualenv env  
$ source env/bin/activate

# Clone Repository
$ git clone https://github.com/CivicDataLab/assam-state-budget-board.git 
$ cd assam-state-budget-board

# Install all dependencies
$ pip install -r requirements.txt

# Apply data migrations
python manage.py migrate

# Run the server
$ python manage.py runserver
```

##### Create an admin user
```
$ python manage.py createsuperuser
```

### Contribute
Standard OSS rules. 

### Credits

### License
The project is licensed under the MIT license.
