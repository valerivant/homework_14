import sqlite3


def get_all(query: str):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row

        result = []

        for item in connection.execute(query).fetchall():
            result.append(item)
        return result


def get_one(query: str):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(query).fetchone()
        if result is None:
            return None
        else:
            return dict(result)


def name_actors(actor1: str = 'Rose McIver', actor2: str = 'Ben Lamb'):
    query = f"""select * from netflix 
    where netflix.'cast' 
    like '%{actor1}%' 
    and netflix.'cast' 
    like '%{actor2}%' 
    """
    cast = []
    cast_list = []
    for item in get_all(query):
        for actor in item['cast'].split(','):
            cast.append(actor)
    for actor in cast:
        if cast.count(actor) > 2:
            cast_list.append(actor)
    return cast_list


print(name_actors())


def get_film_data(film_type: str = 'Movie', date_release: int = 2011, genre: str = 'Children & Family Movies'):
    query = f"""select * from netflix 
    where type like '%{film_type}%' 
    and release_year like '%{date_release}%' and listed_in like '%{genre}%' 
    """
    film_data = []
    for film in get_all(query):
        film_data.append({"title": film["title"],
                          "description": film["description"]
                          })
    return film_data


print(get_film_data())
