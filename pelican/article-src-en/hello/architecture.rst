============
Architecture
============

:date: 2010-10-03 10:20
:summary: Architecture Architecture Architecture Architecture Architecture Architecture Architecture Architecture 
    Architecture Architecture Architecture Architecture Architecture Architecture Architecture Architecture 
    Architecture Architecture Architecture Architecture Architecture 

.. contents::

Basic Architecture
==================

This is the basic system architecture:

::

    ui exe <--------+
      | ^           |
      v |           | 
    da proxy exe    |
      | ^           |
      v |           |
    bl dll <--------+ 
      |    
      v    
    da dll
      |
      v
    database

- "da proxy exe" is for broadcasting the database change to all connected client, otherwise
  ui exe accesses bl dll directly and can only get database change by manually refreshing the 
  view.
- "da proxy exe" is able to deliver web ui, so it is not only a web service, but also a web app

Extended Architecture
=====================

::

    view (both gui & console)
    view model

    App Proxy (a backend switcher, support both native and network backend)

    communication

    balancer
    cache
    app service
    DAL (with DB switcher)

    DB


Extensibility & Scalability
===========================

Multiple DbContext: 

* One extension one DbContext
* Have one "contain-everything" DbContext for database creation

Extending function layers:

* All components' API use the common business entities
* If need an extra layer, e.g. validation, Performance measurement, caching, message queue, 
  etc. , just add a new layer component in the middle with the same API interface (By this
  way, the prototype can just focus on the core functions)

Network
=======

* **Avoid Callback, but use client side service**

  If server use callback to contact client, one disadvantage is: once the callback interface changes,
  all the client must upgrade.

  Therefore, it may be better to have client side services to work as callback event interface. So when
  the client side service is changed, only the necessary minimal sites need to upgrade, other sites 
  can still work on the old client side versions.

* **Use Queue**

  Need to consider to use a message queues for critical communications. 

* **Peer-to-peer Design**

  - Every client can work as a proxy
  - Every client can replicate their proxy list to other clients
  - Because notfication is not based on callback, every client just needs to wait for others to 
    call them. So when a client update its own task, it will call all other clients one-by-one.
  - **Registration**: the living client register itself in the central database, if it is down, other 
    clients will update that client's status in the database if they cannot reach it.
