# Django ORM Queries

In this challenge you'll be working with a single model, `Product`. The database schema has already been created for you.


## Release 0: Setup
Create a virtual env. Start it up. Then tell pip to read the `requirements.txt` file and install all the requirements. 

```

python -m venv venv 

source venv/bin/activate

pip install -r requirements.txt

```

## Release 1: Pass the Tests

Once you've setup the app, your goal is to get all the tests passing. `cd` into `ormQueries` and run `python manage.py test` to see the tests fail.  You can also use the `--failfast` flag to only see one test at a time: `python manage.py test --failfast`.

The `ProductCrud` class has a number of functions for you to implement. As you work, follow the test file & review the function names carefully. You'll need to write class methods to make the tests pass. Also, some of the queries will require you to import some modules and functions from `django.db.models`. 


Need A Hint? Check out the available [Django QuerySet Cheatsheet](https://github.com/chrisdl/Django-QuerySet-Cheatsheet).
