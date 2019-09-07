from os import path
from sorl.thumbnail.base import ThumbnailBackend


class SEOThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        name = path.basename(source.name)
        base, ext = path.splitext(name)
        return "%s.%s%s" % (base, geometry_string, ext)
