#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. 

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

Version = 0.2
setup ( name='django-banish',
        version = Version,
        install_requires='python-memcached',
        description = "django middleware to ban users, prevent too many concurrent connections",
        long_description = "django-banish is a django middleware app to banish user agents by IP addresses or User Agent Header. It also supports basic abuse prevention by automatically banning users if they exceed a certain number of requests per minute which is likely some form of attack or attemped denial of service.",
        author = "Yousef Ourabi",
        author_email = "yourabi@gmail.com",
        url = "http://github.com/yourabi/django-banish",
        packages = ['banish',],
        license = 'Apache',
        platforms = 'Posix; MacOS X;',
        classifiers = [
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
     )
