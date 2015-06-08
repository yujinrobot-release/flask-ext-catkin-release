#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=[
        'flask_cors',
        'flask_restful',
        'flask_migrate',
        'flask_security',
        'flask_wtf',
        'flask_sqlalchemy',
        'flask_script'
    ],
    package_dir={
        'flask_cors': 'flask-cors',
        'flask_restful': 'flask-restful',
        'flask_migrate': 'flask-migrate',
        'flask_security': 'flask-security',
        'flask_login': 'flask-login',
        'flask_principal': 'flask-principal',
        'flask_mail': 'flask-mail',
        'flask_script': 'flask-script',
        'flask_wtf': 'flask-wtf',
        'flask_sqlalchemy': 'flask-sqlalchemy',
        'flask_redis_helper': 'flask-redis-helper',
        'flask_celery_helper': 'flask-celery-helper'
    },
    py_modules=[
        'flask_login',
        'flask_principal',
        'flask_mail',
        'flask_redis_helper',
        'flask_celery_helper'
    ],
    # TODO : flask required to run these...
)

setup(**d)
