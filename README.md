# Local library website built with Django
Partially based on [MDN tutorials](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).

I didn't just copy everything, but made significant improvements. And a design (i.e. appearance) was completely made by me.

## [How it looks (YouTube video)](https://www.youtube.com/watch?v=CYhmGYuMtfg)

## Project stack:

* Django
* Bootstrap
* PostgreSQL
* nginx
* gunicorn
* supervisor
* Let's Encrypt (Certbot)
* Ubuntu
* AWS EC2 VPS

File db.sqlite3 was added to repository just once after populating. Then it was converted to a new PostgreSQL database with [pgloader](https://pgloader.readthedocs.io/en/latest/). User-uploaded book covers are stored in the /media directory.


## The website will be available for a while at https://tconsta.online/
