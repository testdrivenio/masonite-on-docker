"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    Get("/sample", "WelcomeController@show").name("welcome"),
    Post("/", "WelcomeController@upload"),
]
