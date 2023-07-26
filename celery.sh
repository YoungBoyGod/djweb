#!/bin/bash

# Celery worker command
celery -A demo worker -l info &

# Celery beat command
celery -A demo beat -l info