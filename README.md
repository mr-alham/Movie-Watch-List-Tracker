# Movie Watch List Tracker

Movie Watch List Tracker is a simple web application designed to help users manage their movie watchlist. With this application, users can easily add, edit, and search for movies, as well as mark them as watched or downloaded. The project provides a user-friendly interface for convenient navigation and interaction.

![Image of the web page](https://github.com/mr-alham/projects-of-alham/blob/main/private/movie-watch-list-main-page.png "Home page")

## Features

- **Add Movies**: Users can add new movies to their watchlist, providing details such as the movie name, release year, and whether it is a TV series.
- **Edit Movies**: Existing movies can be edited to update their details, including the movie name, year, and series status.
- **Mark as Watched/Downloaded**: Users can mark movies as watched or downloaded, helping them keep track of their viewing progress.
- **Search Functionality**: The application includes a search feature that allows users to quickly find specific movies in their watchlist.
- **User Interface**: The project provides a clean and intuitive user interface for easy navigation and management of the watchlist.

## Getting Started

To run the Movie Watch List Tracker locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies using   `pip install -r requirements.txt`.
3. navigate to the directory where the `app.py` is   `cd Movie-Watch-list-Tracker/app`.
4. Run the Flask web application using   `gunicorn -w 4 -b 0.0.0.0:8000 app:app`.
5. Open your web browser and navigate to   `http://localhost:8000` to access the application.

## Usage

- **Adding Movies**: Click on the "Add a Movie" option in the header and fill out the form with the movie details.
- **Editing Movies**: Navigate to the movie you want to edit and click on the "Edit" option. Modify the details and click "Edit Movie."
- **Marking as Watched/Downloaded**: When editing a movie, you can check the corresponding checkboxes to mark it as watched or downloaded.
- **Searching for Movies**: Use the search bar on the homepage to search for movies by title or other criteria.

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
