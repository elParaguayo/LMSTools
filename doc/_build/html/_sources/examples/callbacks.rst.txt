Using the callbackserver
========================

Callbacks can be configured in two different ways:

1) Using decorators
2) Using the 'add_callback' method

**Decorators**

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

**Using 'add_callback' method**

.. code-block:: python

    def volume_event(event=None):
        print "Volume event received: {}".format(event)

    squeeze = LMSCallbackServer("192.168.0.1")
    squeeze.add_callback(squeeze.VOLUME_CHANGE, volume_event)
    squeeze.start()
