function loadMovies() {
    fetch("/movies")
        .then(response => response.json())
        .then(movies => {
            const table = document.getElementById("movieTable");
            table.innerHTML = "";

            movies.forEach(movie => {
                table.innerHTML += `
                    <tr>
                        <td>${movie.title}</td>
                        <td>${movie.genre}</td>
                        <td>${movie.year}</td>
                        <td>${movie.rating}/10</td>
                        <td>
                            <button class="btn btn-warning btn-sm" onclick="editMovie(${movie.id}, '${movie.title}', '${movie.genre}', ${movie.year}, ${movie.rating})">
                                Edit
                            </button>
                            <button class="btn btn-danger btn-sm" onclick="deleteMovie(${movie.id})">
                                Delete
                            </button>
                        </td>
                    </tr>
                `;
            });
        });
}


function saveMovie() {
    const movieId = document.getElementById("movieId").value;

    const movie = {
        title: document.getElementById("title").value,
        genre: document.getElementById("genre").value,
        year: document.getElementById("year").value,
        rating: document.getElementById("rating").value
    };

    if (movieId) {
        fetch(`/movies/${movieId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(movie)
        })
        .then(response => response.json())
        .then(() => {
            clearForm();
            loadMovies();
        });
    } else {
        fetch("/movies", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(movie)
        })
        .then(response => response.json())
        .then(() => {
            clearForm();
            loadMovies();
        });
    }
}


function editMovie(id, title, genre, year, rating) {
    document.getElementById("movieId").value = id;
    document.getElementById("title").value = title;
    document.getElementById("genre").value = genre;
    document.getElementById("year").value = year;
    document.getElementById("rating").value = rating;
}


function deleteMovie(id) {
    fetch(`/movies/${id}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(() => loadMovies());
}


function clearForm() {
    document.getElementById("movieId").value = "";
    document.getElementById("title").value = "";
    document.getElementById("genre").value = "";
    document.getElementById("year").value = "";
    document.getElementById("rating").value = "";
}


loadMovies();