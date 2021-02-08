import os
from os import path
import logging

from seo import settings as seo_settings
from seo.storage import SpecificNameStorage
from seo.utils import file_hash, storage_location

logger = logging.getLogger(__name__)

REASON_NO_LINK = (
    "The only way this can really happen if is when somebody uploads a file "
    "that is named after the hash of an existing file AND there is a collision "
    "in the first part of the hash. So if I've got an existing file that turns "
    "out after hashing as ce/cec9b1f7db34f7fa87bc3e807c9adf318deb30ef.jpg and then "
    "upload a file also named cec9b1f7db34f7fa87bc3e807c9adf318deb30ef.jpg but the "
    "hash of that file is really ce21b943a1d54b1e69194a823dcabcb103ed5888, which is "
    "completely different except for the first 2 characters. In that case this "
    "assertion will fail. Since this is not an exploit and the bad behaviour is on "
    "purpose, there will be an error and nobody will care."
)


class SEOStorage(SpecificNameStorage):
    prefix = ""

    def create_link(self, storage_path, link_path):
        full_storage_path = self.path(storage_path)
        full_link_path = self.path(link_path)

        if path.exists(full_link_path):
            if not seo_settings.ALLOW_COPIES:
                assert path.islink(full_link_path), REASON_NO_LINK
            if path.realpath(full_storage_path) == path.realpath(full_link_path):
                return link_path

            return storage_path

        os.symlink(path.basename(storage_path), full_link_path)
        return link_path

    def save(self, name, content, max_length=None):
        if name is None:
            name = content.name

        file_id = file_hash(content)
        storage_path, link_path = storage_location(file_id, name, self.prefix)
        stored_location = self._save(storage_path, content)
        logger.debug("File stored in %s", stored_location)
        return self.create_link(stored_location, link_path)
