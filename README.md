The Customer Management System (CMS) is a application designed to assist businesses in organizing, storing, and managing customer-related information. It aims to streamline customer interactions, facilitate data accessibility, and enhance customer relationship management.

Installation
  git clone https://github.com/shubhampythondev/customer-management-system.git
cd customer-management-system
Activate virtual environment source Scripts/activate in GNU/Linux (or) Scripts\activate.bat in Windows
cd cms
python manage.py makemgrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser and enter information as instructions
python manage.py runserver or python manage.py runsslserver for https
Open http://127.0.0.1:8000 or https://127.0.0.1:8000 in web browser
