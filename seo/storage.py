from os.path import exists

from django.core.files.storage import FileSystemStorage


class SpecificNameStorage(FileSystemStorage):
    """
    Storage class that does not try to invent a new name when saving a file.
    """

    def get_available_name(self, name, max_length=None):
        return name

    def _save(self, name, content):
        full_path = self.path(name)
        if not exists(full_path):
            return super(SpecificNameStorage, self)._save(name, content)
        return name
