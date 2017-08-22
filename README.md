## University Register
Single API RESTful created with Django/Django Rest Framework to create/list:

* Universities
* Students
* Professors
* Courses

## Use

The project use python 3

* Clone the repository

    `git clone https://github.com/lfbos/university-register.git`

* Access to the project folder

    `cd university-register`

* Create python environment

    * Virtualenvwrapper: using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/):

        ```
        mkvirtualenv env_name --python=python3
        pip install -r requirements.txt
        ```

    * Virtualenv: using [virtualenv](https://virtualenv.pypa.io/en/stable/):

        ```
        virtualenv env
        source env/bin/activate
        pip install -r requirements.txt
        ```

* Migrate database `python manage.py migrate`

* Execute `python manage.py runserver` and go to [http://localhost:8000/](http://localhost:8000/)


## Endpoints

* /api/universities/:

    - Methods: POST/GET
    - Response: pk (primary key), name
    - Fields:

        - name: type string


* /api/students/:

    - Methods: POST/GET
    - Response: pk, first name, last name, dni, university pk, course list
    - Fields:

        - first_name: type string
        - last_name: type string
        - dni: type string
        - university: type string (university pk)
        - courses (optional): course pks list

* /api/professors/:

    - Methods: POST/GET
    - Response: pk, first name, last name, dni, university pk, profession
    - Fields:

        - first_name: type string
        - last_name: type string
        - dni: type string
        - university: type string (university pk)
        - courses (optional): course pks list

* /api/courses/:

    - Methods: POST/GET
    - Response: name, professor pk
    - Fields:

        - name: type string
        - professor: professor pk

* /api/assign_courses/:

    - Methods: POST
    - Response: 'Courses assigned successfully'
    - Fields:

        - student: student pk
        - courses: course pks list
