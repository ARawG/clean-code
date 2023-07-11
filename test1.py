all_users = {}
all_albums = {}


def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
    all_users[username] = tuple([username ,age ,city ,albums])


def add_album(name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
    all_albums[name] = tuple([artist_name ,genre ,tracks])

def return_counter(info_of_user,info_of_album,index_of_user, index_of_album, all_users, all_albums) -> int:
    counter = 0
    for key,value in all_users.items():
        if(value[index_of_user]==info_of_user):
            for album in value[3]:
                if(all_albums[album][index_of_album]==info_of_album):
                    counter+=all_albums[album][2]
    return counter

def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    return return_counter(username, artist_name, 0, 0, all_users, all_albums)

def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    return return_counter(username, genre, 0,1 , all_users, all_albums)

def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:
    return return_counter(age ,artist_name ,1 ,0, all_users, all_albums)

def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    return return_counter(age, genre, 1, 1, all_users, all_albums)

def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    return return_counter(city, artist_name, 2, 0, all_users, all_albums)

def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    return return_counter(city, genre, 2, 1, all_users,all_albums)

add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users, all_albums)
add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users, all_albums)
add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users, all_albums)
add_album("eclipse", "malmsteen", "classic", 10, all_users, all_albums)
add_album("barf", "beeptunes", "pop", 22, all_users, all_albums)
add_album("tekunbede", "beeptunes", "pop", 14, all_users, all_albums)
add_album("gavazn", "sorena", "persian", 18, all_users, all_albums)
add_album("bidad", "shajarian", "classic", 10, all_users, all_albums)
add_album("blaze", "ghorbani", "pop", 9, all_users, all_albums)
print(query_user_genre("Ali", "classic", all_users, all_albums))
print(query_age_artist(12, "shajarian", all_users, all_albums))
print(query_age_genre(12, "pop", all_users, all_albums))
print(query_city_artist("Bushehr", "ghorbani", all_users, all_albums))
print(query_city_genre("Bushehr", "pop", all_users, all_albums))