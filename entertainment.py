import media
import fresh_tomatoes

doug = media.Movie("Doug's 1st Movie","Doug and his pal Skeeter set's out to find the monster of Lucky Duck Lake. Though things get really out of hand when some one blurts out that the monster is real.","http://ia.media-imdb.com/images/M/MV5BMjA5MTk1OTA1NV5BMl5BanBnXkFtZTYwNDU4NjM5._V1__SX1303_SY591_.jpg","https://www.youtube.com/watch?v=oiQDNUF_gv4",1999,77)
spinal_tap = media.Movie("This is Spinal Tap","Spinal Tap, one of England's loudest bands, is chronicled by film director Marty DeBergi on what proves to be a fateful tour.","http://ia.media-imdb.com/images/M/MV5BMTQ2MTIzMzg5Nl5BMl5BanBnXkFtZTgwOTc5NDI1MDE@._V1__SX1303_SY591_.jpg","https://www.youtube.com/watch?v=N63XSUpe-0o",1984,82)
spaceballs = media.Movie("Spaceballs","President Skroob sends Lord Dark Helmet to steal Planet Druidia's abundant supply of air to replenish their own, and only Lone Starr can stop them.","http://ia.media-imdb.com/images/M/MV5BMTM3Mzg0Mzc2NF5BMl5BanBnXkFtZTcwNDEwNTk0NA@@._V1__SX1303_SY591_.jpg","https://www.youtube.com/watch?v=0uzEgsHypgM",1987,96)
harold_maude = media.Movie("Harold and Maude","Young, rich, and obsessed with death, Harold finds himself changed forever when he meets lively septuagenarian Maude at a funeral.","http://ia.media-imdb.com/images/M/MV5BMTUxMjMwODMxMl5BMl5BanBnXkFtZTYwMDA3MDE5._V1__SX1303_SY591_.jpg","https://www.youtube.com/watch?v=5mz3TkxJhPc",1971,91)
empire_strikes_back = media.Movie("The Empire Strikes Back","After the rebels have been brutally overpowered by the Empire on their newly established base, Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by Darth Vader as part of his plan to capture Luke.","http://ia.media-imdb.com/images/M/MV5BMjE2MzQwMTgxN15BMl5BanBnXkFtZTcwMDQzNjk2OQ@@._V1__SX1303_SY591_.jpg","https://www.youtube.com/watch?v=96v4XraJEPI",1980,124)
back_to_school = media.Movie("Back to School","To help his discouraged son get through college, a funloving and obnoxious rich businessman decides to enter the school as a student himself.","http://ia.media-imdb.com/images/M/MV5BMTYxMTIyOTM1MF5BMl5BanBnXkFtZTcwNzQ0MTcyNA@@._V1__SX1303_SY591_.jpg","https://www.youtube.com/watch?v=iRpUAdI_F_o",1986,96)

movies = [spinal_tap,doug,spaceballs,harold_maude,empire_strikes_back,back_to_school]
fresh_tomatoes.open_movies_page(movies)
