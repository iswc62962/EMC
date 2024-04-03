# Compute & Check pattern for author work

from Lib import *
from Pattern import *
import json

DB_BOOK = "./Book/newDB_Book"
YAGO_BOOK = "./Book/YAGO_book"

R_METRICS_BOOK = "./Book/edo_book_index2.r.m"

# all the book of an author
def extract_author_work(DBorYAGO,author):
    d_work = {}
    for book_id in DBorYAGO:
        found = False
        for s,p,o in DBorYAGO[book_id]:
            if p == "created-inv" and o == author:
                found = True
                break
        if found: 
            d_work[book_id] = DBorYAGO[book_id]
    return d_work

def DB_YAGO_common_author(DB_dict,YAGO_dict):
    authors_DB = []
    authors_YAGO = []
    for key in DB_dict:
        for s,p,o in DB_dict[key]:
            if p == "created-inv":
                if o not in authors_DB:
                    authors_DB.append(o)
    for key in YAGO_dict:
        for s,p,o in YAGO_dict[key]:
            if p == "created-inv":
                if o not in authors_YAGO:
                    authors_YAGO.append(o)
    return list(set(authors_DB) & set(authors_YAGO))


if __name__ == "__main__":
    DB_dict_book = load_triples_to_dict(DB_BOOK)
    YAGO_dict_book = load_triples_to_dict(YAGO_BOOK)
    authors = DB_YAGO_common_author(DB_dict_book,YAGO_dict_book)
    # the nb author in the dataset
    print("author work")
    print(len (authors))
    #print(len(DB_dict_book))
    #print(len(YAGO_dict_book))
    #compute_pattern_dataset(authors,DB_dict_book,YAGO_dict_book,extract_author_work)
    PATTERN_DATASET = "./author_work_pattern_dataset"

    '''
    e_count, d_count, o_count = compute_nb_pair_per_context(PATTERN_DATASET)
    with open("e_author_work_count","w") as output_file:
        json.dump(e_count,output_file)
    with open("d_author_work_count","w") as output_file:
        json.dump(d_count,output_file)
    with open("o_author_work_count","w") as output_file:
        json.dump(o_count,output_file)
    '''
    '''
    with open("o_author_work_count") as input_file:
        o_count = json.load(input_file)
    l_all_omega_context = from_keys_to_list(o_count.keys())
    with open("d_author_work_count") as input_file:
        d_count = json.load(input_file)
    l_all_delta_context = from_keys_to_list(d_count.keys())
    with open("e_author_work_count") as input_file:
        e_count = json.load(input_file)
    l_all_epsilon_context = from_keys_to_list(e_count.keys())
    
    nb_included_d = compute_nb_pair_for_context_included(d_count)
    nb_included_e = compute_nb_pair_for_context_included(e_count)
    nb_included_o = compute_nb_pair_for_context_included(o_count)
    '''
    
    # 1) first pattern
    #p = compute_pattern(nb_included_e,nb_included_d,nb_included_o)
    #res = check_pattern_on_file(p,"./author_work_pattern_dataset")
    #print(p)
    #print(res)
    #[['created-inv'], ['skos:preflabel'], ['wascreatedonyear']]
    #(0.8959143968871596, 148281, 165508)
    #[['created-inv'], ['skos:preflabel'], ['wascreatedonyear']]
    #(0.8959143968871596, 148281, 165508)
    
    # 3) one pattern have been found check the support with with check_patterns_...
    patterns = []
    patterns.append([['created-inv'], ['skos:preflabel'], ['wascreatedonyear']])
    for pattern in patterns:
        print(pattern)
    res = check_patterns_on_file(patterns,"./author_work_pattern_dataset")
    print(res)


    # check pattern on all pair of books
    #with open(R_METRICS_BOOK) as input_file:
    #    r_metrics = json.load(input_file)
    #res = check_pattern_on_r_metrics([['created-inv'], ['skos:preflabel'], ['wascreatedonyear']],r_metrics)
    #print(res)
    #res = check_patterns_on_r_metrics([[['created-inv'], ['skos:preflabel'], ['wascreatedonyear']]],r_metrics)
    #print(res)
