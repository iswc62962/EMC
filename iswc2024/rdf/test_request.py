import rdflib

# List all emc with property haslongitude in delta and islocatedin in omega
def list_emc_with_prop(g):
    query ="""
    SELECT  ?x ?emc ?y
    WHERE {
        ?emc a ns1:EMC .
        ?emc ns1:epsilon  ?epsilon .
        ?emc ns1:delta  ?delta .
        ?emc ns1:omega  ?omega .

        ?epsilon ns1:includes ns1:islocatedin .
        #?epsilon ns1:size 1 .

        ?delta ns1:includes ns2:preflabel .
        ?delta ns1:includes ns1:wascreatedonyear .
        #?delta ns1:size 2 .

        ?omega ns1:includes ns1:haslatitude .
        ?omega ns1:includes ns1:haslongitude .
        ?omega ns1:includes ns1:wascreatedondate .
        #?omega ns1:size 3 .
        }
    """
    qres = g.query(query)
    for r in qres:
        print(r)

# identity context of the pair louvre-lens-yago and jean-cocteau-musueum-db 
def test_pair_with_prop(g):
    query ="""
    SELECT ?eprop ?dprop ?oprop
    WHERE {
        <appalachian_trail_museum_yago> ?p <museum_of_the_american_revolution_db> .
        ?p a ns1:EMC .

        ?p ns1:epsilon ?e .
        ?p ns1:delta ?d .
        ?p ns1:omega ?o .

        ?e ns1:includes ?eprop .
        ?d ns1:includes ?dprop .
        ?o ns1:includes ?oprop .
        }
    """

    qres = g.query(query)
    for r in qres:
        print(r)

def test_count_pair_with_a_given_edo(g):
    query ="""
    SELECT  ?p (COUNT(?p) AS ?pTotal)
    WHERE {
        ?i1 ?p ?i2 .
        ?p a ns1:EMC .

        ?p ns1:epsilon ?e .
        ?p ns1:delta ?d .
        ?p ns1:omega ?o .

        ?e ns1:includes ns1:islocatedin .
        ?e ns1:size 1 .

        ?d ns1:includes ns1:islocatedin .
        ?d ns1:includes ns2:preflabel .
        ?d ns1:size 2 .

        ?o ns1:includes ns1:wascreatedonyar .
        ?o ns1:size 4 .

    }
    """
    qres = g.query(query)
    for r in qres:
        print(r)





if __name__ == "__main__":
    g = rdflib.Graph()
    g.parse("museum_emc.ttl")
 
    list_emc_with_prop(g)
    #test_pair_with_prop(g)
