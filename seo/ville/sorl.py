import contextlib

from os import path, remove
from tempfile import NamedTemporaryFile

from PIL import Image, ImageColor

from sorl.thumbnail.base import ThumbnailBackend, EXTENSIONS
from sorl.thumbnail.conf import settings
from sorl.thumbnail import default

from .slugger import SEOStorage



@contextlib.contextmanager
def create_copy_with_matte(source_image, matte=settings.THUMBNAIL_PADDING_COLOR):
    with NamedTemporaryFile(suffix=".png", delete=False) as non_transparent_source_image:
        new_pic = Image.new("RGB", source_image.size, ImageColor.getrgb(matte))
        rgba_png = source_image.convert("RGBA")
        new_pic.paste(rgba_png, rgba_png)
        new_pic.save(non_transparent_source_image)
        new_pic.close()
        non_transparent_source_image.seek(0)

        yield default.engine.get_image(non_transparent_source_image)

        non_transparent_source_image.close()
        remove(non_transparent_source_image.name)


class SEOThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        name = path.basename(source.name)
        dirname = path.dirname(source.name)
        base, _ = path.splitext(name)
        if "slug" in options:
            base = options["slug"]

        return path.join(
            dirname, "%s.%s.%s" % (base, geometry_string, EXTENSIONS[options["format"]])
        )

    def _create_thumbnail(self, source_image, geometry_string, options, thumbnail):
        key_at_start = thumbnail.key

        # if PNG is transformed to JPEG transparency is lost. Make sure
        # to set matte to whatver THUMBNAIL_PADDING_COLOR has been set to.
        # if this is not done, the background will be black.
        if source_image.format == "PNG" and options.get("format") == "JPEG":
            with create_copy_with_matte(source_image) as non_transparent_source_image:
                super()._create_thumbnail(
                    non_transparent_source_image, geometry_string, options, thumbnail
                )
        else:
            super()._create_thumbnail(source_image, geometry_string, options, thumbnail)

        key_at_end = thumbnail.key

        # make sure to get cache hits on the original requested filename, not the
        # filename returned by the file storage backend.
        if key_at_start != key_at_end:
            # pylint: disable=protected-access
            default.kvstore._set(key_at_start, thumbnail)


class SEOThumbnailStorage(SEOStorage):
    prefix = settings.THUMBNAIL_PREFIX
