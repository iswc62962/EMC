import math
import json
FILTERED_PROPERTIES = []

def get_properties(instance):
    properties = set()
    for s,p,o in instance:
        if p not in properties:
            properties.add(p)
    return properties

def get_property_values(prop,instance):
    values = []
    for s,p,o in instance:
        if p == prop:
            values.append(o)
    return values

def compute_shared_unshared_properties(pair):
    i1_properties = get_properties(pair[0])
    i2_properties = get_properties(pair[1])
    
    shared_properties = i1_properties & i2_properties
    unshared_properties = i1_properties ^ i2_properties

    return shared_properties, unshared_properties

# compute the relation
def compute_r_owlsameas3(pair_list,dict_of_DB,dict_of_YAGO):
    r_metrics = {}
    for id1,i2 in pair_list:
        i1 = dict_of_DB[id1]
        i2 = dict_of_YAGO[id2]
        e,d,op,ov = compute_edo_for_a_pair3(i1,i2,id1,id2)
        # op & ov fusion
        #TODO
        key_r = str(e)+str(d)+str(o)
        if key_r not in r_metrics:
            r_metrics[key_r] = 0
        r_metrics[key_r] += 1
    return r_metrics

def compute_r_owlsameas2(pair_list,dict_of_DB,dict_of_YAGO):
    r_metrics = {}
    for id1,id2 in pair_list:
        i1 = dict_of_DB[id1]
        i2 = dict_of_YAGO[id2]
        e,d,o = compute_edo_for_a_pair2(i1,i2,id1,id2)
        key_r = str(e)+str(d)+str(o)
        if key_r not in r_metrics:
            r_metrics[key_r] = 0
        r_metrics[key_r] += 1
    return r_metrics





def compute_edo_for_a_pair2(i1,i2,id_i1,id_i2):
        # epsilon: the set of properties with the same values
        # delta: the set of properties with different values
        # omega: the set of unshared properties
        epsilon, delta, omega = [],[],[]
        shared,unshared = compute_shared_unshared_properties((i1,i2))

        i1_properties = get_properties(i1)
        i2_properties = get_properties(i2)

        # shared and unsahred properties must cover all properties
        assert(set(list(i1_properties) + list(i2_properties)) == set(list(shared) + list(unshared))) 

        # for each property in shared
        for p in shared:
            # filter properties
            if p in FILTERED_PROPERTIES:
                continue

            # list of values for instances x and y     
            i1_list_of_values = get_property_values(p,i1)
            i2_list_of_values = get_property_values(p,i2)
            
            # we consider all properties as data properties
            i1_set_of_values = set(i1_list_of_values)
            i2_set_of_values = set(i2_list_of_values)

            i1_and_i2 = i1_set_of_values & i2_set_of_values
            i1_xor_i2 = i1_set_of_values ^ i2_set_of_values
 
            if len(i1_and_i2) != 0:
                epsilon.append(p)
            if len(i1_xor_i2) != 0:
                delta.append(p)
            # we can not have both sets empty 
            if len(i1_and_i2) == 0 and len(i1_xor_i2) ==0:
                raise exception("values/properties exception")

        for p in unshared:
            # filter properties
            if p in FILTERED_PROPERTIES:
                continue
            omega.append(p)

        # sort epsilon, delta omega in oder to use them as dict keys
        epsilon.sort()
        delta.sort()
        omega.sort()

        return epsilon,delta,omega



# compute edo for a pair with 2 omega
def compute_edo_for_a_pair3(i1,i2,id_i1,id_i2):
        # epsilon: the set of properties with the same values
        # delta: the set of properties with different values
        # omega: the set of unshared properties
        epsilon, delta, omega_p, omega_v = [],[],[],[]
        shared,unshared = compute_shared_unshared_properties((i1,i2))

        i1_properties = get_properties(i1)
        i2_properties = get_properties(i2)

        # shared and unsahred properties must cover all properties
        assert(set(list(i1_properties) + list(i2_properties)) == set(list(shared) + list(unshared))) 

        # for each property in shared
        for p in shared:
            # filter properties
            if p in FILTERED_PROPERTIES:
                continue

            # list of values for instances x and y     
            i1_list_of_values = get_property_values(p,i1)
            i2_list_of_values = get_property_values(p,i2)
            
            # we consider all properties as data properties
            i1_set_of_values = set(i1_list_of_values)
            i2_set_of_values = set(i2_list_of_values)
            # at least on value in common, p in epsilon
            if i1_set_of_values.intersection(i2_set_of_values):
                epsilon.append(p)
            # set of values are subsets, value incompletness, p in omega_v
            if i1_set_of_values.issubset(i2_set_of_values) or i2_set_of_values.issubset(i1_set_of_values):
                # two same set are subset of themselves, avoid this case
                if i1_set_of_values != i2_set_of_values:
                    omega_v.append(p)
            # set of values are different and not subsets, p in delta
            if i1_set_of_values != i2_set_of_values and not(i1_set_of_values.issubset(i2_set_of_values)) and not(i2_set_of_values.issubset(i1_set_of_values)):
                delta.append(p)

            # p can not be in delta and omega_v
            p_in_delta = p in delta
            p_in_omega_v = p in omega_v
            assert(False == (p_in_delta and p_in_omega_v))

        for p in unshared:
            if p in FILTERED_PROPERTIES:
                continue
            omegai_p.append(p)

        # sort epsilon, delta omega in oder to use them as dict keys
        epsilon.sort()
        delta.sort()
        omega_p.sort()
        omega_v.sort()

        cwa_context = (epsilon,delta,omega_p,omega_v)
        # all properties must be present in the context
        flat_context = epsilon + delta + omega_p + omega_v +FILTERED_PROPERTIES
        assert(set(list(i1_properties) + list(i2_properties)) == set(flat_context))
        return epsilon,delta,omega_p,omega_v 

def load_pair(filename):
    pair_ids = []
    with open (filename) as input_file:
        lines = input_file.readlines()
        for line in lines:
            line_strip = line.strip().split('\t')
            pair_ids.append((line_strip[0],line_strip[1]))
    return pair_ids

def reverse_dict(d):
    d_reversed = {}
    for key in d:
        new_key = d[key]
        if new_key not in d_reversed:
            d_reversed[new_key] = None
        if d_reversed[new_key] != None:
            raise Exception("reverse dict failed")
        d_reversed[new_key] = key
    return d_reversed

def load_triples_to_dict(filename):
    dict_of_ids = {}
    with open (filename) as input_file:
        lines = input_file.readlines()
        for line in lines:
            line_strip = line.strip().split('\t')
            triple = (line_strip[0],line_strip[1],line_strip[2])
            if triple[0] not in dict_of_ids:
                dict_of_ids[triple[0]] = []
            dict_of_ids[triple[0]].append(triple)    
    return dict_of_ids

def compute_r_2(dict_of_DB,dict_of_YAGO):
    r_metrics = {}
    r_pair = {}
    for id1 in dict_of_DB:
        for id2 in dict_of_YAGO:
            i1 = dict_of_DB[id1]
            i2 = dict_of_YAGO[id2]
            e,d,o = compute_edo_for_a_pair2(i1,i2,id1,id2)
            key_r = str(e) + str(d) + str(o)
            if key_r not in r_metrics:
                r_metrics[key_r] = 0
                r_pair[key_r] = []
            r_metrics[key_r] += 1
            r_pair[key_r].append((id1,id2))
    return r_metrics,r_pair

def compute_ids_for_DB_or_YAGO(DBorYAGOdict,index_filename):
    # sort in order to have always the same index
    keys = sorted(list(DBorYAGOdict.keys()))
    id_s = 0
    index = {}
    DBorYAGOdict_with_index = {}
    for key in keys:
        index[id_s] = key
        DBorYAGOdict_with_index[id_s] = DBorYAGOdict[key]
        id_s += 1
    with open(index_filename,"w") as output_file:
        json.dump(index,output_file)
    return DBorYAGOdict_with_index



