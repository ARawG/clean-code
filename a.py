all_users = {}
all_albums = {}


def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
    all_users[username] = [age ,city ,albums]


def add_album(name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
    all_albums[name] = [artist_name ,genre ,tracks]


def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    counter = 0
    for i in all_users.get(username)[2]:
        if(all_albums.get(i)[0]==artist_name):
            counter+=all_albums.get(i)[2]
    return counter

def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    counter = 0
    for i in all_users.get(username)[2]:
        if(all_albums.get(i)[1]==genre):
            counter+=all_albums.get(i)[2]
    return counter


def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:
    counter = 0
    for key,value in all_users.items():
        if(value[0]==age):
            for album in value[2]:
                if(all_albums[album][0]==artist_name):
                    counter+=all_albums[album][2]
    return counter


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    counter = 0
    for key,value in all_users.items():
        if(value[0]==age):
            for album in value[2]:
                if(all_albums[album][2]==genre):
                    counter+=all_albums[album][2]
    return counter


def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    counter = 0
    for key,value in all_users.items():
        if(value[1]==city):
            for album in value[2]:
                if(all_albums[album][0]==artist_name):
                    counter+=all_albums[album][2]
    return counter

def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    counter = 0
    for key,value in all_users.items():
        if(value[1]==city):
            for album in value[2]:
                if(all_albums[album][2]==genre):
                    counter+=all_albums[album][2]
    return counter