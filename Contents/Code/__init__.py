import re, string
ARTE_CONCERT_URL  = 'http://concert.arte.tv'
ARTE_URL  = 'http://www.arte.tv'

ICON = 'arte_logo.png'
ART = 'art-default.png'
PREFIX = '/video/gg_tv'
NAME = 'GGTV Plugin'

####################################################################################################
def Start():

  Plugin.AddPrefixHandler(PREFIX, MainMenu, 'GG_TV', ICON, ART)
  Plugin.AddViewGroup('InfoList', viewMode='InfoList', mediaType='items')
  ObjectContainer.title1 = 'GG_TV'
  ObjectContainer.art = R(ART)
  DirectoryObject.thumb = R(ICON)
  VideoClipObject.thumb = R(ICON)
  VideoClipObject.art = R(ART)
  HTTP.CacheTime = 1800

####################################################################################################
@handler( PREFIX, NAME, art=ART, thumb=ICON )
def MainMenu():
    oc = ObjectContainer( )

    #All movies
    oc.add( DirectoryObject( key=Callback( GetMoviesList, title='Liste des films' ),
                             title='Liste des films',
                             thumb=R( ICON ) ) )

    return oc

####################################################################################################
@route(PREFIX + '/channelmenu/GetMoviesList')
def GetMoviesList(title2):
  oc = ObjectContainer( title2=title2 )
  for movie in getMoviesFromJsonURL():
    oc.add(CreateVideoClipObject(
        url = recording["stream_url"],
        title = recording["title"],
        summary = recording["description"],
        duration = int(recording['length']) * 1000,
        thumb = 'http://static.filmon.com/couch/channels/%s/extra_big_logo.png' % recording['channel_id']
    ))

  if len(oc) < 1:
    oc.header  = "Désolé"
    oc.message = "Aucun film n'a été trouvé."

  return oc

####################################################################################################
def getMoviesFromJsonURL():
    movies = []
    json = JSON.ObjectFromURL( 'http://127.0.0.1/ggtv.php' )
    base_url = json.get( 'base_url', None )

    return movies
