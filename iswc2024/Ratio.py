def compute_r_metrics_for_all_epsilon(r_metrics):
    r_metrics_e = {}
    for key in r_metrics:
        edo_str = key.replace("][","],[")
        edo = eval("["+edo_str+"]")
        e = edo[0]
        e_str = str(e)
        if e_str not in r_metrics_e:
            r_metrics_e[e_str] = 0
        r_metrics_e[e_str] += r_metrics[key]
    return r_metrics_e

def rank_r_metrics_epsilon(r_metrics):
    l_metrics = []
    for key in r_metrics:
        l_metrics.append((key,r_metrics[key]))
    s = sorted(l_metrics, key=lambda x: x[1]) 
    s.reverse()
    return(s)


def compute_sameas_ratio_rank(sameas_rme_ranked,r_metrics_epsilon):
    sameas_ratio = {}
    print("context" + "\t" + "nb same as" + "\t" + "nb all pair" + "\t" + "nb same as \ nb all pair")
    for str_e,nb_sameas in sameas_rme_ranked:
        ratio = nb_sameas / (r_metrics_epsilon[str_e])
        print(str(str_e) + "\t" + str(nb_sameas) + "\t" + str(r_metrics_epsilon[str_e]) + "\t" + str(ratio))
        #print()
        #print(str_e)
        #print(nb_sameas)
        #print(r_metrics_epsilon[str_e])
        #print(ratio)

def compute_sameas_ratio(sameas_r_metrics,r_metrics,initial_ratio,all_sameas_assert,epsilon):
    ratios_above_cutoff = []
    cutoff_ratio = 0.8
    nb_sameas_above_cutoff = 0
    all_same_as = 0
    # print detail
    #print("context" + "\t" +"nb sameas" + "\t" + "all_pair" + "\t" + "ratio")
    #print("context" + " & " +"nb sameas" + " & " + "all_pair" + " & " + "ratio" + "\\")
    for key in sameas_r_metrics:
        nb_sameas = sameas_r_metrics[key]
        ratio = nb_sameas/r_metrics[key]
        all_same_as += nb_sameas
        if ratio >= cutoff_ratio:
            ratios_above_cutoff.append(ratio)
            nb_sameas_above_cutoff += nb_sameas
        
        # print detail
        #print (str(key) + "\t" + str(nb_sameas) + "\t" + str(r_metrics[key]) + "\t" + str(ratio))
        #print (str(key) + " & " + str(nb_sameas) + " & " + str(r_metrics[key]) + " & " + str(ratio) + "\\")

    assert(all_same_as == all_sameas_assert)

    mean_sameas_above_cutoff = "zero division"
    if len(ratios_above_cutoff) != 0:
        mean_sameas_above_cutoff = sum(ratios_above_cutoff)/len(ratios_above_cutoff)
    # comment these lines if detail is uncommented
    #print(str(epsilon) + "\t" + str(initial_ratio) + "\t" + str(nb_sameas_above_cutoff) + "\t" + str(all_same_as) + "\t" + str(nb_sameas_above_cutoff/all_same_as))
    print(str(epsilon) + "\t" + str(initial_ratio) + "\t" + str(nb_sameas_above_cutoff) + "\t" + str(all_same_as) + "\t" + str(nb_sameas_above_cutoff/all_same_as) + "\t" + str(mean_sameas_above_cutoff))

def pareto(nb_pair_total,r_metrics_ranked):
    r_metrics_pareto = []
    nb_pair_80 = nb_pair_total * 0.8
    nb_sum = 0
    for item in r_metrics_ranked:
        nb_sum += item[1]
        r_metrics_pareto.append(item)
        if nb_sum >= nb_pair_80:
            break
    return r_metrics_pareto 

def compute_r_metrics_for_one_epsilon(r_metrics,epsilon):
    r_metrics_wasboronyear = {}
    nb_val = 0
    for key in r_metrics:
        edo_str = key.replace("][","],[")
        edo = eval("["+edo_str+"]")
        e = edo[0]
        if e == epsilon:
            r_metrics_wasboronyear[key] = r_metrics[key]
            nb_val += r_metrics[key]
    return r_metrics_wasboronyear


