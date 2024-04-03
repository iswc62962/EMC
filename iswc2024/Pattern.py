from Lib import *

def compute_nb_pair_per_context(pattern_dataset):
    d_e_count = {}
    d_d_count = {}
    d_o_count = {}
    size1_e_context_list = []
    size1_d_context_list = []
    size1_o_context_list = []

    with open(pattern_dataset) as input_file:
        lines = input_file.readlines()
        for line in lines:
            line_strip = line.strip()
            edo = eval(line_strip)
            e = edo[0]
            d = edo[1]
            o = edo[2]
            
            if str(e) not in d_e_count:
                d_e_count[str(e)] = 0
            d_e_count[str(e)] += 1
            
            if str(d) not in d_d_count:
                d_d_count[str(d)] = 0
            d_d_count[str(d)] += 1

            if str(o) not in d_o_count:
                d_o_count[str(o)] = 0
            d_o_count[str(o)] += 1
   
            if len(e) == 1 and e not in size1_e_context_list:
                size1_e_context_list.append(e)
            if len(d) == 1 and d not in size1_d_context_list:
                size1_d_context_list.append(d)
            if len(o) == 1 and o not in size1_o_context_list:
                size1_o_context_list.append(o)
            
    return d_e_count,d_d_count,d_o_count

def from_keys_to_list(keys):
    out_list = []
    for key in keys:
        item = eval(key)
        out_list.append(item)
    return out_list

def compute_nb_pair_for_context_included(d_count):
    d_count_included = {} 
    l_all_context = from_keys_to_list(d_count)
    for current_context in l_all_context:
        nb_pair = d_count[str(current_context)]
        # compute upper context
        l_upper = compute_upper_context(current_context,l_all_context)
        for upper in l_upper:
            nb_pair += d_count[str(upper)]
        d_count_included[str(current_context)] = nb_pair

    return d_count_included

def compute_upper_context(context,all_context):
    upper = []
    s_context = set(context)
    for current_context in all_context:
        if context == current_context:
            continue
        # we do not want to collect upper context of []
        if context == []:
            continue
        s_current_context = set(current_context)
        if s_context.issubset(s_current_context):
            upper.append(current_context)
    return upper

def compute_pattern(nb_included_e,nb_included_d,nb_included_o):
    e_sorted = from_dict_to_sorted_list(nb_included_e)
    d_sorted = from_dict_to_sorted_list(nb_included_d)
    o_sorted = from_dict_to_sorted_list(nb_included_o)

    return [eval(e_sorted[0][0]),eval(d_sorted[0][0]),eval(o_sorted[0][0])]

def from_dict_to_sorted_list(d):
    l = []
    for key in d:
        l.append((key,d[key]))
    l.sort(key=lambda x: x[1])
    l.reverse()
    return l

def check_pattern_on_file(pattern,file):
    nb_item = 0
    nb_pattern_found = 0

    ep = pattern[0]
    dp = pattern[1]
    op = pattern[2]

    with open(file) as input_file:
        lines = input_file.readlines()
    for line in lines:
        nb_item += 1
        
        line_strip = line.strip()
        edo = eval(line_strip)
        e = edo[0]
        d = edo[1]
        o = edo[2]
         
        is_e_pattern_found = is_pattern_found(ep,e)
        is_d_pattern_found = is_pattern_found(dp,d)
        is_o_pattern_found = is_pattern_found(op,o)
        pattern_found = is_e_pattern_found and is_d_pattern_found and is_o_pattern_found
  
        if pattern_found:
            nb_pattern_found += 1
        else:
            #pass
            print(edo)

    return (nb_pattern_found/nb_item,nb_pattern_found,nb_item)



def check_patterns_on_file(patterns,file):
    nb_item = 0
    nb_pattern_found = 0

    with open(file) as input_file:
        lines = input_file.readlines()
    for line in lines:
        nb_item += 1
 
        line_strip = line.strip()
        edo = eval(line_strip)
        e = edo[0]
        d = edo[1]
        o = edo[2]

        for pattern in patterns:
            ep = pattern[0]
            dp = pattern[1]
            op = pattern[2]

            is_e_pattern_found = is_pattern_found(ep,e)
            is_d_pattern_found = is_pattern_found(dp,d)
            is_o_pattern_found = is_pattern_found(op,o)
            pattern_found = is_e_pattern_found and is_d_pattern_found and is_o_pattern_found
  
            if pattern_found:
                nb_pattern_found += 1
                break

    return (nb_pattern_found/nb_item,nb_pattern_found,nb_item)


def check_pattern_on_r_metrics(pattern,r_metrics):
    ep = pattern[0]
    dp = pattern[1]
    op = pattern[2]
    nb_item = 0
    nb_pattern_found = 0
    for key in r_metrics:
        edo_str = key.replace("][","],[")
        edo = eval("["+edo_str+"]")
        e = edo[0]
        d = edo[1]
        o = edo[2]
        
        is_e_pattern_found = is_pattern_found(ep,e)
        is_d_pattern_found = is_pattern_found(dp,d)
        is_o_pattern_found = is_pattern_found(op,o)
        pattern_found = is_e_pattern_found and is_d_pattern_found and is_o_pattern_found

        if pattern_found:
            nb_pattern_found += r_metrics[key]
        nb_item += r_metrics[key]

    return (nb_pattern_found/nb_item,nb_pattern_found,nb_item)
  
def check_patterns_on_r_metrics(patterns,r_metrics):
    nb_item = 0
    nb_pattern_found = 0
    for key in r_metrics:
        edo_str = key.replace("][","],[")
        edo = eval("["+edo_str+"]")
        e = edo[0]
        d = edo[1]
        o = edo[2]
        for pattern in patterns:
            ep = pattern[0]
            dp = pattern[1]
            op = pattern[2]
 
            is_e_pattern_found = is_pattern_found(ep,e)
            is_d_pattern_found = is_pattern_found(dp,d)
            is_o_pattern_found = is_pattern_found(op,o)
            pattern_found = is_e_pattern_found and is_d_pattern_found and is_o_pattern_found

            if pattern_found:
                nb_pattern_found += r_metrics[key]
                break
        nb_item += r_metrics[key]

    return (nb_pattern_found/nb_item,nb_pattern_found,nb_item)
  
# explicit pattern recognition
def is_pattern_found(pattern,context):
    found = False
    if pattern == [] and context == []:
        found = True
    elif pattern == [] and context != []:
        found = False
    elif pattern != [] and context == []:
        found = False
    elif pattern != [] and context != []:
        s_pattern = set(pattern)
        s_context = set(context)
        found = s_pattern.issubset(s_context)
    else:
        raise Exception("is_pattern_found unkown case")
    return found

def compute_pattern_dataset(common_list,dict_1,dict_2,extract_dict_func):
    for item in common_list:
        d_dict1_extracted = extract_dict_func(dict_1,item)
        d_dict2_extracted = extract_dict_func(dict_2,item)
        for id1 in d_dict1_extracted:
            for id2 in d_dict2_extracted:
                i1 = d_dict1_extracted[id1]
                i2 = d_dict2_extracted[id2]
                e,d,o = compute_edo_for_a_pair2(i1,i2,id1,id2)
                list_2_print = []
                list_2_print.append(e)
                list_2_print.append(d)
                list_2_print.append(o)
                print(list_2_print)
