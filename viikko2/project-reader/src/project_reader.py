from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_dict = toml.loads(content)
        name = toml_dict["tool"]["poetry"]["name"]
        description = toml_dict["tool"]["poetry"]["description"]
        dependencies = toml_dict["tool"]["poetry"]["dependencies"].keys()
        dev_dependencies = toml_dict["tool"]["poetry"]["dev-dependencies"].keys()

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
