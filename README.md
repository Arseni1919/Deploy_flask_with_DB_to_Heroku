# Flask with DB deployed to Heroku

Name of the app: flask-db-heroku-project
Website: [https://flask-db-heroku-project.herokuapp.com/](https://flask-db-heroku-project.herokuapp.com/)

## Inside python of Heroku project

```bash

```

## Inside DB

```bash
heroku pg:psql --app <name of the app>
```

```sql
select * from <table name>;
```

## Pitfalls & Tricks

- [Specifying a Python version](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version)
- [Specifying a Python Runtime](https://devcenter.heroku.com/articles/python-runtimes)
- set `SQLAlchemy==1.3.24` and not `SQLAlchemy==1.4.<`  with `pip install SQLAlchemy==1.3.24`
- [Use SQL with `flask_sqlalchemy`](https://stackoverflow.com/a/22084672/13993545)
- [What does Autogenerate Detect (and what does it not detect?) during `flask db migrate -m "...migration message"`](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect)
- [Show tables in your db:](https://stackoverflow.com/a/769706/13993545)
First, choose your database:
```bash
\c database_name
```
Then, this shows all tables in the current schema:
```bash
\dt
```

## Credits

- [YouTube | Build & Deploy A Python Web App | Flask, Postgres & Heroku](https://www.youtube.com/watch?v=w25ea_I89iM&t=302s)
- [YouTube | REST API With Flask & SQL Alchemy](https://www.youtube.com/watch?v=PTZiDnuC86g)
- [Migration with `flask-migrate`](https://flask-migrate.readthedocs.io/en/latest/)
- [blog | Developing a Flask Web App with a PostreSQL Database - Making all the Possible Errors](https://blog.theodo.com/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/)