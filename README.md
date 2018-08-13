# super
目录结构
```
.
├── =0.5.1
├── LICENSE
├── README.md
├── all.json
├── apps
│   ├── goods
│   ├── trade
│   ├── user_operation
│   ├── users
│   └── utils
├── db.sqlite3
├── db_tools
│   ├── data
│   ├── import_category_data.py
│   └── import_goods_data.py
├── dist
│   ├── index.html
│   └── static
├── extra_apps
│   ├── DjangoUeditor
│   ├── DjangoUeditor3-master
│   ├── django_admin_bootstrapped
│   ├── rest_framework
│   └── xadmin
├── manage.py
├── media
│   ├── a1.jpg
│   ├── banner
│   └── goods
├── requirements.txt
├── static
│   ├── admin
│   ├── rest_framework
│   ├── ueditor
│   └── xadmin
├── super
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates

```
拉取代码
```bash
git clone https://github.com/ZHAISHENKING/super.git
```
启动数据库，并新建数据库`shop`      

修改配置文件 settings.py
```python
# 数据库用mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "shop",
        'USER': 'root',
        'PASSWORD': '',
        'HOST': "",
        "OPTIONS":{"init_command":"SET default_storage_engine=INNODB;"},
    }
}
```
数据库迁移
```bash
python manage.py makemigrations
python manage.py migrate
# 超级用户
python manage.py createsuperuser
python manage.py runserver
```

登录后台
http://127.0.0.1:8000/xadmin
api文档
/api
/docs
前端页面
/
