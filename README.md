## 主要功能：
- 文章，页面，分类目录，标签的添加，删除，编辑等。文章及页面支持`Markdown`，支持代码高亮。
- 支持文章全文搜索。
- 完整的评论功能，包括发表回复评论，以及评论的邮件提醒，支持`Markdown`。
- 侧边栏功能，最新文章，最多阅读，标签云等。
- 支持Oauth登陆，现已有Google,GitHub,facebook,微博登录。
- 支持`Memcache`缓存，支持缓存自动刷新。
- 简单的SEO功能，新建文章等会自动通知Google和百度。
- 集成了简单的图床功能。
- 集成`django-compressor`，自动压缩`css`，`js`。
- 网站异常邮件提醒，若有未捕捉到的异常会自动发送提醒邮件。
- 集成了微信公众号功能，现在可以使用微信公众号来管理你的vps了。

### 配置
配置都是在`setting.py`中.

很多`setting`配置我都是写在环境变量里面的.并没有提交到`github`中来.例如`SECRET_KEY`,`OAHUTH`,`mysql`以及邮件部分的配置等.你可以直接修改代码成你自己的,或者在环境变量里面加入对应的配置就可以了.

`test`目录中的文件都是为了`travis`自动化测试使用的.不用去关注.或者直接使用.这样就可以集成`travis`自动化测试了.

`bin`目录是在`linux`环境中使用`Nginx`+`Gunicorn`+`virtualenv`+`supervisor`来部署的脚本和`Nginx`配置文件.可以参考我的文章:

>[使用Nginx+Gunicorn+virtualenv+supervisor来部署django项目](https://www.lylinux.org/%E4%BD%BF%E7%94%A8nginxgunicornvirtualenvsupervisor%E6%9D%A5%E9%83%A8%E7%BD%B2django%E9%A1%B9%E7%9B%AE.html)

有详细的部署介绍.

为了安全起见，没有把`SECRET_KEY`上传到Github中而是在环境变量中配置的，如果你想要正常运行的话，需要修改`settings.py`中的`SECRET_KEY`为你自己的就可以了。
如：`SECRET_KEY = 'n9ceqv38)#&mwuat@(mjb_p%em$e8$qyr#fw9ot!=ba6lijx-6'`
若本地部署后发现静态文件无法加载.请将`settings.py`中的`DEBUG=False`修改为`DEBUG=True`即可.

## 运行

### 创建数据库

终端下执行:

    ./manage.py makemigrations
    python manage.py sqlmigrate polls 0001
    ./manage.py migrate
### 创建超级用户

 终端下执行:

    ./manage.py createsuperuser
### 创建测试数据
终端下执行:

    ./manage.py create_testdata
### 收集静态文件
终端下执行:  

    ./manage.py collectstatic --noinput
    ./manage.py compress --force

### check issue

    运行`python manage.py check`;这将检查您的项目中的任何问题，而不进行迁移或触摸数据库

### 开始运行：

```shell
python manage.py runserver 8080
```

如果你需改变服务器的IP地址，把IP地址和端口号放到一起。 因此若要监听所有的外网IP，请使用（如果你想在另外一台电脑上展示你的工作，会非常有用）：

```
python manage.py runserver 0.0.0.0:8000
```

 浏览器打开: http://127.0.0.1:8000/  就可以看到效果了。
## 更多配置:
[更多配置介绍](/bin/config.md)

### `wsgi.py`

[如何利用WSGI进行部署](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/)

### 模板组织方式

> 就像静态文件一样，我们可以把所有的模板都放在一起，
形成一个大大的模板文件夹，并且工作正常。但是不建议这样！
最好每一个模板都应该存放在它所属应用的模板目录内（例如polls/templates）
而不是整个项目的模板目录（templates），因为这样每个应用才可以被方便和正确的重用。

> 模板命名空间: 如果我们把模板直接放在polls/templates中（而不是创建另一个polls子目录），但它实际上是一个坏主意。 Django将选择它找到的名字匹配的第一个模板，如果你在不同的应用程序中有一个相同名称的模板，Django将无法区分它们。我们需要能够将Django指向正确的一个，确保这一点的最简单的方法是通过命名空间。也就是说，将这些模板放在为应用程序本身命名的另一个目录中。

	ex: Django是如何找到默认的admin模板呢？回答是: 如果`DIRS`默认是空的，由于`APP_DIRS`被设置为`True``，DjangoTemplates将在INSTALLED_APPS所包含的每个应用的目录下查找名为"templates"子目录（不要忘了django.contrib.admin也是一个应用）。如果`DIRS`不是空的，优先从`DIRS`下查找模板文件,如果要定制管理站点首页，需要重写`admin/index.html`模板，就像前面修改`base_site.html`模板的方法一样，然后从admin app
    目录拷贝到`DIRS`所设定的目录内。

* 请参考[如何重用apps (0%)](https://docs.djangoproject.com/en/1.10/intro/reusable-apps/)。
* Django如何加载模板文件的信息，请查看[模板加载 (0%)](https://docs.djangoproject.com/en/1.10/topics/templates/#template-loading)的文档。
	
### 静态文件

	Django提供了`django.contrib.staticfiles`：它收集每个应用（和任何你指定的地方）的静态文件到一个单独的位置，使得这些文件很容易维护。

	首先在`polls`路径中创建一个`static`目录。Django会从这里搜索静态文件，这个和Django在`polls/templates/`中查找对应的模板文件的方式是一样的。

　　Django有一个[STATICFILES_FINDERS](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-STATICFILES_FINDERS)的查找器，它会告诉Django从哪里查找静态文件。 其中有个内建的查找器`AppDirectoriesFinder`，它的作用是在每个`INSTALLED_APPS`下查找“static”子目录下的静态文件。管理站点的静态文件也是使用相同的目录结构。

>静态文件命名空间: 和模板类似，其实我们也可以直接将静态文件直接放在polls/static下面（而不是再创建一个polls子目录变成: polls/static/polls/css/style.css），但是这样是一个不好的行为。Django会自动使用它所找到的第一个符合要求的静态文件的文件名，如果你有在两个不同应用中存在两个同名的静态文件，那么Django是无法区分它们的。所以我们需要告诉Django该使用其中的哪一个，最简单的方法就是为它们添加命名空间。也就是将这些静态文件放进以它们所在的应用的名字命名的子目录下。

> 警告：{% static %} 模板标签在不是由 Django 生成的静态文件（比如样式表）中是不可用的。在以后开发过程中应该使用相对路径来相互链接静态文件，因为这样你可以只改变STATIC_URL（ static模板标签用它来生成URLs）而不用同时修改一大堆静态文件的路径。

`{%static%}`模板标签生成静态文件的绝对URL
其他更多详细信息，参见[静态文件howto](https://docs.djangoproject.com/en/1.10/howto/static-files/) 和[静态文件参考](https://docs.djangoproject.com/en/1.10/ref/contrib/staticfiles/)。[部署静态文件](https://docs.djangoproject.com/en/1.10/howto/static-files/deployment/)讲述如何在真实的服务器上使用静态文件。
请阅读本教程的[第7部分](https://docs.djangoproject.com/en/1.10/intro/tutorial07/)，了解如何自定义Django自动生成的管理站点。


### migrate

`python manage.py migrate`命令会找出所有还没有被应用的迁移文件（Django使用数据库中一个叫做django_migrations的特殊表来追踪哪些迁移文件已经被应用过），并且在你的数据库上运行它们。迁移功能非常强大，可以让你在开发过程中不断修改你的模型而不用删除数据库或者表然后再重新生成一个新的 —— 它专注于升级你的数据库且不丢失数据。

### shell

`python manage.py shell`, 然后才可以使用models.py中的Model,才可以通过orm对数据库进行操作
可以创建Model对象，并且访问对象的属性，也就是对应的field值

### generic view

* DetailView都是从URL中捕获名为"pk"的主键值，因此才需要把polls/urls.py中question_id改成了pk以使通用视图可以找到主键值。

> 默认情况下，DetailView泛型视图使用一个称作`<app name>/<model name>_detail.html`的模板。在本例中，实际使用的是`polls/question_detail.html`。template_name属性就是用来指定这个模板名的，用于代替自动生成的默认模板名。

　　在教程的前面部分，我们给模板提供了一个包含question和latest_question_list的上下文变量。而对于DetailView，question变量会被自动提供，因为我们使用了Django的模型（Question），Django会智能的选择合适的上下文变量。然而，对于ListView，自动生成的上下文变量是question_list。为了覆盖它，我们提供了context_object_name属性，指定说我们希望使用latest_question_list而不是question_list。

    抓住青春的尾巴，抓住时间的尾巴
    沙漏