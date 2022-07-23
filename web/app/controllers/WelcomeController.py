"""A WelcomeController Module."""

from masonite.controllers import Controller
from masonite.filesystem import Storage
from masonite.request import Request
from masonite.views import View


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("welcome")

    def upload(self, storage: Storage, view: View, request: Request):
        filename = storage.disk("local").put_file("image_upload", request.input("image_upload"))
        return view.render("welcome", {"image_url": f"/framework/filesystem/{filename}"})
