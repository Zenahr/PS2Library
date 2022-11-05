import os, glob
from pprint import pprint
import shutil
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
SUPPORTED_ISO_FORMATS = ('.iso', '.bin', '.mdf', '.nrg', '.img', '.dump', '.gz', '.cso', '.chd', '.ISO', '.BIN', '.MDF', '.NRG', '.IMG', '.DUMP', '.GZ', '.CSO', '.CHD')
SUPPORTED_COVER_IMAGE_FORMATS = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.PNG', '.JPG', '.JPEG', '.GIF', '.WEBP')

@profile
def get_games() -> list:
    games = list()
    ROMS_FOLDER = config['default']['ROMS_FOLDER']
    print(ROMS_FOLDER)
    for root, _, files in os.walk(ROMS_FOLDER):
        # if current directory is "other", skip it.
        if root.split('\\')[-1] == 'other':
            continue
        if len(files) > 0:
            entry = dict(
                display_name    = '',
                iso             = '',     # reference this if multidisc is False
                cover           = '',
                cover_extension = '',
                multidisc       = False,
                isos            = list(), # reference this list if multidisc is True
            )
            entry['display_name'] = root.split('\\')[-1] # get display name based on directory name
            if entry['display_name'] == 'ROMS':
                del entry
                continue
            for file in files:
                if file.endswith(SUPPORTED_COVER_IMAGE_FORMATS): # get cover image 
                    entry['cover'] = os.path.join(root, file)
                    entry['cover_extension'] = entry['cover'].split('.')[-1] # use to help build the cover URL
                try:
                    pass # UNCOMMENT THIS LINE TO ENABLE MULTIDISC SUPPORT
                    # if len(glob.glob(root + '/*.iso')) > 1 or len(glob.glob(root + '/*.bin')) > 1: # determine if multidisc
                    #     entry['multidisc'] = True
                    #     if file.endswith(SUPPORTED_ISO_FORMATS):
                    #         entry['isos'].append(os.path.join(root, file))
                except Exception as e:
                    print(e)
                if not entry['multidisc']:
                    if file.endswith(SUPPORTED_ISO_FORMATS):
                        entry['iso'] = os.path.join(root, file)
            games.append(entry)
    # pprint(games)
    return games

def prepare_artwork(games: list):
    """Prepare artwork for games by copying it to the "covers" directory so that they can be served by Flask."""
    for game in games:
        if game['cover']:
            original_cover = game['cover']
            original_cover_extension = game['cover_extension']
            if not os.path.isfile(os.path.join('static', 'covers', game['display_name'] + '.' + original_cover_extension)):
                shutil.copy(game['cover'], os.path.join('static', 'covers', game['display_name'] + '.' + original_cover_extension))

if '__main__' == __name__:
    prepare_artwork(get_games())
    games = get_games()
    # print(games)