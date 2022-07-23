from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/sample", "WelcomeController@show"),
    Route.post("/", "WelcomeController@upload"),
]
