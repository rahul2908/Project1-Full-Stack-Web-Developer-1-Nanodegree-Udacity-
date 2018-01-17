import movie
import fresh_tomatoes

"""In this file all the details for the movies are used. """

dangal = movie.Films("Dangal", "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg", "https://www.youtube.com/watch?v=x_7YlGv9u1g&t=7s", "2 Hours 49 Minutes")
toilet = movie.Films("Toilet - Ek Prem Katha", "https://upload.wikimedia.org/wikipedia/en/1/12/Toilet_Ek_Prem_Katha.jpg", "https://www.youtube.com/watch?v=ym4EJQ7XORk", "2 Hours 35 Minutes")
raess = movie.Films("Raess", "https://upload.wikimedia.org/wikipedia/en/2/2b/Raees_Poster.jpg", "https://www.youtube.com/watch?v=J7_1MU3gDk0", "2 Hours 41 Minutes")
ms_dhoni = movie.Films("M.S Dhoni", "https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg", "https://www.youtube.com/watch?v=6L6XqWoS8tw", "3 Hours 40 Minutes")
sultan = movie.Films("Sultan", "https://upload.wikimedia.org/wikipedia/en/1/1f/Sultan_film_poster.jpg", "https://www.youtube.com/watch?v=wPxqcq6Byq0&t=2s", "2 Hours 50 Minutes")
padmavati = movie.Films("Padmavati", "https://upload.wikimedia.org/wikipedia/en/7/73/Padmaavat_poster.jpg", "https://www.youtube.com/watch?v=8YaF2m7hCx0", "2 Hours 40 Minutes")
singham = movie.Films("Singham", "https://upload.wikimedia.org/wikipedia/en/a/ac/Singham_%282011_Hindi_film%29_Theatrical_poster.jpg", "https://www.youtube.com/watch?v=mp-XqCrCi6I", "2 Hours 23 Minutes")
tiger_zinda_hai = movie.Films("Tiger Zinda Hai", "https://upload.wikimedia.org/wikipedia/en/5/5e/Tiger_Zinda_Hai_-_Poster.jpg", "https://www.youtube.com/watch?v=ePO5M5DE01I", "2 Hours 45 Minutes")
drishyam = movie.Films("Drishyam", "https://upload.wikimedia.org/wikipedia/en/8/8a/Drishyam_2015_film.jpg", "https://www.youtube.com/watch?v=AuuX2j14NBg", "2 Hours 43 Minutes")
movies = [dangal,toilet,raess,ms_dhoni,sultan,padmavati,singham,tiger_zinda_hai,drishyam]

fresh_tomatoes.open_movies_page(movies)
