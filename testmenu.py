from LMSTools import LMSServer, LMSMenuHandler

srv = LMSServer("192.168.0.70")
player = srv.get_players()[0]

CUSTOM_MENU = {
"count": 4,
"item_loop": [{
    "node": "myMusic",
    "weight": 11,
    "text": "Artists",
    "actions": {
        "go": {
            "cmd": ["browselibrary", "items"],
            "params": {
                "menu": 1,
                "mode": "artists",
                "role_id": "ALBUMARTIST,ARTIST,BAND,COMPOSER,CONDUCTOR,TRACKARTIST"
            }
        }
    },
    "homeMenuText": "All Artists",
    "id": "myMusicArtistsAllArtists",
    "icon": "html/images/artists.png"
}, {
    "node": "myMusic",
    "weight": 20,
    "text": "Albums",
    "actions": {
        "go": {
            "cmd": ["browselibrary", "items"],
            "params": {
                "menu": 1,
                "mode": "albums"
            }
        }
    },
    "homeMenuText": "Browse Albums",
    "id": "myMusicAlbums",
    "icon": "html/images/albums.png"
}, {
    "node": "myMusic",
    "text": "Playlists",
    "weight": 80,
    "id": "myMusicPlaylists",
    "icon": "html/images/playlists.png",
    "actions": {
        "go": {
            "cmd": ["browselibrary", "items"],
            "params": {
                "menu": 1,
                "mode": "playlists"
            }
        }
    }
}, {
     "node": "myMusic",
     "text": "Search",
     "weight": 90,
     "id": "myMusicSearch",
     "icon": "html/images/search.png",
     "actions": {
        "go": {
            "cmd": ["browselibrary", "items"],
            "params": {
                "menu": 1,
                "mode": "search"
            }
        }
    }
}, {
    "node": "home",
    "window": {
        "titleStyle": "album",
        "icon-id": "plugins/MyApps/html/images/icon.png"
    },
    "uuid": "2E3ACD53-B9A8-4440-9C5B-517B1EB28E34",
    "weight": 80,
    "displayWhenOff": 0,
    "text": "My Apps",
    "id": "opmlmyapps",
    "actions": {
        "go": {
            "player": 0,
            "cmd": ["myapps", "items"],
            "params": {
                "menu": "myapps"
            }
        }
    }
}]
}

menu = LMSMenuHandler(player)
results = menu.getCustomMenu(CUSTOM_MENU)
for item in results:
    print item.text, item.cmd
