# Compute & Check pattern for director work 

from Lib import *
from Pattern import *

DB_FILM = "./Film/DB_Film"
YAGO_FILM = "./Film/YAGO_Film"


R_METRICS_FILM = "./Film/edo_film_index2.r.m"

def extract_director(DBorYAGO,director):
    d_direction = {}
    for film_id in DBorYAGO:
        found = False
        for s,p,o in DBorYAGO[film_id]:
            if p == "directed-inv" and o == director:
                found = True
                break
        if found:
            d_direction[film_id] = DBorYAGO[film_id]
    return d_direction

def DB_YAGO_common_director(DB_dict,YAGO_dict):
    director_DB = []
    director_YAGO = []
    for key in DB_dict:
        for s,p,o in DB_dict[key]:
            if p == "directed-inv":
                if o not in director_DB:
                    director_DB.append(o)
    for key in YAGO_dict:
        for s,p,o in YAGO_dict[key]:
            if p == "directed-inv":
                if o not in director_YAGO:
                    director_YAGO.append(o)
    return list(set(director_DB) & set(director_YAGO))

if __name__ == "__main__":
    DB_dict_film = load_triples_to_dict(DB_FILM)
    YAGO_dict_film = load_triples_to_dict(YAGO_FILM)
    directors = DB_YAGO_common_director(DB_dict_film,YAGO_dict_film)
    # the nb directors in the dataset
    print("director work")
    print(len(directors))
    #compute_pattern_dataset(directors,DB_dict_film,YAGO_dict_film,extract_director)
    PATTERN_DATASET = "./director_work_pattern_dataset"
    #e_count, d_count, o_count = compute_nb_pair_per_context(PATTERN_DATASET)
    '''
    with open("e_director_work_count","w") as output_file:
        json.dump(e_count,output_file)
    with open("d_director_work_count","w") as output_file:
        json.dump(d_count,output_file)
    with open("o_director_work_count","w") as output_file:
        json.dump(o_count,output_file)
    '''
    '''
    with open("o_director_work_count") as input_file:
        o_count = json.load(input_file)
    l_all_omega_context = from_keys_to_list(o_count.keys())
    with open("d_director_work_count") as input_file:
        d_count = json.load(input_file)
    l_all_delta_context = from_keys_to_list(d_count.keys())
    with open("e_director_work_count") as input_file:
        e_count = json.load(input_file)
    l_all_epsilon_context = from_keys_to_list(e_count.keys())
    
    '''
    #nb_included_d = compute_nb_pair_for_context_included(d_count)
    #nb_included_e = compute_nb_pair_for_context_included(e_count)
    #nb_included_o = compute_nb_pair_for_context_included(o_count)

    # 1) first pattern
    #p = compute_pattern(nb_included_e,nb_included_d,nb_included_o)
    #res = check_pattern_on_file(p,"./director_work_pattern_dataset")
    #print(p)
    #print(res)
    #['directed-inv'], ['skos:preflabel'], ['wascreatedonyear']]
    #(0.7588806315115741, 512208, 674952) 
    # p1 = p

    # nb_p1_found = 512208


    # 2) the first pattern cover 75% with find a second one on the rest of the dataset
    PATTERN_DATASET = "./director2_work_pattern_dataset"
    #e_count, d_count, o_count = compute_nb_pair_per_context(PATTERN_DATASET)
    '''
    with open("e_director2_work_count","w") as output_file:
        json.dump(e_count,output_file)
    with open("d_director2_work_count","w") as output_file:
        json.dump(d_count,output_file)
    with open("o_director2_work_count","w") as output_file:
        json.dump(o_count,output_file)
    '''
    '''
    with open("o_director2_work_count") as input_file:
        o_count = json.load(input_file)
    l_all_omega_context = from_keys_to_list(o_count.keys())
    with open("d_director2_work_count") as input_file:
        d_count = json.load(input_file)
    l_all_delta_context = from_keys_to_list(d_count.keys())
    with open("e_director2_work_count") as input_file:
        e_count = json.load(input_file)
    l_all_epsilon_context = from_keys_to_list(e_count.keys())
    
    '''
    #nb_included_d = compute_nb_pair_for_context_included(d_count)
    #nb_included_e = compute_nb_pair_for_context_included(e_count)
    #nb_included_o = compute_nb_pair_for_context_included(o_count)

    #p = compute_pattern(nb_included_e,nb_included_d,nb_included_o)
    #res = check_pattern_on_file(p,"./director2_work_pattern_dataset")
    #print(p)
    #print(res)
    #[['directed-inv'], ['skos:preflabel'], ['islocatedin']] 
    # (0.5795666814137541, 94321, 162744)
    #p2 = p
    #p2_ratio = 94321/674952
    #p2_ratio = 0.1397447522194171

    # nb_p2_found = 94321
# nb_p1_p2_found = 512208 + 94321 = 606529
    
    
    # 3) 2 patterns have been found, chech the support with check_patterns_ .
    patterns = []
    patterns.append([['directed-inv'], ['skos:preflabel'], ['wascreatedonyear']])
    patterns.append([['directed-inv'], ['skos:preflabel'], ['islocatedin']])
    for pattern in patterns:
        print(pattern)
    res = check_patterns_on_file(patterns,"./director_work_pattern_dataset")  
    print(res)

    # 4) Additional checks
    # p2 first, then p1
    #p2 = [['directed-inv'], ['skos:preflabel'], ['islocatedin']]  
    #res2 = check_pattern_on_file(p2,"./director_work_pattern_dataset")
    #print(p2)
    #print(res2)
    #['directed-inv'], ['skos:preflabel'], ['islocatedin']]
    #(0.7288118266187817, 491913, 674952)
    
    # nb_p2_found = 491913


    #p1 = [['directed-inv'], ['skos:preflabel'], ['wascreatedonyear']] 
    # file director_work_pattern_check contains item not matched with p2
    #res1 = check_pattern_on_file(p1,"./director_work_pattern_check")
    #print(p1)
    #print(res1)
    #[['directed-inv'], ['skos:preflabel'], ['wascreatedonyear']]
    #(0.6261834909500161, 114616, 183039)

    # nb_p1_found = 114616
    # nb_p2_p1_found = 491913 + 114616 = 606529

    # nb_p1_p2_found == nb_p2_p1_found 
    # check pattern on all pair of books
    #with open(R_METRICS_FILM) as input_file:
    #    r_metrics = json.load(input_file)
    #patterns = []
    #patterns.append([['directed-inv'], ['skos:preflabel'], ['wascreatedonyear']])
    #patterns.append([['directed-inv'], ['skos:preflabel'], ['islocatedin']])
    #res = check_patterns_on_r_metrics(patterns,r_metrics)
    #print(res)
