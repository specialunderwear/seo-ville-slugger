from os import path
from sorl.thumbnail.base import ThumbnailBackend, EXTENSIONS
from sorl.thumbnail.conf import settings
from sorl.thumbnail import default
from .slugger import SEOStorage


class SEOThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        name = path.basename(source.name)
        dirname = path.dirname(source.name)
        base, ext = path.splitext(name)
        return path.join(
            dirname, "%s.%s.%s" % (base, geometry_string, EXTENSIONS[options["format"]])
        )

    def _create_thumbnail(self, source_image, geometry_string, options, thumbnail):
        key_at_start = thumbnail.key
        super()._create_thumbnail(source_image, geometry_string, options, thumbnail)
        key_at_end = thumbnail.key

        # make sure to get cache hits on the original requested filename, not the
        # filename returned by the file storage backend.
        if key_at_start != key_at_end:
            default.kvstore._set(key_at_start, thumbnail)


class SEOThumbnailStorage(SEOStorage):
    prefix = settings.THUMBNAIL_PREFIX
