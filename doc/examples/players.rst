.. _player-example:

Controlling/querying your squeezeplayer
=======================================

Retrieving players
------------------

Once you've got your server, you'll want to get your players next.

It's easy to get the list of the players currently attached to your server:

.. code-block:: python

    from LMSTools import LMSServer

    # Define your server address
    SERVER_IP = "192.168.0.1"

    # create the server object
    server = LMSServer(SERVER_IP)

    # get the attached players
    players = server.get_players()

Each item in 'players' will be a :class:`LMSPlayer <LMSTools.player.LMSPlayer>` \
instance and should be easily identifiable by printing the output of the list.

.. code-block:: python

    >>>server.get_players()
    [LMSPlayer: Living Room (40:40:40:40:40:40),
     LMSPlayer: PiRadio (41:41:41:41:41:41),
     LMSPlayer: elParaguayo's Laptop (42:42:42:42:42:42)]
    >>>laptop = server.get_players()[2]
    >>>Laptop
    LMSPlayer: elParaguayo's Laptop (42:42:42:42:42:42)

So, now you've got your player, what can you do with it?

Controlling the player
----------------------

It's easy to do simple manipulation of the playlist.

The player has methods to :func:`play <LMSTools.player.LMSPlayer.play>`, \
:func:`pause <LMSTools.player.LMSPlayer.pause>` and skip tracks.

.. code-block:: python

    >>>laptop.play()
    >>>laptop.next()
    >>>laptop.stop()
    >>>

Changing volume
---------------

Players have a :attr:`volume <LMSTools.player.LMSPlayer.volume>` property. This \
can be used to retrieve the current volume level and adjust it. In addition \
there are :func:`volume_up <LMSTools.player.LMSPlayer.volume_up>` and \
:func:`volume_down <LMSTools.player.LMSPlayer.volume_down>` methods.

.. code-block:: python

    >>># Get the volume level
    >>>laptop.volume
    75
    >>>laptop.volume_down()
    >>>laptop.volume
    70
    >>>laptop.volume_down(10)
    >>>laptop.volume
    60
    >>>laptop.volume = 90
    >>>laptop.volume
    90

Syncing players
---------------

You can sync and unsync players easily.

.. code-block:: python

    >>>livingroom = server.get_players()[0]
    >>>livingroom
    LMSPlayer: Living Room (40:40:40:40:40:40
    >>>laptop.sync(livingroom)
    >>>

You can confirm which players are synced with your player:

.. code-block:: python

    >>>laptop.get_synced_players()
    [LMSPlayer: Living Room (40:40:40:40:40:40]
    >>>

If there are multiple sync groups then you can view members by using the \
:func:`show_players_sync_status <LMSTools.server.LMSServer.show_players_sync_status>` \
method.

Adding tracks to the playlist
-----------------------------

If you have a path to a playable item, these can be added to the playlist \
directly.

.. code-block:: python

    >>># You can use spotify urls if the app is installed
    >>>laptop.playlist_play("spotify://track:5xYZXIgVAND5sWjN8G0hID")
    >>>

The :func:`playlist_insert <LMSTools.player.LMSPlayer.playlist_insert>` and \
:func:`playlist_add <LMSTools.player.LMSPlayer.playlist_add>` methods can be \
used to place tracks at different locations in the playlist (i.e. next and \
last) while :func:`playlist_delete <LMSTools.player.LMSPlayer.playlist_delete>` \
can be used to remove tracks.

.. code-block:: python

    >>>laptop.playlist_delete("spotify://track:5xYZXIgVAND5sWjN8G0hID")
    >>>

.. _player-metadata:

Getting metadata
----------------

In case you don't know what's actually playing at the moment, you can retrieve \
metadata about the track (and other items in the playlist).

.. code-block:: python

    >>>laptop.track_title
    u'Go!'
    >>>laptop.track_artist
    u'Public Service Broadcasting'
    >>>laptop.track_album
    u'The Race For Space'

You can attempt to get a URL for the current track's artwork via the \
:attr:`track_artwork <LMSTools.player.LMSPlayer.track_artwork>` property.

If you want to query the playlist, there are a number of options open to you. \
See: :func:`playlist_get_info <LMSTools.player.LMSPlayer.playlist_get_info>`, \
:func:`playlist_get_detail <LMSTools.player.LMSPlayer.playlist_get_detail>` and \
:func:`playlist_get_current_detail <LMSTools.player.LMSPlayer.playlist_get_current_detail>`.

.. code-block:: python

    >>>laptop.playlist_get_current_detail()
    [{u'album': u'The Race For Space',
      u'artist': u'Public Service Broadcasting',
      u'coverart': u'0',
      u'coverid': u'-186029800',
      u'duration': u'252',
      u'id': u'-186029800',
      u'playlist index': 0,
      u'remote': 1,
      u'title': u'Go!'}]

Additional information can be requested by using \
:class:`tags <LMSTools.tags.LMSTags>`.

.. code-block:: python

    >>>from LMSTools import LMSTags as tags
    >>>laptop.playlist_get_current_detail(taglist=[tags.DURATION, tags.CONTENT_TYPE])
    [{u'duration': u'252',
      u'id': u'-186029800',
      u'playlist index': 0,
      u'title': u'Go!',
      u'type': u'Ogg Vorbis (Spotify)'}]

...and more
-----------

See the class documentation for :class:`LMSPlayer <LMSTools.player.LMSPlayer>` \
for further information on available properties and methods.
