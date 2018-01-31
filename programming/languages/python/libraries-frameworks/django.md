`django-admin startproject xxx`创建`project`
`python manage.py runserver`会自动加载修改，但新增文件需要重启
`project`和`app`是多对多的
`Template namespacing`,默认的template backend为`DjangoTemplates`会在所有installed_apps中查找
使用`{% url %} `避免硬编码的url
多个app情况下，url最好使用`Namespacing URL names`, 通过设置`app_name`
`{% csrf_token %}`内置的csrf保护机制
POST请求后添加一个redirect，避免用户点击back后重新提交表单
generic views
