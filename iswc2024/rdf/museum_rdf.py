# museum ttl generation
from Lib import *
from rdflib import Graph, Literal, Namespace, URIRef, RDF, RDFS, XSD
from urllib.parse import quote
import json

DB_MUSEUM = "./Museum/DB_Museum"
YAGO_MUSEUM = "./Museum/YAGO_museum"
PREFIX = "iswc:"

def preprocess():
    DB_dict = load_triples_to_dict(DB_MUSEUM)
    YAGO_dict = load_triples_to_dict(YAGO_MUSEUM)

    DB_dict_ids = compute_ids_for_DB_or_YAGO(DB_dict,"DB_Museum_ids")
    YAGO_dict_ids = compute_ids_for_DB_or_YAGO(YAGO_dict,"YAGO_Museum_ids")

    with open("DB_Museum_triples","w") as input_file:
        json.dump(DB_dict_ids,input_file)
    
    with open("YAGO_Museum_triples","w") as input_file:
        json.dump(YAGO_dict_ids,input_file)

    print(len(DB_dict_ids))
    print(len(YAGO_dict_ids))

def DB_or_YAGO_2_ttl(g,DBorYAGO_dict,s_label):
    iswc = Namespace("http://iswc.org/")
    for key in DBorYAGO_dict:
        for s,p,o in DBorYAGO_dict[key]:
            s_ttl = URIRef(quote(s + "_" + s_label))
            p_ttl = URIRef("iswc:"+p) if ":" not in p else URIRef(p)
            o_ttl = Literal(o)
            g.add((s_ttl,p_ttl,o_ttl))
    
    # keep this lon for after
    #g.add((s_ttl,URIRef("iswc:"+"emc1"),s_ttl))

def emc_as_a_predicate(predicate,pairs,graphe):
    for pair in pairs:
        DB_id = DB_dict_ids[pair[0]]
        YAGO_id = YAGO_dict_ids[pair[1]]
        pair1_ttl = URIRef(quote(DB_id + "_" + "db"))
        pair2_ttl = URIRef(quote(YAGO_id + "_" + "yago"))
        # add
        graphe.add((pair1_ttl,pair_p_ttl,pair2_ttl))
        graphe.add((pair2_ttl,pair_p_ttl,pair1_ttl))

def includes_predicate(context,context_label,d_context,graphe):
    d_context[str(context)] = context_label
    # add includes predicate for epsilon
    s_ttl = URIRef(PREFIX+d_context[str(context)])
    g.add( (s_ttl,URIRef(PREFIX+"size"),Literal(len(context),datatype=XSD.integer)) )
    g.add( (s_ttl,URIRef(RDF.type),URIRef(PREFIX+"Context")) )
    for prop in context:
        prop_ttl = URIRef("iswc:"+prop) if ":" not in prop else URIRef(prop)
        g.add((s_ttl,URIRef(PREFIX+"includes"),prop_ttl))

if __name__ == "__main__":
    # 1) preprocess
    #preprocess()
    
    # 2) ompute edo and save res in json
    '''
    with open("DB_Museum_triples") as input_file:
        DB_dict_ids = json.load(input_file)
    with open("YAGO_Museum_triples") as input_file:
        YAGO_dict_ids = json.load(input_file)
    d_metric, d_pair = compute_r_2(DB_dict_ids,YAGO_dict_ids)

    with open("edo_museum_index2.r.m","w") as output_file:
        json.dump(d_metric,output_file)
 
    with open("edo_museum_index2.r","w") as output_file:
        json.dump(d_pair,output_file)
        '''
    # 3) generate ttl graphs
    DB_dict = load_triples_to_dict(DB_MUSEUM)
    YAGO_dict = load_triples_to_dict(YAGO_MUSEUM)

    g = Graph()
    # 3.1) put DB and YAGO in the graph
    DB_or_YAGO_2_ttl(g,DB_dict,"db") 
    DB_or_YAGO_2_ttl(g,YAGO_dict,"yago") 

    # 3.2) put emc as prediacte and as object in the graph
    # we need ids
    with open("DB_Museum_ids") as input_file:
        DB_dict_ids = json.load(input_file)
    with open("YAGO_Museum_ids") as input_file:
        YAGO_dict_ids = json.load(input_file)

    # for real
    '''
    with open("edo_museum_index2.r") as input_file:
        d_pair = json.load(input_file)
    # for test
    iteration = 0
    d_pair_test = {}
    for edo in d_pair:
        edo_str = edo.replace("][","],[")
        edo_py = eval("["+edo_str+"]")
        e = edo_py[0]
        d = edo_py[1]
        o = edo_py[2]
        if e != [] and d != [] and o != []:
            d_pair_test[edo] = d_pair[edo]
            iteration += 1
            if iteration == 5:
                break
    
    with open("d_pair_test","w") as output_file:
        json.dump(d_pair_test,output_file)
    '''
    # iwsc:emc and iswc:e, iswc:d, iswc:o index 
    emc_index = 0
    e_index = 0
    d_index = 0
    o_index = 0
    # we need to index iswc:e, iswc:d, iswc:o 
    d_epsilon = {}
    d_delta = {}
    d_omega = {}

    with open("d_pair_test") as input_file:
        d_pair_test = json.load(input_file)

    # FOR TEST
    d_pair= d_pair_test
    for edo in d_pair:
        # index all iswc:e, iswc:d, iswc:o 
        edo_str = edo.replace("][","],[")
        edo_py = eval("["+edo_str+"]")
    
        # 3.2.1 include predicate
        # include predicate for e  
        e = edo_py[0]    
        if str(e) not in d_epsilon:
            includes_predicate(e,"e_" + str(e_index),d_epsilon,g)
            e_index += 1
        e_label = d_epsilon[str(e)]
        
        # include predicate for d  
        d = edo_py[1]    
        if str(d) not in d_delta:
            includes_predicate(d,"d_" + str(d_index),d_delta,g)
            d_index += 1
        d_label = d_delta[str(d)]
   
        # include predicate for o  
        o = edo_py[2]    
        if str(o) not in d_omega:
            includes_predicate(o,"o_" + str(o_index),d_omega,g)
            o_index += 1
        o_label = d_omega[str(o)]
      

        # 3.2.2 emc as a subject
        edo_s_ttl = URIRef(PREFIX+"emc_" + str(emc_index) + "_" + e_label + "_" + d_label + "_" + o_label)
        edo_p_ttl = RDF.type
        #edo_o_ttl= URIRef(PREFIX+"EntityMatchingContext")
        edo_o_ttl= URIRef(PREFIX+"EMC")
        
        # add rdf type predicate
        g.add((edo_s_ttl,edo_p_ttl,edo_o_ttl)) 
        
        # 3.2.3 add epsilon, delta, omega predicate
        e_s_ttl = URIRef(PREFIX+e_label)
        g.add((edo_s_ttl,URIRef(PREFIX+"epsilon"),e_s_ttl))
        
        d_s_ttl = URIRef(PREFIX+d_label)
        g.add((edo_s_ttl,URIRef(PREFIX+"delta"),d_s_ttl))
   
        o_s_ttl = URIRef(PREFIX+o_label)
        g.add((edo_s_ttl,URIRef(PREFIX+"omega"),o_s_ttl))
   
        # 3.2.3 emc as predicate
        pair_p_ttl = edo_s_ttl
        pairs = d_pair[edo]
        emc_as_a_predicate(pair_p_ttl,pairs,g)
        # warn the indent
        emc_index += 1
    print(g.serialize(format="turtle"))
