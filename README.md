# Movie Watch List Tracker

Movie Watch List Tracker is a simple web application designed to help users manage their movie watchlist. With this application, users can easily add, edit, and search for movies, as well as mark them as watched or downloaded. The project provides a user-friendly interface for convenient navigation and interaction.

![Image of the web page](https://github.com/mr-alham/projects-of-alham/blob/main/private/movie-watch-list-main-page.png "Home page")

## Features

- **Add Movies**: Users can add new movies to their watchlist, providing details such as the movie name, release year, and whether it is a TV series.
- **Edit Movies**: Existing movies can be edited to update their details, including the movie name, year, and series status.
- **Label Movies**: Users can mark movies as watched or downloaded, helping them keep track of their viewing progress.
- **Search Movies**: The application includes a search feature that allows users to quickly find movies by year or by TV-Series in their watchlist.
- **User Interface**: The project provides a clean and intuitive user interface for easy navigation and management of the watchlist.

## Getting Started

To run the Movie Watch List Tracker locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies using   `pip install -r requirements.txt`.
3. navigate to the directory where the `app.py` is   `cd Movie-Watch-list-Tracker/app`.
4. Run the Flask web application using   `gunicorn -w 4 -b 0.0.0.0:8000 app:app`.
5. Open your web browser and navigate to   `http://localhost:8000` to access the application.

## Usage

- **To add a Movie**: Click on the "Add a Movie" option in the header and fill out the text boxes with the movie details.
- **To Edit a  Movie**: Navigate to the movie you want to edit and click on '•••' and click the "Edit" option. Modify the details and click "Edit Movie."
- **To Label Watched or Downloaded Movies**: Navigate to the movie which needs to label and click on '•••' and select checkboxes as you wish and click 'Done' to save.
- **To Search for a Movies**: Use the search bar on the homepage to search movies by title or by the year.

## Docker

- **Build the Dcoker Image**:
    ```bash
    docker build -t movie_watch_list .
    ```

- **Run the Docker Image as a Container**:
    ```bash
    docker run --name movie_watch_list -p 8000:8000 -d movie_watch_list
    ```
    
***OR***

- **Pull the Image and run the Image:**
  ```bash
  docker pull mralham/movie_watch_list:latest
  ```
  ```bash
  docker run --name movie_watch_list \
  -v movie_data:/app/data \
  -p 80:80 \
  -d mralham/movie_watch_list
  ```

***OR***

- **Run the Image directly:**
  ```bash
  docker run --name movie_watch_list \
  -v movie_data:/app/data \
  -p 80:80 \
  -d mralham/movie_watch_list
  ```
  - Then access the website using `http://localhost` OR `http://127.0.0.1`
  - If the port is already in use replace `host port` with a desired port number as `<host port>:80` in `-p 80:80`.
## Contributing

Contributions to Movie Watch List Tracker are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.

Please ensure that your code follows the project's coding conventions and includes appropriate documentation and tests.

## License

This project is licensed under the MIT License. Feel free to use and modify it according to your needs.

## Contact

For any inquiries or support, please contact alham@duck.com.
