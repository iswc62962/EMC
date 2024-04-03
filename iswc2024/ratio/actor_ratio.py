# table and bar chart generation
from Lib import *
import json
from Ratio import *

DB_ACTOR = "./Actor/DB_Actor"
YAGO_ACTOR = "./Actor/YAGO_actor"

# we use the convertion of DB/YAGO label to id done previously 
# (files are on serv/reset4)
# the mapping of label to ids is in these 2 files:
DB_IDS = "./Actor/DB_Actor_ids"
YAGO_IDS = "./Actor/YAGO_Actor_ids"

# And the dicts of triple with ids are:
DB_TRIPLES = "./Actor/DB_Actor_triples" 
YAGO_TRIPLES = "./Actor/YAGO_Actor_triples"

# r_metric for actor
R_METRICS = "./Actor/edo_actor_index2.r.m"


SAMEAS_PAIR_FILE = "./Actor/Actor.Goldstandard.txt"

# the preprocess convert pair lable file to id file
def preprocess():
    pairs = load_pair(SAMEAS_PAIR_FILE) 
    with open(DB_IDS) as input_file:
        d_DB_ids = json.load(input_file)
    with open(YAGO_IDS) as input_file:
        d_YAGO_ids = json.load(input_file)
    d_DB_ids_reversed = reverse_dict(d_DB_ids)
    d_YAGO_ids_reversed = reverse_dict(d_YAGO_ids)

    pairs_reversed = []
    for name1,name2 in pairs:
        id1 = d_DB_ids_reversed[name1]
        id2 = d_YAGO_ids_reversed[name2]
        pairs_reversed.append((id1,id2))
    return pairs_reversed

if __name__ == "__main__":
    # same as stuff
    with open(DB_TRIPLES) as input_file:
        DB_dict = json.load(input_file)
    with open(YAGO_TRIPLES) as input_file:
        YAGO_dict = json.load(input_file)
 
    sameas_pairs_ids = preprocess()
    sameas_r_metrics = compute_r_owlsameas2(sameas_pairs_ids,DB_dict,YAGO_dict)
    sameas_r_metrics_epsilon = compute_r_metrics_for_all_epsilon(sameas_r_metrics)
    sameas_rme_ranked = rank_r_metrics_epsilon(sameas_r_metrics_epsilon)
   
    # assert
    all_same_as = 0
    for item in sameas_rme_ranked:
        all_same_as += item[1]
    assert(all_same_as == 5220)

    # all pair stuff
    r_metrics = {}
    with open(R_METRICS) as input_file:
        r_metrics = json.load(input_file)
    r_metrics_epsilon = compute_r_metrics_for_all_epsilon(r_metrics)

    # assert
    all_pair = 0
    for key in r_metrics_epsilon:
        all_pair += r_metrics_epsilon[key]
    assert(all_pair == 629618168)

    sameas_rme_pareto = pareto(5220,sameas_rme_ranked)

    # print here data for table
    #compute_sameas_ratio_rank(sameas_rme_pareto,r_metrics_epsilon)
   
    
    # print here data for bar chart
    # to print bar chart detail go in Ratio.py and uncomment # print detail section
    print("epsilon\tinitial sameas ratio\tnb sameas > 0.8\tall sameas\tnb sameas > 0.8/all sameas"+"\t"+ "mean ratio" )
    initial_ratio = 1.484811146005401e-06
    e1 = []
    e1_r_metrics = compute_r_metrics_for_one_epsilon(r_metrics,e1)
    sameas_e1_r_metrics = compute_r_metrics_for_one_epsilon(sameas_r_metrics,e1)
    compute_sameas_ratio(sameas_e1_r_metrics,e1_r_metrics,initial_ratio,927,e1)
   
    initial_ratio = 7.12916906848861e-05 
    nb_sameas = 292 
    e2 = ['wasbornonyear']
    e2_r_metrics = compute_r_metrics_for_one_epsilon(r_metrics,e2)
    sameas_e2_r_metrics = compute_r_metrics_for_one_epsilon(sameas_r_metrics,e2)
    compute_sameas_ratio(sameas_e2_r_metrics,e2_r_metrics,initial_ratio,nb_sameas,e2)
    
    initial_ratio = 0.02387832699619772
    nb_sameas = 157
    e3 = ['diedonyear', 'wasbornonyear']
    e3_r_metrics = compute_r_metrics_for_one_epsilon(r_metrics,e3)
    sameas_e3_r_metrics = compute_r_metrics_for_one_epsilon(sameas_r_metrics,e3)
    compute_sameas_ratio(sameas_e3_r_metrics,e3_r_metrics,initial_ratio,nb_sameas,e3)
    
    initial_ratio = 0.018084291187739465
    nb_sameas = 118
    e4 = ['wasbornondate', 'wasbornonyear']
    e4_r_metrics = compute_r_metrics_for_one_epsilon(r_metrics,e4)
    sameas_e4_r_metrics = compute_r_metrics_for_one_epsilon(sameas_r_metrics,e4)
    compute_sameas_ratio(sameas_e4_r_metrics,e4_r_metrics,initial_ratio,nb_sameas,e4)
  
    initial_ratio = 0.009782030834662414
    nb_sameas = 92 
    e5 = ['actedin']
    e5_r_metrics = compute_r_metrics_for_one_epsilon(r_metrics,e5)
    sameas_e5_r_metrics = compute_r_metrics_for_one_epsilon(sameas_r_metrics,e5)
    compute_sameas_ratio(sameas_e5_r_metrics,e5_r_metrics,initial_ratio,nb_sameas,e5)
   
    initial_ratio = 0.2
    nb_same_as = 68
    e6 = ['actedin', 'wasbornonyear']
    e6_r_metrics = compute_r_metrics_for_one_epsilon(r_metrics,e6)
    sameas_e6_r_metrics = compute_r_metrics_for_one_epsilon(sameas_r_metrics,e6)
    compute_sameas_ratio(sameas_e6_r_metrics,e6_r_metrics,initial_ratio,nb_same_as,e6)
    
    initial_ratio = 0.7102803738317757
    nb_same_as = 76
    e7 = ['wasbornin', 'wasbornondate', 'wasbornonyear']
    e7_r_metrics = compute_r_metrics_for_one_epsilon(r_metrics,e7)
    sameas_e7_r_metrics = compute_r_metrics_for_one_epsilon(sameas_r_metrics,e7)
    compute_sameas_ratio(sameas_e7_r_metrics,e7_r_metrics,initial_ratio,nb_same_as,e7)
 
