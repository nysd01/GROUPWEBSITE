pip install -r requirements.txt
#python3.9 manage.py collectstatic
#!/bin/bash
python3 manage.py collectstatic --noinput
python3 manage.py migrate
