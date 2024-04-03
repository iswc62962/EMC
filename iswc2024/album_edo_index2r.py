# edo index2.r.m generation
from Lib import *

DB_ALBUM = "./Album/DB_Album"
YAGO_ALBUM = "./Album/YAGO_album"

def preprocess():
    DB_dict = load_triples_to_dict(DB_ALBUM)
    YAGO_dict = load_triples_to_dict(YAGO_ALBUM)

    DB_dict_ids = compute_ids_for_DB_or_YAGO(DB_dict,"DB_Album_ids")
    YAGO_dict_ids = compute_ids_for_DB_or_YAGO(YAGO_dict,"YAGO_Album_ids")

    with open("DB_Album_triples","w") as input_file:
        json.dump(DB_dict_ids,input_file)
    
    with open("YAGO_Album_triples","w") as input_file:
        json.dump(YAGO_dict_ids,input_file)

    print(len(DB_dict_ids))
    print(len(YAGO_dict_ids))

if __name__ == "__main__":
    preprocess()
    #85072
    #137178
    with open("DB_Album_triples") as input_file:
        DB_dict_ids = json.load(input_file)
    with open("YAGO_Album_triples") as input_file:
        YAGO_dict_ids = json.load(input_file)
    d_metric = compute_r(DB_dict_ids,YAGO_dict_ids)

    with open("edo_album_index2.r.m","w") as output_file:
        json.dump(d_metric,output_file)
 
    '''
    with open("edo_album_index2.r.m") as input_file:
        d_metrics = json.load(input_file)
        all_pairs = 0
        for key in d_metrics:
            all_pairs += d_metrics[key]
    assert(all_pairs == 85072*137178)
    # compute identity relations
    r_contextual_identiy = 0
    pair_contextual_identiy = 0
    r_full_given_identity = 0
    pair_full_given_identity = 0
    r_full = 0
    pairs_full = 0
    
    d_identity = compute_identity_relation(d_metrics)

    r_contextual_identiy = len(d_identity)

    r_full = len(d_metrics)
    pairs_full = all_pairs

    for key in d_identity:
        r_full_given_identity += d_identity[key][0]
        pair_full_given_identity += d_identity[key][1]

    pair_contextual_identiy = pair_full_given_identity

    print(r_contextual_identiy)
    print(r_full_given_identity)
    print(r_full)
    print()
    print(pair_contextual_identiy)
    print(pair_full_given_identity)
    print(pairs_full)
    '''
 

 
