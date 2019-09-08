from os.path import join
from django.conf import settings as s

HASH_BLOCKSIZE = getattr(s, "SEO_VILLE_SLUGGER_HASH_BLOCKSIZE", 65536)
HASH_DIRNAME_SLICE_SIZE = getattr(s, "SEO_VILLE_SLUGGER_HASH_DIRNAME_SLICE_SIZE", 2)
