# edo index2.r.m generation
from Lib import *

DB_UNIVERSITY = "./University/DB_University"
YAGO_UNIVERSITY = "./University/YAGO_university"

def preprocess():
    DB_dict = load_triples_to_dict(DB_UNIVERSITY)
    YAGO_dict = load_triples_to_dict(YAGO_UNIVERSITY)

    DB_dict_ids = compute_ids_for_DB_or_YAGO(DB_dict,"DB_University_ids")
    YAGO_dict_ids = compute_ids_for_DB_or_YAGO(YAGO_dict,"YAGO_University_ids")

    with open("DB_University_triples","w") as input_file:
        json.dump(DB_dict_ids,input_file)
    
    with open("YAGO_University_triples","w") as input_file:
        json.dump(YAGO_dict_ids,input_file)

    #print(len(DB_dict_ids))
    #print(len(YAGO_dict_ids))

def prepare_batches(DB_dict,YAGO_dict):
    i = 0
    for db_entry in DB_dict:
        with open("./batches/batch_" + str(i),"w") as write_file:
            for yago_entry in YAGO_dict:
                write_file.write(str(db_entry) + "\t" + str(yago_entry)+"\n")
            i += 1 


if __name__ == "__main__":
    ######################
    ## 1) preprocess 
    #preprocess()

    ######################
    ## 2) batches
    #DB_dict = {}
    #YAGO_dict = {}
    #with open("DB_University_triples") as input_file:
    #    DB_dict = json.load(input_file)
    #with open("YAGO_University_triples") as input_file:
    #    YAGO_dict = json.load(input_file)

    #prepare_batches(DB_dict,YAGO_dict)
 
    ######################
    ## 3) compute relation for each batch
    #DB_dict = {}
    #YAGO_dict = {}
    #with open("DB_University_triples") as input_file:
    #    DB_dict = json.load(input_file)
    #with open("YAGO_University_triples") as input_file:
    #    YAGO_dict = json.load(input_file)

    #for i in range(0,100):
    #for i in range(100,200):
    #for i in range(200,10000):
    #for i in range(10000,10353):
    #    batch = "./batches/batch_" + str(i)
    #    compute_r_json(DB_dict,YAGO_dict,batch,batch)

    ######################
    ## 4) index batch results metrics only
    #edo_index_prefix = "edo_university_index"
    
    #with open(edo_index_prefix + ".r.m") as input_file:
    #    d_index_metrics = json.load(input_file)

    #for i in range(0,2):
    #for i in range(0,100):
    #for i in range(100,200):
    #for i in range(200,10000):
    #for i in range(10000,10353):
    #    batch = "./batches/batch_" + str(i)
    #    index_r_json_metrics_only(batch,d_index_metrics,23352)  

    #with open(edo_index_prefix + ".r.m","w") as output_file:
    #    json.dump(d_index_metrics,output_file)
    
    ######################
    ## 5) check point charlie
    #edo_index_prefix = "edo_university_index"
    #with open(edo_index_prefix + ".r.m") as input_file:
    #    d_index_metrics = json.load(input_file)

    #all_pairs = 0
    #for key in d_index_metrics:
    #    all_pairs += d_index_metrics[key]
    #assert(all_pairs == 241763256)
    
    ######################
    # 6)
    #d_identity = compute_identity_relation(d_index_metrics)
    #all_pairs = 0
    #for key in d_identity:
    #    print(key + " : "  + str(d_identity[key]))
    #    all_pairs += d_identity[key]
    #print(all_pairs) 
 
    ######################
    ######################
    # 7) or do it with no batches
    #with open("DB_University_triples") as input_file:
    #    DB_dict_ids = json.load(input_file)
    #with open("YAGO_University_triples") as input_file:
    #    YAGO_dict_ids = json.load(input_file)
    #d_metric = compute_r(DB_dict_ids,YAGO_dict_ids)

    #with open("edo_university_index2.r.m","w") as output_file:
    #    json.dump(d_metric,output_file)

    # check
    with open("edo_university_index2.r.m") as input_file:
        d_metrics = json.load(input_file)
    all_pairs = 0
    for key in d_metrics:
        all_pairs += d_metrics[key]
    assert(all_pairs == 241763256) 
    
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
    
    # compute difference relations
    r_contextual_diff = 0
    pair_contextual_diff = 0
    r_full_given_diff = 0
    pair_full_given_diff = 0

    d_diff = compute_difference_relation(d_metrics)
    r_contextual_diff = len(d_diff)
    for key in d_diff:
        r_full_given_diff += d_diff[key][0]
        pair_full_given_diff += d_diff[key][1]

    pair_contextual_diff = pair_full_given_diff
    print()
    print("Difference")
    print(r_contextual_diff)
    print(r_full_given_diff)
    print(r_full)
    print()
    print(pair_contextual_diff)
    print(pair_full_given_diff)
    print(pairs_full)


    
    # compute partitions 
    print()
    partition(d_metrics,r_full,all_pairs)


