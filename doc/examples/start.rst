Starting out
============

Unsurprisingly, the library is centered around the server. So your first step \
is to create a server object.

.. code-block:: python

    from LMSTools import LMSServer

    # Define your server address
    SERVER_IP = "192.168.0.1"

    # create the server object
    server = LMSServer(SERVER_IP)

At this point, you can test if your connection works by running the Ping \
method.

::

  >>>server.Ping()
  True

Pretty unexciting though, isn't it?

That's because you know it's not the server that really matters, it's the \
players. So let's see how they work in the next section: :ref:`player-example`.
