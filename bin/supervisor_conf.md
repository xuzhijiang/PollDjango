## Installation and Setup

`sudo apt-get install supervisor`

Now, restart it:

`sudo service supervisor restart`

let's create myproject.conf in `/etc/supervisor/conf.d/` folder:

`sudo vim /etc/supervisor/conf.d/myproject.conf` and type the following:

```shell
[program:myproject]
command=/bin/bash -c 'source /home/xuzhijiang/project/DjangoProject/bin/gunicorn_conf.sh'
directory=/home/xuzhijiang/
autostart=true
autorestart=true
stderr_logfile=/var/log/myproject.err.log
stdout_logfile=/var/log/myproject.out.log
```

Let's save the file and execute the following commands to bring these changes into effect:

```shell
sudo supervisorctl reread
sudo supervisorctl update
```

To verify that everything is working, type this:

`ps ax | grep gunicorn`

you can now use supervisor to check whether your app is running:

`sudo supervisorctl status myproject`

Open up /etc/supervisor/supervisor.conf and place these lines at the beginning of the file:

```shell
[inet_http_server]
port=0.0.0.0:9001
```

Save the file and reload supervisor:

`sudo supervisorctl reload`

Open up your browser and go to 0.0.0.0:9001. 

![Reference](http://rahmonov.me/posts/run-a-django-app-with-nginx-gunicorn-and-supervisor/)