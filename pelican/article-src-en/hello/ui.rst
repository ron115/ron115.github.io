==============
User Interface
==============

:date: 2013-12-23 10:20
:summary: User User User User User User User User User User User User User User User User User 
    User User User User User User User User User User User User User User User User User User 
    User User User User User User User User User User User User User User User User User User 

.. contents::

Misc
====

Test embed html:

.. raw:: html

    <h1>hello</h1>
    <h2>hello</h2>

    <i class="icon-note"></i>
    <i class="icon-heart"></i>
    <i class="icon-flag"></i>
    <i class="icon-github"></i>
    

* Need to provide a "download" button to download the user data to local machine 

  [TBD] Download all or just a part of user data?

::

    [=+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    @@ 
    @@ [#2012-11-06_16:53:19]

    用下面的方式打开浏览器
    http://docs.python.org/3/library/webbrowser.html

    然后同时打开一个本地 web 服务器

    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+=]

Views
=====

Outline
-------

* sidebar
* tree view, with a column to show a progress bar (display remaining task number, progress percentage)

  - See: http://www.codeproject.com/Articles/30721/WPF-TreeListView-Control

* outline mode, tag mode
* circular including is not allowed as all children nodes need to be displayed

Backlog
-------

* table mode

  * Insert defined row(s) above/below (change the defined row number in the setting)
  * Insert row(s) above/below (will pop up a dialog to input the number of rows to be inserted)
  * Should embed a collapsible tree on the first column, 
    the UI is similar to `this <http://www.taskmanagementguide.com/images/solution/articles/activity-management-software-different-activities001.jpg>`_, 
    but the progress bar should display on the outline view

* (scrum) board mode (using split+ListView, with property window)
* top: breadcrumb
* submit update    

  - --> update activity log (with a "download" button)
  - --> update progress view

* create an unorganized task (i.e. todo)
* fast detail pane (like the TotalCommand "ctrl+q" feature )

* copy paste to batch update the time estimate (like Excel)

.. _activity_view:

History
-------

(This view is like an "Audits" table in automation control system, and is also used as timesheet or my
direction control purpose.)

* Record daily activities

::

    [=+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    @@ 
    @@ [#2012-09-24_17:53:28]

    execution page (readonly, automatically updated) --- the done list
        by date
        by issue
        
        网页版：
        纵向两列
        左列，1/3宽度，日历控件排列，鼠标滚轮平滑滑动
        右列，2/3宽度，时间线或表格两种视图
        
    see "pg'-w. QTableWidget. QItemDelegate. QComboBox. _.py"

    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+=]

**Columns**:

* week day
* date
* job (so each job should have unique name)
* action

  1. create
  #. include in sprint
  #. start
  #. finish
  #. time reestimate
  #. suspend (need to provide reason)
  #. break down (when user do "break down" or "move to a new job")
  #. update (recorded when user do "save")
  #. close (need to provide reason)

* task
* remarks

Statistic
---------

* 根据百分比的 burn down 好像更合理一点（百分比的计算单位还是应该根据time estimate来进行）
* 除了 burn down chart 以外，还需要正负柱状图，正方向代表插入的任务量，负方向代表消除的任务量
* 最后部分显示 progress bar （那些Job的需要显示则在某处配置）

SWOT
----

(need to be moved to somewhere)

* strength
* weekness
* oppotunity
* threat

Detail
------

Task Detail View

* Used for adding task comments
* It was tracked issues page

  ::

    create date
    status
    project
    tags
    brief description
    details

Menu Bar
========

File
----

::

    [=+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    @@ 
    @@ [#2012-09-24_17:54:07]

    new (based on sqlite3 format)

    load --- can load multiple files)
    load all from path --- popup a tree list, and a input box to locate a path
    load a copy from URL --- download to local and open as readonly, can detect source change
    load a session --- a py file

    save as session --- a py file

    close current file
    close all files

    exist

    export to html
    export to pdf

    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+=]

Search
------

::

    [=+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    @@ 
    @@ [#2012-09-24_21:09:28]

    search in current file
    search in all opened files

    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+=]

View
----

::

    [=+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    @@ 
    @@ [#2012-09-24_21:10:19]

    file view
    outline view

    table mode
    board mode

    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+=]

Tools
-----


Options
-------



Help
----

::

    [=+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    @@ 
    @@ [#2012-09-24_21:12:12]

    user manual
    about (a dialog with QCommandLinkButton)
        version (license info, version, release notes)
        application:
            idea history (GTD, scrum, excel spreadsheet)
            what problem does this application aim to resolve?
                publish for teamwork
                integrated with feature list/requirement/test (the requirement matrix)
                task stack
                easier management (status, project tree)
                keep motivation: achievement/done list (auto-genarate execution log and burn up chart)
                integrated with SWOT (direction control)
                need a local lightweight issue tracking database, which can be well integrated with the todo list
        author (hold off at this moment)
            My name (Ron when ordering coffee, the pronunciation of "Li")
            My blog link
            My github link
                （move the following info to github）
                My product development principle
                    innovation is not from a sudden inspiration but from a specific problem resolving and constant improvement
                    user experience, especially details and UI, should always has the top priority
                    information and data should be always searchable
                My software engineering principle
                    microkernel
                    unit test
                    modular, especially separate UI from BL
                    reusable, testable, scalable, extendable
        acknowledgement (give lib list; for qt, pyside, python, github, mercurial, tortoisehg, tortoisegit & microsoft excel)

    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+=]

Feedback
--------

::

    [=+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    @@ 
    @@ [#2012-09-24_21:13:14]

    bug report
    proposals
        proposal votes
            e.g.
            
            As a (tick boxes)
                personal user
                team user with ___ memebers
            , I want "(some feature discription)"
            , so that I can ...
            
            [TODO] how to collect the info of the most used feature?
            [TODO] how to determine the features that users are willing to pay?
        create other proposals
    other comments

    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+=]

Tool Bar
========

::

    [=+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    @@ 
    @@ [#2012-09-24_17:54:41]

    search

    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+=]

