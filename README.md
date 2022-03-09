# UA-Help
A website associating users / institutions / companies who actively participate in helping the victims of the Ukrainian-Russian war.

### How to generate fixtures
```shell script
python manage.py dumpdata --indent 4 app_name auth.user > filename.json
```

### How to load fixtures

```shell script
python manage.py loaddata app_name\fixtures\filename.json
```

