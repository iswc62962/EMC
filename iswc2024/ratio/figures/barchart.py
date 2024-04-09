import matplotlib.pyplot as plt
import numpy as np

def plot_table_4():
    classes = ("Book", "Actor", "City", "Mountain", "University")
    quantitication_counts = {
            "Genuine Incomp" : np.array([6285,473,1550,3172,1489]),
            "Genuine Conflicts": np.array([1990,2014,7325,1477,3333]),
            "GI X GC" : np.array([1587,496,3656,7344,1325]) 
            }
    width = 0.6  # the width of the bars: can also be len(x) sequence


    fig, ax = plt.subplots()
    bottom = np.zeros(5)

    for quantification, quantitication_count in quantitication_counts.items():
        p = ax.bar(classes, quantitication_count, width, label=quantification, bottom=bottom)
        bottom += quantitication_count
        ax.bar_label(p, label_type='center')

        #ax.set_title('if it works ...')
        ax.legend()

    #plt.show()
    plt.savefig("./table_4.pdf", format="pdf")

def plot_actor():

    #title = "Actor {} ns"
    #title = "Actor {wasbornonyear} ns"
    #title = "Actor {diedonyear,wasbornonyear} ns"
    #title = "Actor {wasbornondate,wasbornonyear} ns"
    #title = "Actor {actedin} ns"
    #title = "Actor {actedin,wasbornonyear} ws"
    #title = "Actor {wasbornin,wasbornondate,wasbornonyear} ws"
    
    #classes = ("e1 ns", "e2 ns", "e3 ns","e4 ns","e5 ns", "e6 ws","e7 ws")
    classes = ("e1 NIC", "e2 NIC", "e3 NIC","e4 NIC","e5 NIC", "e6 WIC","e7 WIC")
    quantitication_counts = {
            #"Specific EMCs" : np.array([0,1,7,3,19,73,48]),
            "Representative EMCs" : np.array([0,round((1/292)*100),round((7/157)*100),round((3/118)*100),round((19/92)*100),round((49/68)*100),round((48/76)*100)]),
            #"No Specific EMCs" : np.array([927,291,150,115,73,19,28])
            "No Representative EMCs" : np.array([100,round((291/292)*100),round((150/157)*100),round((115/118)*100),round((73/92)*100),round((19/68)*100),round((28/76)*100)])
            }

    width = 0.6  # the width of the bars: can also be len(x) sequence
    fig, ax = plt.subplots()
    bottom = np.zeros(7)

    for quantification, quantitication_count in quantitication_counts.items():
        p = ax.bar(classes, quantitication_count, width, label=quantification, bottom=bottom)
        bottom += quantitication_count
        ax.bar_label(p, label_type='center')

        ax.set_title('Actor')
        ax.legend()

    #plt.show()
    plt.savefig("./actor_chart.pdf", format="pdf")


def plot_album():
    #title = "Album {skos:preflabel'} ws"
    #title = "Album {created-inv} ns"
    #title = "Album {wascreatedondate,wascreatedonyear} ns"
    #title = "Album {} ns"
 
    #classes = ("e1 ws", "e2 ns", "e3 ns","e4 ns")
    classes = ("e1 wr", "e2 nr", "e3 nr","e4 nr")
    quantitication_counts = {
            #"Specific EMCs" : np.array([round((6598/9164)*100),0,0,0]),
            "Representative EMCs" : np.array([round((6598/9164)*100),0,0,0]),
            #"No Specific EMCs" : np.array([round((2566/9164)*100),100,100,100])
            "No Representative EMCs" : np.array([round((2566/9164)*100),100,100,100])
            }

    width = 0.6  # the width of the bars: can also be len(x) sequence
    fig, ax = plt.subplots()
    bottom = np.zeros(4)

    for quantification, quantitication_count in quantitication_counts.items():
        p = ax.bar(classes, quantitication_count, width, label=quantification, bottom=bottom)
        bottom += quantitication_count
        ax.bar_label(p, label_type='center')

        ax.set_title('Album')
        ax.legend()

    #plt.show()
    plt.savefig("./album_chart.pdf", format="pdf")

def plot_book():
    #title = "Book empty ns"
    #title = "Book {created-inv,haspages} ws"
    # [0,round((56/1744)*100)]
    # [100,round((1688/1744)*100)]


    #classes = ("e1 ns", "e2 ws")
    classes = ("e1 nr", "e2 wr")
    quantitication_counts = {
            #"Specific EMCs" : np.array([0,round((56/1744)*100)]),
            "Representative EMCs" : np.array([0,round((56/1744)*100)]),
            #"No Specific EMCs" : np.array([100,round((1688/1744)*100)])
            "No Representative EMCs" : np.array([100,round((1688/1744)*100)])
            }

    width = 0.6  # the width of the bars: can also be len(x) sequence
    fig, ax = plt.subplots()
    bottom = np.zeros(2)
    for quantification, quantitication_count in quantitication_counts.items():
        p = ax.bar(classes, quantitication_count, width, label=quantification, bottom=bottom)
        bottom += quantitication_count
        ax.bar_label(p, label_type='center')

        ax.set_title('Book')
        #ax.legend()

    #plt.show()
    #plt.figure(figsize=(6, 4))
    plt.savefig("./book_chart.pdf", format="pdf")


def plot_album_book():
    #title = "Album {skos:preflabel'} ws"
    #title = "Album {created-inv} ns"
    #title = "Album {wascreatedondate,wascreatedonyear} ns"
    #title = "Album {} ns"
    
    #title = "Book empty ns"
    #title = "Book {created-inv,haspages} ws"
    # [0,round((56/1744)*100)]
    # [100,round((1688/1744)*100)]


    #classes = ("e1 ws", "e2 ns", "e3 ns","e4 ns")
    classes = ("Ue1 WIC", "Ue2 NIC", "Ue3 NIC","Ue4 NIC"," ","Be1 NIC","Be2 WIC")
    quantitication_counts = {
            #"Specific EMCs" : np.array([round((6598/9164)*100),0,0,0]),
            "Representative EMCs" : np.array([round((6598/9164)*100),0,0,0,0,0,round((56/1744)*100)]),
            #"No Specific EMCs" : np.array([round((2566/9164)*100),100,100,100])
            "No Representative EMCs" : np.array([round((2566/9164)*100),100,100,100,0,100,round((1688/1744)*100)])
            }
    width = 0.6  # the width of the bars: can also be len(x) sequence
    fig, ax = plt.subplots()
    bottom = np.zeros(7)
    for quantification, quantitication_count in quantitication_counts.items():
        p = ax.bar(classes, quantitication_count, width, label=quantification, bottom=bottom)
        bottom += quantitication_count
        ax.bar_label(p, label_type='center')

        ax.set_title('Album                                                     Book')
        ax.legend()

    #plt.show()
    plt.savefig("./album_book_chart.pdf", format="pdf")


def plot_film():
    titel = "Film {}"
    title = "Film {wascreatedondate,wascreatedonyear} ns"
    title = "Film {actedin-inv,created-inv,directed-inv,wrotemusicfor-inv} ws"
    title = "Film {actedin-inv,created-inv,directed-inv} ns"
    title = "Film {actedin-inv,directed-inv,wrotemusicfor-inv} ws"
    title = "Film {actedin-inv,created-inv,directed-inv,edited-inv,wrotemusicfor-inv} ws"
    title = "Film {actedin-inv,directed-inv} ns"
    title = "Film {actedin-inv,directed-inv,edited-inv,wrotemusicfor-inv} ws"
    title = "Film {wascreatedonyear} ns"
    #[0,round((5/1905)*100),round((1002/1434)*100),round((177/1206)*100),round((698/896)*100),round((650/822)*100),round((54/722)*100),round((535/681)*100),0]
    #[100,round((1900/1905)*100),round((432/1434)*100),round((1029/1206)*100),round((198/896)*100),,round((172/822)*100),round((668/722)*100),round((146/681)*100),100]

    #classes = ("e1 ns","e2 ns", "e3 ws","e4 ns","e5 ws","e6 ws","e7 ns","e8 ws","e9 ns")
    classes = ("e1 NIC","e2 NIC", "e3 WIC","e4 NIC","e5 WIC","e6 WIC","e7 NIC","e8 WIC","e9 NIC")
    quantitication_counts = {
            #"Specific EMCs" : np.array([0,round((5/1905)*100),round((1002/1434)*100),round((177/1206)*100),round((698/896)*100),round((650/822)*100),round((54/722)*100),round((535/681)*100),0]),
            "Representative EMCs" : np.array([0,round((5/1905)*100),round((1002/1434)*100),round((177/1206)*100),round((698/896)*100),round((650/822)*100),round((54/722)*100),round((535/681)*100),0]),
            #"No Specific EMCs" : np.array([100,round((1900/1905)*100),round((432/1434)*100),round((1029/1206)*100),round((198/896)*100),round((172/822)*100),round((668/722)*100),round((146/681)*100),100])
            "No Representative EMCs" : np.array([100,round((1900/1905)*100),round((432/1434)*100),round((1029/1206)*100),round((198/896)*100),round((172/822)*100),round((668/722)*100),round((146/681)*100),100])
            }

    width = 0.6  # the width of the bars: can also be len(x) sequence
    fig, ax = plt.subplots()
    bottom = np.zeros(9)

    for quantification, quantitication_count in quantitication_counts.items():
        p = ax.bar(classes, quantitication_count, width, label=quantification, bottom=bottom)
        bottom += quantitication_count
        ax.bar_label(p, label_type='center')

        ax.set_title('Film')
        ax.legend()

    #plt.show()
    plt.savefig("./film_chart.pdf", format="pdf")

def plot_mountain():
    title= "Moutain {islocatedin} ns"
    #classes = ("e1 ns")
    classes = ("e1 nr")
    quantitication_counts = {
            #"Specific EMCs" : np.array(0),
            "Representative EMCs" : np.array([0]),
            #"No Specific EMCs" : np.array(100)
            "No Representative EMCs" : np.array([100])
            }

    width = 0.2  # the width of the bars: can also be len(x) sequence
    fig, ax = plt.subplots()
    bottom = np.zeros(1)

    for quantification, quantitication_count in quantitication_counts.items():
        p = ax.bar(classes, quantitication_count, width, label=quantification, bottom=bottom)
        bottom += quantitication_count
        ax.bar_label(p, label_type='center')

        ax.set_title('Mountain')
        ax.legend()

    #plt.show()
    plt.savefig("./mountain_chart.pdf", format="pdf")

def plot_university():
    title = "University empty ns "
    title = "University {graduatedfrom-inv} ns"
    title = "University {islocatedin} ns"
    title = "University {graduatedfrom-inv,islocatedin} ns"
    #[0,[round((175/841)*100),round((1/570)*100),round((27/151)*100)]
    #[100,round((666/841)*100),round((569/570)*100),round((124/151)*100)]


    #classes = ("e1 ns","e2 ns","e3 ns","e4 ns")
    classes = ("e1 nr","e2 nr","e3 nr","e4 nr")
    quantitication_counts = {
            #"Specific EMCs" : np.array([0,round((175/841)*100),round((1/570)*100),round((27/151)*100)]),
            "Representative EMCs" : np.array([0,round((175/841)*100),round((1/570)*100),round((27/151)*100)]),
            #"No Specific EMCs" : np.array([100,round((666/841)*100),round((569/570)*100),round((124/151)*100)])
            "No Representative EMCs" : np.array([100,round((666/841)*100),round((569/570)*100),round((124/151)*100)])
            }

    width = 0.6  # the width of the bars: can also be len(x) sequence
    fig, ax = plt.subplots()
    bottom = np.zeros(4)

    for quantification, quantitication_count in quantitication_counts.items():
        p = ax.bar(classes, quantitication_count, width, label=quantification, bottom=bottom)
        bottom += quantitication_count
        ax.bar_label(p, label_type='center')

        ax.set_title('University')
        ax.legend()

    #plt.show()
    plt.savefig("./university_chart.pdf", format="pdf")


def plot_university_mountain():
    title = "University empty ns "
    title = "University {graduatedfrom-inv} ns"
    title = "University {islocatedin} ns"
    title = "University {graduatedfrom-inv,islocatedin} ns"
    #[0,[round((175/841)*100),round((1/570)*100),round((27/151)*100)]
    #[100,round((666/841)*100),round((569/570)*100),round((124/151)*100)]
    #classes = ("e1 ns","e2 ns","e3 ns","e4 ns")
    classes = ("Ue1 NIC","Ue2 NIC","Ue3 NIC","Ue4 NIC"," ","Me1 NIC")
    quantitication_counts = {
            #"Specific EMCs" : np.array([0,round((175/841)*100),round((1/570)*100),round((27/151)*100)]),
            "Representative EMCs" : np.array([0,round((175/841)*100),round((1/570)*100),round((27/151)*100),0,0]),
            #"No Specific EMCs" : np.array([100,round((666/841)*100),round((569/570)*100),round((124/151)*100)])
            "No Representative EMCs" : np.array([100,round((666/841)*100),round((569/570)*100),round((124/151)*100),0,100])
            }

    width = 0.6  # the width of the bars: can also be len(x) sequence
    fig, ax = plt.subplots()
    bottom = np.zeros(6)

    for quantification, quantitication_count in quantitication_counts.items():
        p = ax.bar(classes, quantitication_count, width, label=quantification, bottom=bottom)
        bottom += quantitication_count
        ax.bar_label(p, label_type='center')
        ax.set_title('University                                            Mountain')
        ax.legend()
    #plt.show()
    plt.savefig("./university_mountain_chart.pdf", format="pdf")

if __name__ == "__main__":
    plot_actor()
    #plot_album()
    #plot_book()
    plot_film()
    #plot_mountain()
    #plot_university()
    plot_album_book()
    plot_university_mountain()
