#!/usr/bin/env bash

NAME="djangoblog"
DJANGODIR=/var/www/DjangoBlog
SOCKFILE=/var/www/DjangoBlog/run/gunicorn.sock
USER=root
GROUP=root
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=DjangoBlog.settings
DJANGO_WSGI_MODULE=DjangoBlog.wsgi
# worker的数量推荐设置为2 * CPUs + 1，这样的话，在任何时候都有一半的worker在做IO.

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /var/www/dev/python3/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /var/www/dev/python3/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=-
