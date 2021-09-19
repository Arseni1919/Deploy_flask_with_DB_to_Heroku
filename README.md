# Flask with DB deployed to Heroku

Name of the app: flask-db-heroku-project

## Inside DB

```bash
heroku pg:psql --app <name of the app>
```

```sql
select * from <table name>;
```

## Pitfalls

- [Specifying a Python version](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version)
- [Specifying a Python Runtime](https://devcenter.heroku.com/articles/python-runtimes)
- set `SQLAlchemy==1.3.24` and not `SQLAlchemy==1.4.<`  with `pip install SQLAlchemy==1.3.24`
- 

## Credits

- [YouTube | Build & Deploy A Python Web App | Flask, Postgres & Heroku](https://www.youtube.com/watch?v=w25ea_I89iM&t=302s)