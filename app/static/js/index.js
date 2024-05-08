
let movies;
let default_list;
let current_list = [];
let order = true;

function process_movies(movies) {
    const showMoviesDiv = document.getElementById('showMovies');
    showMoviesDiv.innerHTML = '';
    let id = 0;

    for (let movie of movies) {
        id = ++id;

        showMoviesDiv.innerHTML += `<tr>
        <td id="index-td-id" >${id}</td>
        <td id="index-td-movie" >${movie.movie}</td>
        <td id="index_td_tv" >labels</td>
        <td id="index-td-label" >${movie.year}</td>
        <td id="index-td-year" >${movie.series ? "✓" : "-"}</td>
        <td id="index-td-dropdown">
            <div class="dropdown">
                <button>•••</button>
                <div class="dropdown-content">
                    <form action="/update" method="GET">
                        <a href="/edit/${movie.index}">Edit </a>
                        <input id="update-watched" type="checkbox" name="watched" value="true" ${movie.watched ? "checked" : ''} />
                        Watched
                        <br />
                        <input id="update-downloaded" type="checkbox" name="downloaded" value="true" ${movie.downloaded ? "checked" : ''} />
                        Downloaded
                        <br />
                        <button id="update-submit" type="submit" name="index" value="${movie.index}" >Done</button>
                    </form>
                </div>
            </div>
        </td>
    </tr>`;
    }
    current_list = movies;
}

// function watched_downloaded() {

//     const downloaded = document.getElementById('downloaded');
//     const watched = document.getElementById('watched');
//     const download_checked = downloaded.checked;
//     const watch_checked = watched.checked;
//     let new_movie_list = [];

//     if (watch_checked && download_checked) {
//         for (let movie of movies) {
//             if (movie.watched && movie.downloaded) {
//                 new_movie_list.push(movie);
//                 process_movies(new_movie_list);

//             }
//         }
//     } else if (watch_checked) {
//         for (let movie of movies) {
//             if (movie.watched) {
//                 new_movie_list.push(movie);
//                 process_movies(new_movie_list);
//             }
//         }
//     } else if (download_checked) {
//         for (let movie of movies) {
//             if (movie.downloaded) {
//                 new_movie_list.push(movie);
//                 process_movies(new_movie_list);
//             }
//         }
//     } else {
//         process_movies(default_list);
//     }
// }

function checkbox_all() {
    if (document.getElementById("all").checked) {
        document.getElementById("watched").disabled = true;
        document.getElementById("downloaded").disabled = true;

        process_movies(movies);

    } else {
        document.getElementById("watched").disabled = false;
        document.getElementById("downloaded").disabled = false;
        watched_downloaded();
    }
}

fetch("/movies")
    .then((response) => response.json())
    .then((data) => {
        movies = data;
        let new_movie_list = [];
        for (let movie of movies) {
            if (!movie.downloaded) {
                new_movie_list.push(movie);
            }
        }

        default_list = new_movie_list;
        process_movies(new_movie_list);

    })
    .catch((error) => console.log(error));

const year = document.getElementById("th_year");
const tv = document.getElementById("th_tv");

year.addEventListener("click", function () {
    if (order) {
        current_list.sort((a, b) => a.year - b.year);
        order = false;
    } else {
        current_list.sort((a, b) => b.year - a.year);
        order = true;
    }
    process_movies(current_list);
});


tv.addEventListener("click", function () {
    if (order) {
        current_list.sort((a, b) => {
            if (a.series === b.series) {
                return 0;
            }
            return a.series ? -1 : 1;
        });
        order = false;
    } else {
        current_list.sort((a, b) => {
            if (a.series === b.series) {
                return 0;
            }
            return a.series ? 1 : -1;
        });
        order = true;
    }
    process_movies(current_list);
});


