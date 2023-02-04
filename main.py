from flask import Flask, jsonify
from utils import get_one, get_all

app = Flask(__name__)


@app.get('/movie/<title>')
def get_by_title(title: str):
    query = f"""select * from netflix where title like '%{title}%' order by date_added desc """
    result = get_one(query)
    movie = {
        "title": result["title"],
        "country": result["country"],
        "release_year": result["date_added"],
        "genre": result["listed_in"],
        "description": result["description"]
    }
    return jsonify(movie)


@app.get('/movie/<year1>/to/<year2>')
def get_by_year(year1: str, year2: str):
    query = f"""select * from netflix
     where release_year 
     between '{year1}' and '{year2}' 
     limit 100
     """

    film_by_year = []
    for item in get_all(query):
        film_by_year.append({"title": item["title"],
                             "release_year": item["release_year"]})
    return jsonify(film_by_year)


@app.get('/movie/rating/children')
def get_children_film():
    query = """select * from netflix where rating = 'G'"""
    children_film = []
    for item in get_all(query):
        children_film.append({
            "title": item["title"],
            "rating": item["rating"],
            "description": item["description"]
        })
    return children_film


@app.get('/movie/rating/family')
def get_family_film():
    query = """select * from netflix
     where rating = 'G'
     or rating = 'PG' 
     or rating = 'PG-13' 
     """
    family_film = []
    for item in get_all(query):
        family_film.append({
            "title": item["title"],
            "rating": item["rating"],
            "description": item["description"]
        })
    return family_film


@app.get('/movie/rating/adult')
def get_adult_film():
    query = """select * from netflix
     where rating = 'R'
     or rating = 'NC-17' 
     """
    adult_film = []
    for item in get_all(query):
        adult_film.append({
            "title": item["title"],
            "rating": item["rating"],
            "description": item["description"]
        })
    return adult_film


@app.get('/movie/genre/<genre>')
def get_film_by_genre(genre: str):
    query = f"""select * from netflix 
    where listed_in 
    like '%{genre.lower()}%' 
    order by release_year desc 
    limit 10 
    """
    genre_film = []
    for item in get_all(query):
        genre_film.append({
            "title": item["title"],
            "genre": item["listed_in"],
            "description": item["description"],
            "date": item["date_added"]
        })
    return genre_film


app.run()
