import matplotlib.pyplot as plt



def pie(title,values,filename):
    labels = 'specific combination', 'unspecific combination'

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.savefig("./"+filename+".pdf", format="pdf")


def actor():
    title = "Actor {} ns"
    actor = [0,927]
    filename = "actor_empty"
    pie(title,actor,filename)
    
    title = "Actor {wasbornonyear} ns"
    actor = [1,291]
    filename = "actor_wasbornonyear"
    pie(title,actor,filename)

    title = "Actor {diedonyear,wasbornonyear} ns"
    actor = [7,150]
    filename = "actor_diedonyear_wasbornonyear"
    pie(title,actor,filename)

    title = "Actor {wasbornondate,wasbornonyear} ns"
    actor = [3,115]
    filename = "actor_wasbornondate_wasbornonyear"
    pie(title,actor,filename)

    title = "Actor {actedin} ns"
    actor = [19,73]
    filename = "actor_actedin"
    pie(title,actor,filename)

    title = "Actor {actedin,wasbornonyear} ws"
    actor = [49,19]
    filename = "actor_actedin_wasbornonyear"
    pie(title,actor,filename)

    title = "Actor {wasbornin,wasbornondate,wasbornonyear} ws"
    actor = [48,28]
    filename = "actor_wasbornin_wasbornondate_wasbornonyear"
    pie(title,actor,filename)

def album():
    title = "Album {skos:preflabel'} ws"
    album = [6598,2566]
    filename = "album_preflabel"
    pie(title,album,filename)

    title = "Album {created-inv} ns"
    album = [0,8405]
    filename = "album_created-inv"
    pie(title,album,filename)

    title = "Album {wascreatedondate,wascreatedonyear} ns"
    album = [0,6953]
    filename = "album_wascreatedondate_wascreatedonyear"
    pie(title,album,filename)

    title = "Album {} ns"
    album = [0,6807]
    filename = "album_empty"
    pie(title,album,filename)

def book():
    title = "Book empty ns"
    book = [0,1909]
    filename = "book_empty"
    pie(title,book,filename)

    title = "Book {created-inv,haspages} ws"
    book = [56,1688]
    filename = "book_created-inv_haspages"
    pie(title,book,filename)

def film():
    title = "Film {wascreatedondate,wascreatedonyear} ns"
    film = [5,1900]
    filename = "film_wascreatedondate_wascreatedonyear"
    pie(title,film,filename)
   
    title = "Film {actedin-inv,created-inv,directed-inv,wrotemusicfor-inv} ws"
    film = [1002,432]
    filename = "film_actedin-inv_created-inv_directed-inv_wrotemusicfor-inv"
    pie(title,film,filename)

    title = "Film {actedin-inv,created-inv,directed-inv} ns"
    film = [177,1029]
    filename = "film_actedin-inv_created-inv_directed-inv"
    pie(title,film,filename)

    title = "Film {actedin-inv,directed-inv,wrotemusicfor-inv} ws"
    film = [698,198]
    filename = "film_actedin-inv_directed-inv_wrotemusicfor-inv"
    pie(title,film,filename)

    title = "Film {actedin-inv,created-inv,directed-inv,edited-inv,wrotemusicfor-inv} ws"
    film = [650,172]
    filename = "film_actedin-inv_created-inv_directed-inv_edited-inv_wrotemusicfor-inv"
    pie(title,film,filename)

    title = "Film {actedin-inv,directed-inv} ns"
    film = [54,668]
    filename = "film_actedin-inv_directed-inv"
    pie(title,film,filename)

    title = "Film {actedin-inv,directed-inv,edited-inv,wrotemusicfor-inv} ws"
    film = [535,146]
    filename = "film_actedin-inv_directed-inv_edited-inv_wrotemusicfor-inv"
    pie(title,film,filename)
    
    title = "Film {wascreatedonyear} ns"
    film = [0,508]
    filename = "film_wascreatedonyear"
    pie(title,film,filename)

def mountain():
    title= "Moutain {islocatedin} ns"
    mountain = [0,2388]
    filename = "moutain_islocatedin"
    pie(title,mountain,filename)

def university():
    title = "University empty ns "
    university = [0,2388]
    filename = "university_empty"
    pie(title,university,filename)

    title = "University {graduatedfrom-inv} ns"
    university = [175,666]
    filename = "university_graduatedfrom-inv"
    pie(title,university,filename)

    title = "University {islocatedin} ns"
    university = [1,569]
    filename = "university_islocatedin"
    pie(title,university,filename)

    title = "University {graduatedfrom-inv,islocatedin} ns"
    university = [27,124]
    filename = "university_graduatedfrom-inv_islocatedin"
    pie(title,university,filename)

if __name__ == "__main__":
    actor()
    album()
    book()
    film()
    moutain()
    university()

