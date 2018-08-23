#!/usr/bin/env bash

NAME="myproject"
DJANGODIR=/home/xuzhijiang/project/app_deployment
SOCKFILE=${DJANGODIR}/${NAME}/${NAME}.socket
# USER=root
# GROUP=root
# worker的数量推荐设置为2 * CPUs + 1，这样的话，在任何时候都有一半的worker在做IO.
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=${NAME}.settings
DJANGO_WSGI_MODULE=${NAME}.wsgi

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd ${DJANGODIR}/${NAME}
source ${DJANGODIR}/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

cd ${DJANGODIR}/${NAME}
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ${DJANGODIR}/venv/bin/gunicorn ${NAME}.wsgi:application \
--name $NAME \
--workers $NUM_WORKERS \
--bind=unix:$SOCKFILE \
--log-level=info \
--log-file=-
# Note that: must be source gunicorn_conf.sh to take effect.