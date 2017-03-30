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

Discovering servers
-------------------

If you don't know the address of your server you can use the \
:class:`LMSDiscovery <LMSTools.discovery.LMSDiscovery>` class to find servers.

.. code-block:: python

    from LMSTools import LMSServer, LMSDiscovery

    # Find servers
    servers = LMSDiscovery().all()

    if servers:

        # Get the details of the server
        SERVER_IP = servers[0]["host"]
        SERVER_PORT = servers[0]["port"]

        # create the server object
        server = LMSServer(SERVER_IP)

What now?
---------

At this point, you can test if your connection works by running the Ping \
method.

::

  >>>server.Ping()
  True

Pretty unexciting though, isn't it?

That's because you know it's not the server that really matters, it's the \
players. So let's see how they work in the next section: :ref:`player-example`.
