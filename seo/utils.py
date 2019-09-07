import hashlib
from os.path import splitext, join, basename

from seo import settings as seo_settings


def file_hash(content):
    hasher = hashlib.sha1()
    buf = content.read(seo_settings.HASH_BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = content.read(seo_settings.HASH_BLOCKSIZE)

    content.seek(0)
    return hasher.hexdigest()


def file_name(file_id, name):
    _, ext = splitext(name)
    return "%s%s" % (file_id, ext.lower())


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)


def get_directory_from_file_id(file_id):
    return file_id[:2]


def storage_location(file_id, name, prefix=""):
    _, ext = splitext(name)
    ext = ext.lower()
    dir_name = get_directory_from_file_id(file_id)
    file_name = "%s%s" % (file_id, ext)
    ext_name = ext.replace(".", "")
    return (
        join(prefix, ext_name, dir_name, file_name),
        join(prefix, ext_name, dir_name, basename(name)),
    )
