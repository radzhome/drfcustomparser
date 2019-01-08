# Purpose

Reproduces issue when using custom json parser with "raw data" create or update in the UI.

# Step by step

Used python 3.7.2 to reproduce.

1. run `pip3 install -r requirements.txt`

2. run `python3 manage.py runserver`

3. login using `admin:admin`, http://127.0.0.1:8000/api-auth/login/?next=/api-root/videos/

4. go to edit UI, http://127.0.0.1:8000/api-root/tasks/1/

5. select "raw data for the edit" 

6. use: {"name": "test", "owner": "test2"} and "PUT" 

7. Notice the change fails, see runserver output, see data vs body

8. Change the DEFAULT_PARSER_CLASSES back to default parser and repeat, problem is gone (data QueryDict is no longer empty)
