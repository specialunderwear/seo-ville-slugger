from os.path import exists

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class SpecificNameStorage(FileSystemStorage):
    """
    Storage class that does not try to invent a new name when saving a file.
    """

    def __init__(self):
        super(SpecificNameStorage, self).__init__(location=settings.MEDIA_ROOT)

    def get_available_name(self, name, max_length=None):
        return name

    def _save(self, name, content):
        full_path = self.path(name)
        if not exists(full_path):
            return super(SpecificNameStorage, self)._save(name, content)
        return name
