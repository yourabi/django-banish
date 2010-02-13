django-banish
====

django-banish is django middleware app to banish user agents by IP addresses or User Agent Header. It also supports basic abuse prevention by automatically banning users if they exceed a certain number of requests per minute which is likely some form of attack or attemped denial of service.

Django-banish stores all the 'banishments' in memory to avoid DB lookup on every request. It requires memcached, especially for the IP abuse monitoring feature.

django-banish was previously called django-ipban and hosted on google-code. That code should be ignored - In 2010 it was dusted off and given a new life at github.


Installation
------------

Requirements:

* Python 2.5+
* Django
* Memcache 

Get django-banish 
--------

Browse the source on GitHub: <http://github.com/yourabi/django-banish>

Clone with Git:
    $ git clone git://github.com/yourabi/django-banish


Setup
------
Install django-banish. Make sure it is on your PYTHONPATH or in your django project directory.

In your django project settings.py you must set the following options:
    1) Add 'banish.middleware.BanishMiddleware' to MIDDLEWARE_CLASSES
    2) Add 'banish' to INSTALLED_APPS
    3) Add BANISH_ENABLED = True to enable Django-Banish (handy if you lock yourself out)
    4) Optionally set BANSIH_ABUSE_THRESHOLD (default is 75) to the threshold of requests per minute

Issues
------
Find a bug? Want a feature? Submit an [issue
here](http://github.com/yourabi/django-banish/issues). Patches welcome!

License
------
django-banish is released under the Apache Software License, Version 2.0


Authors
-------
 * [Yousef Ourabi][1]


 [1]: http://github.com/yourabi
