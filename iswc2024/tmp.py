# metrics detail for the classes of the dataset
from Lib import *

DB_ALBUM = "./Album/DB_Album"
YAGO_ALBUM = "./Album/YAGO_album"
ALBUM_GD = "./Album/Album.Goldstandard.txt"

DB_ACTOR = "./Actor/DB_Actor"
YAGO_ACTOR = "./Actor/YAGO_actor"
ACTOR_GD = "./Actor/Actor.Goldstandard.txt"

DB_UNIVERSITY = "./University/DB_University"
YAGO_UNIVERSITY = "./University/YAGO_university"
UNIVERSITY_GD = "./University/University.Goldstandard.txt"

DB_BOOK = "./Book/DB_Book"
YAGO_BOOK = "./Book/YAGO_book"
BOOK_GD = "./Book/Book.Goldstandard.txt.oi"

DB_FILM = "./Film/DB_Film"
YAGO_FILM = "./Film/YAGO_Film"
FILM_GD = "./Film/Film.Goldstandard.N-1.txt"

DB_MOUNTAIN = "./Mountain/DB_Mountain"
YAGO_MOUNTAIN = "./Mountain/YAGO_mountain"
MOUNTAIN_GD = "./Mountain/Mountain.Goldstandard.txt"

def compute_properties_metric(DBorYAGO_dict):

    nb_p_db_or_yago = []
    nb_triples = 0
    l_prop = []
    for i in DBorYAGO_dict:
        for s,p,o in DBorYAGO_dict[i]:
            nb_triples += 1
            if p not in l_prop:
                l_prop.append(p)
    return nb_triples, len(l_prop)


if __name__ == "__main__":
    
    DB_dict = load_triples_to_dict(DB_ALBUM)
    YAGO_dict = load_triples_to_dict(YAGO_ALBUM)
    gd = load_pair(ALBUM_GD)
    nb_t_db, nb_p_db = compute_properties_metric(DB_dict)
    nb_t_yago, nb_p_yago = compute_properties_metric(YAGO_dict)

    print("Album")
    print(len(DB_dict))
    print(nb_t_db)
    print(nb_p_db)
    print(len(YAGO_dict))
    print(nb_t_yago)
    print(nb_p_yago)
    print(len(gd)) 
    
    DB_dict = load_triples_to_dict(DB_ACTOR)
    YAGO_dict = load_triples_to_dict(YAGO_ACTOR)
    gd = load_pair(ACTOR_GD)
    nb_t_db, nb_p_db = compute_properties_metric(DB_dict)
    nb_t_yago, nb_p_yago = compute_properties_metric(YAGO_dict)
    print()
    print("Actor")
    print(len(DB_dict))
    print(nb_t_db)
    print(nb_p_db)
    print(len(YAGO_dict))
    print(nb_t_yago)
    print(nb_p_yago)
    print(len(gd)) 

    DB_dict = load_triples_to_dict(DB_UNIVERSITY)
    YAGO_dict = load_triples_to_dict(YAGO_UNIVERSITY)
    gd = load_pair(UNIVERSITY_GD)
    nb_t_db, nb_p_db = compute_properties_metric(DB_dict)
    nb_t_yago, nb_p_yago = compute_properties_metric(YAGO_dict)
    print()
    print("University")
    print(len(DB_dict))
    print(nb_t_db)
    print(nb_p_db)
    print(len(YAGO_dict))
    print(nb_t_yago)
    print(nb_p_yago)
    print(len(gd)) 

    DB_dict = load_triples_to_dict(DB_BOOK)
    YAGO_dict = load_triples_to_dict(YAGO_BOOK)
    gd = load_pair(BOOK_GD)
    nb_t_db, nb_p_db = compute_properties_metric(DB_dict)
    nb_t_yago, nb_p_yago = compute_properties_metric(YAGO_dict)
    print()
    print("Book")
    print(len(DB_dict))
    print(nb_t_db)
    print(nb_p_db)
    print(len(YAGO_dict))
    print(nb_t_yago)
    print(nb_p_yago)
    print(len(gd)) 

    DB_dict = load_triples_to_dict(DB_FILM)
    YAGO_dict = load_triples_to_dict(YAGO_FILM)
    gd = load_pair(FILM_GD)
    nb_t_db, nb_p_db = compute_properties_metric(DB_dict)
    nb_t_yago, nb_p_yago = compute_properties_metric(YAGO_dict)
    print()
    print("Film")
    print(len(DB_dict))
    print(nb_t_db)
    print(nb_p_db)
    print(len(YAGO_dict))
    print(nb_t_yago)
    print(nb_p_yago)
    print(len(gd)) 

    DB_dict = load_triples_to_dict(DB_MOUNTAIN)
    YAGO_dict = load_triples_to_dict(YAGO_MOUNTAIN)
    gd = load_pair(MOUNTAIN_GD)
    nb_t_db, nb_p_db = compute_properties_metric(DB_dict)
    nb_t_yago, nb_p_yago = compute_properties_metric(YAGO_dict)
    print()
    print("Mountain")
    print(len(DB_dict))
    print(nb_t_db)
    print(nb_p_db)
    print(len(YAGO_dict))
    print(nb_t_yago)
    print(nb_p_yago)
    print(len(gd)) 


