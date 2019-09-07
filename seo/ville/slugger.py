import os
from os import path
import logging

from seo.storage import SpecificNameStorage
from seo.utils import file_hash, storage_location

logger = logging.getLogger(__name__)


class SEOStorage(SpecificNameStorage):
    def create_link(self, storage_path, link_path):
        full_storage_path = self.path(storage_path)
        full_link_path = self.path(link_path)

        if path.exists(full_link_path):
            assert path.islink(full_link_path)
            if path.realpath(full_storage_path) == path.realpath(full_link_path):
                return link_path
            else:
                return storage_path

        os.symlink(full_storage_path, full_link_path)
        return link_path

    def save(self, name, content, max_length=None):
        if name is None:
            name = content.name

        file_id = file_hash(content)
        storage_path, link_path = storage_location(file_id, name)
        stored_location = self._save(storage_path, content)
        logger.debug("File stored in %s" % stored_location)
        return self.create_link(stored_location, link_path)
