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
    #actor = [0,1] 
    filename = "actor_empty"
    pie(title,actor,filename)
    
    title = "Actor {wasbornonyear} ns"
    actor = [1,291]
    #actor = [1/292,291/292]
    filename = "actor_wasbornonyear"
    pie(title,actor,filename)

    title = "Actor {diedonyear,wasbornonyear} ns"
    actor = [7,150]
    #actor = [7/157,150/157]
    filename = "actor_diedonyear_wasbornonyear"
    pie(title,actor,filename)

    title = "Actor {wasbornondate,wasbornonyear} ns"
    actor = [3,115]
    #actor = [3/118,115/118]
    filename = "actor_wasbornondate_wasbornonyear"
    pie(title,actor,filename)

    title = "Actor {actedin} ns"
    actor = [19,73]
    #actor = [19/92,73/92]
    filename = "actor_actedin"
    pie(title,actor,filename)

    title = "Actor {actedin,wasbornonyear} ws"
    actor = [49,19]
    #actor = [49/68,19/68]
    filename = "actor_actedin_wasbornonyear"
    pie(title,actor,filename)

    title = "Actor {wasbornin,wasbornondate,wasbornonyear} ws"
    actor = [48,28]
    #actor = [48/76,28/76]
    filename = "actor_wasbornin_wasbornondate_wasbornonyear"
    pie(title,actor,filename)

def album():
    title = "Album {skos:preflabel'} ws"
    album = [6598,2566]
    #album = [round((6598/9164)*100),round((2566/9164)*100)]
    filename = "album_preflabel"
    pie(title,album,filename)

    title = "Album {created-inv} ns"
    album = [0,8405]
    #album = [0,100]]
    filename = "album_created-inv"
    pie(title,album,filename)

    title = "Album {wascreatedondate,wascreatedonyear} ns"
    album = [0,6953]
    #album = [0,100]
    filename = "album_wascreatedondate_wascreatedonyear"
    pie(title,album,filename)

    title = "Album {} ns"
    album = [0,6807]
    #album = [0,100]
    filename = "album_empty"
    pie(title,album,filename)

    title = "Album {skos:preflabel'} ws"
    title = "Album {created-inv} ns"
    title = "Album {wascreatedondate,wascreatedonyear} ns"
    title = "Album {} ns"
    #[round((6598/9164)*100),0,0,0]
    #[round((2566/9164)*100),100,100,100]

def book():
    title = "Book empty ns"
    book = [0,1909]
    #book = [0,100]
    filename = "book_empty"
    pie(title,book,filename)

    title = "Book {created-inv,haspages} ws"
    book = [56,1688]
    #book = [round((56/1744)*100),round((1688/1744)*100)]
    filename = "book_created-inv_haspages"
    pie(title,book,filename)
    
    #title = "Book empty ns"
    #title = "Book {created-inv,haspages} ws"
    #book = [0,100]
    #book = [round((56/1744)*100),round((1688/1744)*100)]
    # [0,round((56/1744)*100)]
    # [100,round((1688/1744)*100)]
def film():
    title = "Film {wascreatedondate,wascreatedonyear} ns"
    film = [5,1900]
    # film = [round((5/1905)*100),round((1900/1905)*100)]
    filename = "film_wascreatedondate_wascreatedonyear"
    pie(title,film,filename)
   
    title = "Film {actedin-inv,created-inv,directed-inv,wrotemusicfor-inv} ws"
    film = [1002,432]
    #film = [round((1002/1434)*100),round((432/1434)*100)]
    filename = "film_actedin-inv_created-inv_directed-inv_wrotemusicfor-inv"
    pie(title,film,filename)

    title = "Film {actedin-inv,created-inv,directed-inv} ns"
    film = [177,1029]
    #film = [round((177/1206)*100),round((1029/1206)*100)]
    filename = "film_actedin-inv_created-inv_directed-inv"
    pie(title,film,filename)

    title = "Film {actedin-inv,directed-inv,wrotemusicfor-inv} ws"
    film = [698,198]
    #film = [round((698/896)*100),round((198/896)*100)]
    filename = "film_actedin-inv_directed-inv_wrotemusicfor-inv"
    pie(title,film,filename)

    title = "Film {actedin-inv,created-inv,directed-inv,edited-inv,wrotemusicfor-inv} ws"
    film = [650,172]
    #film = [round((650/822)*100),round((172/822)*100)]
    filename = "film_actedin-inv_created-inv_directed-inv_edited-inv_wrotemusicfor-inv"
    pie(title,film,filename)

    title = "Film {actedin-inv,directed-inv} ns"
    film = [54,668]
    #film = [round((54/722)*100),round((668/722)*100)]
    filename = "film_actedin-inv_directed-inv"
    pie(title,film,filename)

    title = "Film {actedin-inv,directed-inv,edited-inv,wrotemusicfor-inv} ws"
    film = [535,146]
    #film = [round((535/681)*100),round((146/681)*100)]
    filename = "film_actedin-inv_directed-inv_edited-inv_wrotemusicfor-inv"
    pie(title,film,filename)
    
    title = "Film {wascreatedonyear} ns"
    #film = [0,508]
    film = [0,100]
    filename = "film_wascreatedonyear"
    pie(title,film,filename)

    title = "Film {wascreatedondate,wascreatedonyear} ns"
    # film = [round((5/1905)*100),round((1900/1905)*100)]
 
    title = "Film {actedin-inv,created-inv,directed-inv,wrotemusicfor-inv} ws"
    #film = [round((1002/1434)*100),round((432/1434)*100)]
 
    title = "Film {actedin-inv,created-inv,directed-inv} ns"
    #film = [round((177/1206)*100),round((1029/1206)*100)]

    title = "Film {actedin-inv,directed-inv,wrotemusicfor-inv} ws"
    #film = [round((698/896)*100),round((198/896)*100)]
     
    title = "Film {actedin-inv,created-inv,directed-inv,edited-inv,wrotemusicfor-inv} ws"
    film = [round((650/822)*100),round((172/822)*100)]
 
    title = "Film {actedin-inv,directed-inv} ns"
    #film = [round((54/722)*100),round((668/722)*100)]
 
    title = "Film {actedin-inv,directed-inv,edited-inv,wrotemusicfor-inv} ws"
    #film = [round((535/681)*100),round((146/681)*100)]

    title = "Film {wascreatedonyear} ns"
    #film = [0,100]
 
    title = "Film {wascreatedondate,wascreatedonyear} ns"
    title = "Film {actedin-inv,created-inv,directed-inv,wrotemusicfor-inv} ws"
    title = "Film {actedin-inv,created-inv,directed-inv} ns"
    title = "Film {actedin-inv,directed-inv,wrotemusicfor-inv} ws"
    title = "Film {actedin-inv,created-inv,directed-inv,edited-inv,wrotemusicfor-inv} ws"
    title = "Film {actedin-inv,directed-inv} ns"
    title = "Film {actedin-inv,directed-inv,edited-inv,wrotemusicfor-inv} ws"
    title = "Film {wascreatedonyear} ns"
    [round((5/1905)*100),round((1002/1434)*100),round((177/1206)*100),round((698/896)*100),round((650/822)*100),round((54/722)*100),round((535/681)*100),0]
    [round((1900/1905)*100),round((432/1434)*100),round((1029/1206)*100),round((198/896)*100),,round((172/822)*100),round((668/722)*100),round((146/681)*100),100]

def mountain():
    title= "Moutain {islocatedin} ns"
    mountain = [0,2388]
    filename = "moutain_islocatedin"
    pie(title,mountain,filename)

def university():
    title = "University empty ns "
    university = [0,2388]
    #university = [0,100]
    filename = "university_empty"
    pie(title,university,filename)

    title = "University {graduatedfrom-inv} ns"
    university = [175,666]
    university = [round((175/841)*100),round((666/841)*100)]
    filename = "university_graduatedfrom-inv"
    pie(title,university,filename)

    title = "University {islocatedin} ns"
    university = [1,569]
    #university = [round((1/570)*100),round((569/570)*100)]
    filename = "university_islocatedin"
    pie(title,university,filename)

    title = "University {graduatedfrom-inv,islocatedin} ns"
    university = [27,124]
    #university = [round((27/151)*100),round((124/151)*100)]
    filename = "university_graduatedfrom-inv_islocatedin"
    pie(title,university,filename)


    title = "University empty ns "
    title = "University {graduatedfrom-inv} ns"
    title = "University {islocatedin} ns"
    title = "University {graduatedfrom-inv,islocatedin} ns"
    #university = [0,100]
    #university = [round((175/841)*100),round((666/841)*100)]
    #university = [round((1/570)*100),round((569/570)*100)]
    #university = [round((27/151)*100),round((124/151)*100)]
    #[0,[round((175/841)*100),round((1/570)*100),round((27/151)*100)]
    #[100,round((666/841)*100),round((569/570)*100),round((124/151)*100)]
if __name__ == "__main__":
    #actor()
    #album()
    #book()
    #film()
    #mountain()
    #university()

