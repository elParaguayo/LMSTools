Callback server
===============

LMSCallbackServer provides a mechanism for subscribing to event notifications \
from the server and triggering callback functions based on the type of event \
received.

The server subclasses the python threading so that the server can be run in \
the background.

Event notifications
-------------------

The callback server will send a single parameter to the callback function. \
This parameter is the event payload. Therefore any method that is to be used \
as a callback function should be able to accept (and handle) this payload.

Notification payload
--------------------

The payload is a single string and must be parsed by your callback function.

An example payload looks like this:

::

  41:41:41:41:41:41 mixer volume -5

The first part of the payload is the reference of the player, the remaining \
part is the relevant event.

If you need to check whether the event matches a specific player you can \
check equivalence via the :attr:`ref <LMSTools.player.LMSPlayer.ref>` property \
or just compare the player reference received with the player object. e.g.:

.. code-block:: python

  >>>laptop = LMSPlayer("41:41:41:41:41:41", server)
  >>>event = "41:41:41:41:41:41 mixer volume -5"
  >>>event_player = event.split(" ")[0]
  >>>event_player == laptop.ref
  True
  >>>event_player == laptop
  True

Alternatively, the player can check the event itself via the \
:attr:`check_event_player <LMSTools.player.LMSPlayer.check_event_player>` or \
:attr:`check_event_sync_group <LMSTools.player.LMSPlayer.check_event_sync_group>` \
methods.

.. code-block:: python

  >>>laptop = LMSPlayer("41:41:41:41:41:41", server)
  >>>event = "41:41:41:41:41:41 mixer volume -5"
  >>>laptop.check_event_player(event)
  True

Using the callbackserver
------------------------

Callbacks can be configured in two different ways:

1) Using decorators_
2) Using the add_callback_ method

.. decorators:

Decorators
~~~~~~~~~~

.. code-block:: python

    squeeze = LMSCallbackServer()

    @squeeze.event(squeeze.VOLUME_CHANGE)
    def volume_event(event=None):
        print "Volume event received: {}".format(event)

    squeeze.set_server("192.168.0.1")
    squeeze.start()

If you are using decorators inside a class then this will happen before your
class has been initialised so you need to provide the callback server with a
reference to the class instance.

.. code-block:: python

    squeeze = LMSCallbackServer()

    class MyClass(object):

        def __init__(self):
            self.squeeze = squeeze
            self.squeeze.set_server("192.168.0.1", parent_class=self)
            self.squeeze.start()

        @squeeze.event(squeeze.VOLUME_CHANGE)
        def volume_event(self, event=None):
            print "Volume event received: {}".format(event)

Multiple events can be added with multiple decorators

.. code-block:: python

    @squeeze.event(squeeze.VOLUME_CHANGE)
    @squeeze.event(squeeze.PLAY_PAUSE)
    def generic_event(event=None):
        print "Event received: {}".format(event)

Or by passing events as a list

.. code-block:: python

    @squeeze.event([squeeze.VOLUME_CHANGE, squeeze.PLAY_PAUSE])
    def generic_event(event=None):
        print "Event received: {}".format(event)

.. _add_callback:

Using 'add_callback' method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def volume_event(event=None):
        print "Volume event received: {}".format(event)

    squeeze = LMSCallbackServer("192.168.0.1")
    squeeze.add_callback(squeeze.VOLUME_CHANGE, volume_event)
    squeeze.start()
