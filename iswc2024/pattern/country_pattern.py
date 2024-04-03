# Compute & Check pattern for countries 
from Pattern import *
from Lib import * 

DB_BOOK = "./Book/newDB_Book"
YAGO_BOOK = "./Book/YAGO_book"

DB_MOUNTAIN = "./Mountain/DB_mountain"
YAGO_MOUNTAIN = "./Mountain/YAGO_mountain"

DB_UNIVERSITY = "./University/DB_University"
YAGO_UNIVERSITY = "./University/YAGO_university"

def DBorYAGO_common_country(DB_dict_book,DB_dict_mountain):
    book_country = []
    mountain_country = []
    for key in DB_dict_book:
        for s,p,o in DB_dict_book[key]:
            if p == "islocatedin":
                if o not in book_country:
                    book_country.append(o)
    for key in DB_dict_mountain:
        for s,p,o in DB_dict_mountain[key]:
            if p == "islocatedin":
                if o not in mountain_country:
                    mountain_country.append(o)

    return list(set(book_country) & set (mountain_country))



def extract_country(DBorYAGO,country):
    d_country = {}
    for book_id in DBorYAGO:
        found = False
        for s,p,o in DBorYAGO[book_id]:
            if p == "islocatedin" and o == country:
                found = True
                break
        if found: 
            d_country[book_id] = DBorYAGO[book_id]
    return d_country


if __name__ == "__main__":
    # 1) book mountain
    DB_dict_book = load_triples_to_dict(DB_BOOK)
    DB_dict_mountain = load_triples_to_dict(DB_MOUNTAIN)
    countries = DBorYAGO_common_country(DB_dict_book,DB_dict_mountain)
    # the number of countries
    print("book mountain")
    print(len(countries))
    #compute_pattern_dataset(countries,DB_dict_book,DB_dict_mountain,extract_country)
    #PATTERN_DATASET = "./country_pattern_dataset"
    #e_count, d_count, o_count = compute_nb_pair_per_context(PATTERN_DATASET)

    '''    
    with open("e_country_count","w") as output_file:
        json.dump(e_count,output_file)
    with open("d_country_count","w") as output_file:
        json.dump(d_count,output_file)
    with open("o_country_count","w") as output_file:
        json.dump(o_count,output_file)
    '''    
    '''    
    with open("o_country_count") as input_file:
        o_count = json.load(input_file)
    l_all_omega_context = from_keys_to_list(o_count.keys())
    with open("d_country_count") as input_file:
        d_count = json.load(input_file)
    l_all_delta_context = from_keys_to_list(d_count.keys())
    with open("e_country_count") as input_file:
        e_count = json.load(input_file)
    l_all_epsilon_context = from_keys_to_list(e_count.keys())
    '''    
    #nb_included_d = compute_nb_pair_for_context_included(d_count)
    #nb_included_e = compute_nb_pair_for_context_included(e_count)
    #nb_included_o = compute_nb_pair_for_context_included(o_count)

    # 1.1) first pattern
    #p = compute_pattern(nb_included_e,nb_included_d,nb_included_o)
    #res = check_pattern_on_file(p,"./country_pattern_dataset")
    #print(p)
    #print(res)
    #[['islocatedin'], ['skos:preflabel'], ['created-inv']]
    #(0.9579661455695491, 15320925, 15993180)    
    #[['islocatedin'], ['skos:preflabel'], ['created-inv']]
    #(0.9579661455695491, 15320925, 15993180)
     
    # 1.2) one pattern have been found check the support with with check_patterns_...
    patterns = []
    patterns.append([['islocatedin'], ['skos:preflabel'], ['created-inv']])
    for pattern in patterns:
        print(pattern)
    res = check_patterns_on_file(patterns,"./country_pattern_dataset")
    print(res)


    # 2) do the same between book and university
    DB_dict_university = load_triples_to_dict(DB_UNIVERSITY)
    countries = DBorYAGO_common_country(DB_dict_book,DB_dict_university)
    # the number of countries
    print("book university")
    print(len(countries))
    #compute_pattern_dataset(countries,DB_dict_book,DB_dict_mountain,extract_country)
    PATTERN_DATASET = "./country2_pattern_dataset"
    #e_count, d_count, o_count = compute_nb_pair_per_context(PATTERN_DATASET)
    '''
    with open("e_country2_count","w") as output_file:
        json.dump(e_count,output_file)
    with open("d_country2_count","w") as output_file:
        json.dump(d_count,output_file)
    with open("o_country2_count","w") as output_file:
        json.dump(o_count,output_file)
 
    '''
    '''
    with open("o_country2_count") as input_file:
        o_count = json.load(input_file)
    l_all_omega_context = from_keys_to_list(o_count.keys())
    with open("d_country2_count") as input_file:
        d_count = json.load(input_file)
    l_all_delta_context = from_keys_to_list(d_count.keys())
    with open("e_country2_count") as input_file:
        e_count = json.load(input_file)
    l_all_epsilon_context = from_keys_to_list(e_count.keys())
    
    '''
    #nb_included_d = compute_nb_pair_for_context_included(d_count)
    #nb_included_e = compute_nb_pair_for_context_included(e_count)
    #nb_included_o = compute_nb_pair_for_context_included(o_count)
    # 2.1) first pattern
    #p = compute_pattern(nb_included_e,nb_included_d,nb_included_o)
    #res = check_pattern_on_file(p,"./country2_pattern_dataset")
    #print(p)
    #print(res)
    #[['islocatedin'], ['skos:preflabel'], ['created-inv']]
    #(0.957966700852281, 15320840, 15993082)
    #['islocatedin'], ['skos:preflabel'], ['created-inv']]
    #(0.957966700852281, 15320840, 15993082)
    
    # 2.2) one pattern have been found check the support with with check_patterns_...
    patterns = []
    patterns.append([['islocatedin'], ['skos:preflabel'], ['created-inv']])
    for pattern in patterns:
        print(pattern)
    res = check_patterns_on_file(patterns,"country2_pattern_dataset")
    print(res)


    # 3) do the same between university and mountain
    countries = DBorYAGO_common_country(DB_dict_university,DB_dict_mountain)
    # The number of countries
    print("university mountain") 
    print(len(countries))
    #compute_pattern_dataset(countries,DB_dict_university,DB_dict_mountain,extract_country)
    PATTERN_DATASET = "./country3_pattern_dataset"
    #e_count, d_count, o_count = compute_nb_pair_per_context(PATTERN_DATASET)
    '''
    with open("e_country3_count","w") as output_file:
        json.dump(e_count,output_file)
    with open("d_country3_count","w") as output_file:
        json.dump(d_count,output_file)
    with open("o_country3_count","w") as output_file:
        json.dump(o_count,output_file)
    '''
    '''
    with open("o_country3_count") as input_file:
        o_count = json.load(input_file)
    l_all_omega_context = from_keys_to_list(o_count.keys())
    with open("d_country3_count") as input_file:
        d_count = json.load(input_file)
    l_all_delta_context = from_keys_to_list(d_count.keys())
    with open("e_country3_count") as input_file:
        e_count = json.load(input_file)
    l_all_epsilon_context = from_keys_to_list(e_count.keys())
    
    '''
    #nb_included_d = compute_nb_pair_for_context_included(d_count)
    #nb_included_e = compute_nb_pair_for_context_included(e_count)
    #nb_included_o = compute_nb_pair_for_context_included(o_count)
    # 3.1) fisrt pattern
    #p = compute_pattern(nb_included_e,nb_included_d,nb_included_o)
    #res = check_pattern_on_file(p,"./country3_pattern_dataset")
    #print(p)
    #print(res)
    #[['islocatedin'], ['islocatedin'], ['haslatitude', 'haslongitude']]
    # (0.5988531757136322, 2871907, 4795678)
    #[['islocatedin'], ['islocatedin'], ['haslatitude', 'haslongitude']]
    # (0.5988531757136322, 2871907, 4795678)
    n = 4795678
    #  work on the 40% left by the pattern computed above
    PATTERN_DATASET = "./country31_pattern_dataset"
    #e_count, d_count, o_count = compute_nb_pair_per_context(PATTERN_DATASET)
    '''
    with open("e_country31_count","w") as output_file:
        json.dump(e_count,output_file)
    with open("d_country31_count","w") as output_file:
        json.dump(d_count,output_file)
    with open("o_country31_count","w") as output_file:
        json.dump(o_count,output_file)
    '''
    '''
    with open("o_country31_count") as input_file:
        o_count = json.load(input_file)
    l_all_omega_context = from_keys_to_list(o_count.keys())
    with open("d_country31_count") as input_file:
        d_count = json.load(input_file)
    l_all_delta_context = from_keys_to_list(d_count.keys())
    with open("e_country31_count") as input_file:
        e_count = json.load(input_file)
    l_all_epsilon_context = from_keys_to_list(e_count.keys())

    '''
    #nb_included_d = compute_nb_pair_for_context_included(d_count)
    #nb_included_e = compute_nb_pair_for_context_included(e_count)
    #nb_included_o = compute_nb_pair_for_context_included(o_count)
    # 3.2) second pattern
    #p = compute_pattern(nb_included_e,nb_included_d,nb_included_o)
    #res = check_pattern_on_file(p,"./country31_pattern_dataset")
    #print(p)
    #print(res)
    #['islocatedin'], ['islocatedin'], ['graduatedfrom-inv']]
    #(0.40754382928113586, 784021, 1923771)
    #[['islocatedin'], ['islocatedin'], ['graduatedfrom-inv']]
    #(0.40754382928113586, 784021, 1923771)

    #p2 = p
    #p2_ratio =  784021/n
    #p2_ratio = 0.1634849128736333

    # work on the left of previous step
    PATTERN_DATASET = "./country32_pattern_dataset"
    #e_count, d_count, o_count = compute_nb_pair_per_context(PATTERN_DATASET)
    '''
    with open("e_country32_count","w") as output_file:
        json.dump(e_count,output_file)
    with open("d_country32_count","w") as output_file:
        json.dump(d_count,output_file)
    with open("o_country32_count","w") as output_file:
        json.dump(o_count,output_file)
    '''
    '''
    with open("o_country32_count") as input_file:
        o_count = json.load(input_file)
    l_all_omega_context = from_keys_to_list(o_count.keys())
    with open("d_country32_count") as input_file:
        d_count = json.load(input_file)
    l_all_delta_context = from_keys_to_list(d_count.keys())
    with open("e_country32_count") as input_file:
        e_count = json.load(input_file)
    l_all_epsilon_context = from_keys_to_list(e_count.keys())
    '''
    #nb_included_d = compute_nb_pair_for_context_included(d_count)
    #nb_included_e = compute_nb_pair_for_context_included(e_count)
    #nb_included_o = compute_nb_pair_for_context_included(o_count)
    # 3.3) third pattern
    #p = compute_pattern(nb_included_e,nb_included_d,nb_included_o)
    #res = check_pattern_on_file(p,"./country32_pattern_dataset")
    #print(p)
    #print(res)
    #[['islocatedin'], ['islocatedin'], []]
    #(0.6581820574687431, 750163, 1139750) 
    #p3 = p
    #p3_ratio = 750163/n
    #p3_ratio = 0.1564248058355878
    
    # work on the left of the previous step 
    #PATTERN_DATASET = "./country33_pattern_dataset"
    #e_count, d_count, o_count = compute_nb_pair_per_context(PATTERN_DATASET)

    '''
    with open("e_country33_count","w") as output_file:
        json.dump(e_count,output_file)
    with open("d_country33_count","w") as output_file:
        json.dump(d_count,output_file)
    with open("o_country33_count","w") as output_file:
        json.dump(o_count,output_file)
    '''
    '''
    with open("o_country33_count") as input_file:
        o_count = json.load(input_file)
    l_all_omega_context = from_keys_to_list(o_count.keys())
    with open("d_country33_count") as input_file:
        d_count = json.load(input_file)
    l_all_delta_context = from_keys_to_list(d_count.keys())
    with open("e_country33_count") as input_file:
        e_count = json.load(input_file)
    l_all_epsilon_context = from_keys_to_list(e_count.keys())
    '''
    #nb_included_d = compute_nb_pair_for_context_included(d_count)
    #nb_included_e = compute_nb_pair_for_context_included(e_count)
    #nb_included_o = compute_nb_pair_for_context_included(o_count)
    #p = compute_pattern(nb_included_e,nb_included_d,nb_included_o)
    #res = check_pattern_on_file(p,"./country33_pattern_dataset")
    # 3.4) fourth pattern
    #print(p)
    #print(res)
    #[['islocatedin'], ['islocatedin'], ['hasmotto']]
    #(0.7766044554874778, 302555, 389587)

    #p4 = p
    #p4_ratio = 302555/n
    #p4_ratio = 0.0630890981421188

    # check if 80\% support is reached
    #nb_p1_p2_p3_p4 = 2871907 + 784021 + 750163 + 302555 = 4708646
    
    # p4 first
    p1 = [['islocatedin'], ['islocatedin'], ['haslatitude', 'haslongitude']]
    p2 = [['islocatedin'], ['islocatedin'], ['graduatedfrom-inv']]
    p3 = [['islocatedin'], ['islocatedin'], []]
    p4 = [['islocatedin'], ['islocatedin'], ['hasmotto']]

    #res = check_pattern_on_file(p4,"country3_pattern_dataset") 
    #print(res)
    #(0.37216093324030514, 1784764, 4795678)
    #res = check_pattern_on_file(p3,"country_pattern_check1")
    #print(res)
    #(0.24914793315252445, 750163, 3010914)
    #res = check_pattern_on_file(p2,"country_pattern_check2")
    #print(res)
    #(0.4310461435160263, 974488, 2260751)
    #res = check_pattern_on_file(p1,"country_pattern_check3")
    #print(res)
    #(0.9323373213720678, 1199231, 1286263) 

    #nb_p4_p3_p2_p1 = 1784764 + 750163 +974488+1199231 = 4708646
    # final ratio = 0.981851992564972
    
    # each pattern individual
    
    #res = check_pattern_on_file(p4,"country3_pattern_dataset") 

    #res_p1 = check_pattern_on_file(p1,"country3_pattern_dataset") 
    #print(res_p1)
    #res_p2 = check_pattern_on_file(p2,"country3_pattern_dataset") 
    #print(res_p2)
    #res_p3 = check_pattern_on_file(p3,"country3_pattern_dataset") 
    #print(res_p3)
    #res_p4 = check_pattern_on_file(p4,"country3_pattern_dataset") 
    #print(res_p4)

    #(0.5988531757136322, 2871907, 4795678)
    #(0.4211321110383141, 2019614, 4795678)  
    #(0.1564248058355878, 750163, 4795678)
    #(0.37216093324030514, 1784764, 4795678)

    # 7) 4 patterns have been found, chech the support with check_patterns_ .
    patterns = []
    patterns.append(p1)
    patterns.append(p2)
    patterns.append(p3)
    patterns.append(p4)
    for pattern in patterns:
        print(pattern)
    res = check_patterns_on_file(patterns,"./country3_pattern_dataset")  
    print(res)

 


    # 8) Not used
    #PATTERN_DATASET = "./country34_pattern_dataset"
    #e_count, d_count, o_count = compute_nb_pair_per_context(PATTERN_DATASET)
    '''
    with open("e_country34_count","w") as output_file:
        json.dump(e_count,output_file)
    with open("d_country34_count","w") as output_file:
        json.dump(d_count,output_file)
    with open("o_country34_count","w") as output_file:
        json.dump(o_count,output_file)
    
    '''
    '''
    with open("o_country34_count") as input_file:
        o_count = json.load(input_file)
    l_all_omega_context = from_keys_to_list(o_count.keys())
    with open("d_country34_count") as input_file:
        d_count = json.load(input_file)
    l_all_delta_context = from_keys_to_list(d_count.keys())
    with open("e_country34_count") as input_file:
        e_count = json.load(input_file)
    l_all_epsilon_context = from_keys_to_list(e_count.keys())
    
    '''
    #nb_included_d = compute_nb_pair_for_context_included(d_count)
    #nb_included_e = compute_nb_pair_for_context_included(e_count)
    #nb_included_o = compute_nb_pair_for_context_included(o_count)
    #p = compute_pattern(nb_included_e,nb_included_d,nb_included_o)
    #res = check_pattern_on_file(p,"./country34_pattern_dataset")
    #print(p)
    #print(res)
    #[['islocatedin'], ['islocatedin'], ['wascreatedondate', 'wascreatedonyear']]
    #(0.3312344884640132, 28828, 87032)
 
    #p5 = p
    #p5_ratio = 28828/n
    #p5_ratio = 0.006011245959382594

