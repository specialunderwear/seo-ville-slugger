from os import path
from sorl.thumbnail.base import ThumbnailBackend
from sorl.thumbnail.conf import settings
from .slugger import SEOStorage


class SEOThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        name = path.basename(source.name)
        base, ext = path.splitext(name)
        return "%s.%s%s" % (base, geometry_string, ext)


class SEOThumbnailStorage(SEOStorage):
    prefix = settings.THUMBNAIL_PREFIX
