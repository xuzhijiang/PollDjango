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

### 更多配置:
[更多配置介绍](/bin/config.md)

#### 模板组织方式

> 就像静态文件一样，我们可以把所有的模板都放在一起，
形成一个大大的模板文件夹，并且工作正常。但是不建议这样！
最好每一个模板都应该存放在它所属应用的模板目录内（例如polls/templates）
而不是整个项目的模板目录（templates），因为这样每个应用才可以被方便和正确的重用。

> 模板命名空间: 如果我们把模板直接放在polls/templates中（而不是创建另一个polls子目录），但它实际上是一个坏主意。 Django将选择它找到的名字匹配的第一个模板，如果你在不同的应用程序中有一个相同名称的模板，Django将无法区分它们。我们需要能够将Django指向正确的一个，确保这一点的最简单的方法是通过命名空间。也就是说，将这些模板放在为应用程序本身命名的另一个目录中。

	ex: Django是如何找到默认的admin模板呢？回答是: 如果`DIRS`默认是空的，由于`APP_DIRS`被设置为`True``，DjangoTemplates将在INSTALLED_APPS所包含的每个应用的目录下查找名为"templates"子目录（不要忘了django.contrib.admin也是一个应用）。如果`DIRS`不是空的，优先从`DIRS`下查找模板文件,如果要定制管理站点首页，需要重写`admin/index.html`模板，就像前面修改`base_site.html`模板的方法一样，然后从admin app
    目录拷贝到`DIRS`所设定的目录内。
	
#### static file

##### staticfiles App

`django.contrib.staticfiles` expose three management command.
使用这3个命令，saticfiles App(`django.contrib.staticfiles`)可以搜集静态文件，查找静态文件，etc.

`python manage.py collectstatic --help`

###### collectstatic命令的作用

要搜集的静态文件的源将会在`STATICFILES_FINDERS`中包含的FINDERS中去搜集，默认是在`django.contrib.staticfiles.finders.FileSystemFinder`以及`django.contrib.staticfiles.finders.AppDirectoriesFinder`中查找,前者对应`STATICFILES_DIRS`变量对应的目录，后者对应于在INSTALLED_APPS中对应的所有app下的`static`的目录下去搜集,把静态文件搜集到`STATIC_ROOT`中,如果搜集过程中有多个名字相同的文件，将把
找到的第一个文件放到`STATIC_ROOT`中，在后续的`collectstatic`运行中（如果`STATIC_ROOT`不为空），仅当文件的修改时间戳大于`STATIC_ROOT`中文件的时间戳时才复制文件。 因此，如果从INSTALLED_APPS中删除应用程序，最好使用`collectstatic --clear`选项以删除过时的静态文件。

###### findstatic

`python manage.py findstatic css/base.css admin/js/core.js`
`findstatic --first`

##### STATIC_ROOT

Settings for django.contrib.staticfiles.

> The absolute path to the directory where collectstatic will collect static files for deployment.就是collectstatic命令搜集静态文件，集中存放的地方

##### STATIC_URL

> 引用位于STATIC_ROOT中的静态文件时使用的URL。

##### STATICFILES_DIRS

在`STATICFILES_FINDERS`启用了FileSystemFinder查找器时，
`django.contrib.staticfiles`将会遍历静态文件的位置

##### STATICFILES_FINDERS

查找器列表，表示在哪些位置查找静态文件。

> 静态文件命名空间: 和模板类似，其实我们也可以直接将静态文件直接放在polls/static下面（而不是再创建一个polls子目录变成: polls/static/polls/css/style.css），但是这样是一个不好的行为。Django会自动使用它所找到的第一个符合要求的静态文件的文件名，如果你有在两个不同应用中存在两个同名的静态文件，那么Django是无法区分它们的。所以我们需要告诉Django该使用其中的哪一个，最简单的方法就是为它们添加命名空间。也就是将这些静态文件放进以它们所在的应用的名字命名的子目录下。

### migrate

`python manage.py migrate`命令会找出所有还没有被应用的迁移文件（Django使用数据库中一个叫做django_migrations的特殊表来追踪哪些迁移文件已经被应用过），并且在你的数据库上运行它们。迁移功能非常强大，可以让你在开发过程中不断修改你的模型而不用删除数据库或者表然后再重新生成一个新的 —— 它专注于升级你的数据库且不丢失数据。

### shell

`python manage.py shell`, 然后才可以使用models.py中的Model,才可以通过orm对数据库进行操作
可以创建Model对象，并且访问对象的属性，也就是对应的field值

### generic view

1. DetailView都是从URL匹配字符串中捕获名为"pk"的主键值，因此才需要把polls/urls.py中question_id改成了pk以使通用视图可以找到主键值。

2. By default，DetailView使用`<app name>/<modelname>_detail.html`模板。In this case，用的是`polls/question_detail.html`。

3. 对于ListView，默认的context_object_name是<modelname>_list,为了覆盖它,我们给context_object_name赋值为latest_question_list