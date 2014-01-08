=======
Project
=======

:date: 2010-10-03 10:20

Console Commands
================

Use py33.bat or ve\django142_v-env.bat

Versions
========

It is decided to develop multiple prototype versions:

* (main) Python version (probably with some performance critical java components), and 
* C# version, and
* (optional) Java version

to compare those technology and then make the final decision for the long term platform choice.

Currently, the Python version is temporarily considered as the main production codebase, other versions
will only be developed for learning and technology comparison purpose. However, this may be changed if
it is proven that using other technology, e.g. Java or C#, can deliver faster or better code.

When the final platform choice decision is made, all the other prototype codebases will released as open source projects.

Technology Stack
================
Misc
----

::

    [=+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    @@ 
    @@ [#2012-10-10_23:00:08]

    初步决定使用以下工具栈：

      commonJS  -- for 模块化，代码重用
    + dojo      -- for 界面组件
    + backbone  -- for MVC框架
    + 某一个python web server:
           bottle
        or cherry
        or tornado

    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+=]

Libs
----

**NDesk.Options 0.2.1**

* Description: A command line parser 

  Recommended by: http://stackoverflow.com/questions/491595/best-way-to-parse-command-line-arguments-in-c

* Location: \_lab\app_TimeInsight\vs\libs\ndesk-options\NDesk.Options.dll
* Download from: http://www.ndesk.org/Options
* Version in use: 0.2.1

Cloud Platform
--------------

Iaas candidates:

* Amazon EC2: with HAProxy, Django, mod_wsgi, Apache, MySQL, memcached [#f1]_
* Google Compute Engine https://cloud.google.com/pricing/compute-engine

Configurations
==============

* CI: Travis (recommended) or Jekins
  - Travis + selenium for web gui testing: http://about.travis-ci.org/docs/user/gui-and-headless-browsers/
* Others:

::

    [=+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    @@ 
    @@ [#2012-09-24_17:51:47]

    - four-digit version number: major.feature.bug.revision
    - all feature & bug fixing work are on branch, then merge to trunk (trunk 
      keeps stable for release)
    - create a script to read labels from hg to generate release notes and 
      update version numbers

    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+=]


.. rubric:: Footnotes

.. [#f1] from: `Scaling Django to 30,000 requests per second <http://attentionshard.wordpress.com/2011/04/26/scaling-django-to-30000-requests-per-second/>`_

