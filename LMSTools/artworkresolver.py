from urllib import urlencode

class LMSArtworkResolver(object):
    """
    Class object to help provide an easy way of obtaining a URL to a playlist item.

    The class is capable of working out the appropriate path depending on \
    whether the file is remote or local.

    :type host: str
    :param host: address of the server
    :type port: int
    :param port: webport of the server (default 9000)
    """

    def __init__(self, host="localhost", port=9000):
        self.host = host
        self.port = port

        # Set up the template for local artwork
        base = "http://{host}:{port}".format(host=self.host, port=self.port)
        self.localart = base + "/music/{coverid}/cover_{h}x{w}_p.png"

        self.default = self.localart

    def __getRemoteURL(self, track, size):
        # Check whether there's a URL for remote artworl
        art = track.get("artwork_url", False)

        h, w = size

        # If there is, build the link.
        if art:

            return track.get("artwork_url")

        # If not, return the fallback image
        else:
            return self.default.format(coverid=0, h=h, w=w)

    def __getLocalURL(self, track, size):
        # Check if local cover art is available
        coverart = track.get("coverart", False)

        h, w = size

        # If so, build the link
        if coverart:

            return self.localart.format(h=h,
                                        w=w,
                                        coverid=track["coverid"])

        # If not, return the fallback image
        else:
            return self.default.format(h=h,
                                        w=w,
                                        coverid=0)

    def getURL(self, track, size=(500, 500)):
        """
        Method for generating link to artwork for the selected track.

        :type track: dict
        :param track: a dict object which must contain the "remote", "coverid" \
        and "coverart" tags as returned by the server.

        :type size: tuple
        :param size: optional parameter which can be used when creating links \
        for local images. Default (500, 500).
        """

        # List of required keys
        required = ["remote", "coverart"]

        # Check that we've received the right type of data
        if type(track) != dict:
            raise TypeError("track should be a dict")

        # Check if all the keys are present
        if not set(required) < set(track.keys()):
            raise KeyError("track should have 'remote' and"
                           " 'coverart' keys")

        # Check the flags for local and remote art
        track["coverart"] = int(track["coverart"])
        remote = int(track["remote"])

        # If it's a remotely hosted file, let's get the link
        if remote:
            return self.__getRemoteURL(track, size)

        # or it's a local file, so let's get the link
        else:
            return self.__getLocalURL(track, size)
