## Installation

```shell
sudo apt-get install nginx
```

Now, we will configure Nginx to pass traffic to the process.

Create a file `/etc/nginx/sites-available/djtrump` and type in the following:

```shell
upstream project_socket {
	server unix:/home/xuzhijiang/project/app_deployment/myproject/myproject.socket fail_timeout=0;
}

server {
    listen 8000;
    server_name 0.0.0.0;

    keepalive_timeout 70;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /home/xuzhijiang/project/app_deployment/myproject;
    }

    location / {
            include proxy_params;
	    proxy_redirect off;

	    if (!-f $request_filename) {
		proxy_pass http://project_socket;
		break;
	    }
    }
}
```

Adjust the paths such as `/home/xuzhijiang/project/app_deployment/myproject` to your own environment.


Enable this file by linking it to the sites-enable folder:

```shell
sudo ln -fs /etc/nginx/sites-available/djtrump /etc/nginx/sites-enabled
```

and check if our configuration file was correctly written:

```shell
sudo nginx -t
```

If everything is OK, you should see something like this:

```shell
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

First, let's move all our static files to `/home/xuzhijiang/project/app_deployment/myproject/static/` because we set up Nginx to look for them there. Open up myproject/settings.py and add this:

```shell
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

Save and close. Now, let's collect them to that folder:

```shell
./manage.py collectstatic --clear
```

Confirm the operation and our static files should be there for Nginx to find them.

Now, let's finally run our app:

`gunicorn --workers 3 --bind unix:/home/xuzhijiang/project/app_deployment/myproject/myproject.socket myproject.wsgi`

let's restart Nginx to make these changes take effect:

```shelpassword

sudo service nginx restart
```

![Reference](http://rahmonov.me/posts/run-a-django-app-with-gunicorn-in-ubuntu-16-04/)