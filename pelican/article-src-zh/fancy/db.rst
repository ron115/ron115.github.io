========
Database
========

:date: 2010-10-03 10:20

Overview
========

More Considerations
-------------------

need to have some way to verify the database file is not corrupted

About DTOs
----------

Only the relation tables are automatically created by the EF ORM framework, 
other tables all have a relevant DTO object with the same name.

Database Merging
----------------

- Need database merging interfaces
- Need object transfering format definitions (probably using xml)

- Merge by ReadActivities()/CreateActivities() - the ORM should be able to create all tables


