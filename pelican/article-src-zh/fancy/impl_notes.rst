====================
Implementation Notes
====================

:date: 2010-10-03 10:20

.. contents::

If find any build/runtime problem
=================================

.. code:: java

    public void setReceivingSendSyncDResponse(boolean isReceivingSendSyncDResponse)
    {
        this.isReceivingSendSyncDResponse = isReceivingSendSyncDResponse;
        
        if(isReceivingSendSyncDResponse)
        {
            msgSet = new DynetReceivedMessageSet(network);                
        }
        else
        {
                sendSyndDReturn = new DynetReadResponse(network);             
                sendSyndDReturn.readResponse(sendSyndDRsp.getMsgSet());                
            }
        }
    }


* Make sure the library references use the same .net platform as the relevant projects, 
  especially the sqlite dll references, which were added manually in TiTest project

TiCommon
========

* Reason why remove List<Task> property in Job 
  
  - to avoid maintain the in memory object state (to keep consistent with the DB data)
  - it's too trouble to query a task list when create a Job object

TiDesk (the UI layer)
=====================

Mix using WPF and WinForm
-------------------------

WPF does not have tray icon notification control, so WinForm is used for that function instead.

* Affedtec file: TimeInsight\vs\Tidesk\MainWindow.xaml.cs
* Added reference: System.Windows.Forms

TiCore (the BL layer)
=====================

Serialization
-------------

* Although because of a hidden proxy object added by the entity framework, the serialization of DTOs can not be done 
  in asp.net mvc, it can, however, be performed by a customized function using XmlSerializer and MemoryStream.
* To prevent circular reference, some DTO propoerties a marked as "[XmlIgnoreAttribute]"

