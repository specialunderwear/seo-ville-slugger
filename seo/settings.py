from os.path import join
from django.conf import settings as s

HASH_BLOCKSIZE = getattr(s, "SEO_VILLE_SLUGGER_HASH_BLOCKSIZE", 65536)
MAX_FILENAME_LENGTH = getattr(s, "SEO_VILLE_SLUGGER_MAX_FILENAME_LENGTH", 512)
