#!/bin/env bash

cd ..

python manage.py syncdb --noinput
python manage.py loaddata liquidfeedback/fixtures/demo_data.json
