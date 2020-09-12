from xbmcswift2 import Plugin, xbmcgui
plugin = Plugin()
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': "https://listen-nme.sharp-stream.com/nme1.mp3",
            'thumbnail': "https://radio.nme.com/static/media/nme-1.b6b0cc81.png",
            'is_playable': True},
        {
            'label': plugin.get_string(30002),
            'path': "https://listen-nme.sharp-stream.com/nme2.mp3",
            'thumbnail': "https://radio.nme.com/static/media/nme-2.a3f6a801.png",
            'is_playable': True},
    ]
    return items

if __name__ == '__main__':
    plugin.run()
