Just One of those things
------------------------

Seo ville slugger will solve the problems you are having with django, media
files and filenames.

Django's default storage backend has some pretty annoying behaviour.
When uploading the same file for the second time, you get a second file on disk
with some kind of crazy hash value added at the end.

There are 2 kinds of people that are not happy with that.

1. The person that has to pay for disk space
2. The SEO people your customer has hired.

This storage backend stores files named after their hash value and adds a symlink
with the original name. No duplication and you can SEO your heart out.

Media file and pagespeed mobile score
=====================================

Ideally, you would want to have long cache expiry headers for your site’s uploaded files,
Just like you’ve got with your static files.
That usually poses a problem in conjunction with the pretty urls.
It is safe to put long expiry headers when using SEOStorage, because the files
are distributed over folders named after a tiny piece of the hash.
Obviously this small hash could lead to collisions, so the storage backend will prevent
it as follows:

In the rare case we encounter two different files with exactly the same filename, and they end up in the same folder
due to hash collision, the new file will not get the pretty SEO url. Instead the full hashed filename
will be used instead. In these rare cases you might get a SEO unfriendly url.

We can’t worry about that can we? Phat phat chance anyone will notice!

Usage
=====

You can use the storage backend on a global level by adding the following to
your django settings::

    DEFAULT_FILE_STORAGE = 'seo.ville.slugger.SEOStorage'

Sorl thumbnail
==============

Suppose you want sorl thumbnail to also have nice urls based on the original
filename?::

    THUMBNAIL_BACKEND = 'seo.ville.sorl.SEOThumbnailBackend'
    THUMBNAIL_STORAGE  = 'seo.ville.sorl.SEOThumbnailStorage'

With sorl you can pass the slug as a parameter to the thumbnail tag::

    {% thumbnail image "330x450" upscale=True slug=slug as thumb %}

Settings
========

- ``SEO_VILLE_SLUGGER_HASH_BLOCKSIZE`` change this if you think hashing of the file use too much or not enough memory
- ``SEO_VILLE_SLUGGER_HASH_DIRNAME_SLICE_SIZE`` change this if you find there are too many collisions.
- ``SEO_VILLE_SLUGGER_ALLOW_COPIES`` set this value to True if your media files get copies from server to server.
   Because this process breaks the hardlinks, you will get failed assertion errors claiming the following:
   ``The only way this can really happen if is when somebody uploads a file that is named after the hash of an existing file AND there is a collision in the first part of the hash. So if I've got an existing file that turns out after hashing as ce/cec9b1f7db34f7fa87bc3e807c9adf318deb30ef.jpg and then upload a file also named cec9b1f7db34f7fa87bc3e807c9adf318deb30ef.jpg but the hash of that file is really ce21b943a1d54b1e69194a823dcabcb103ed5888, which is completely different except for the first 2 characters. In that case this assertion will fail. Since this is not an exploit and the bad behaviour is on purpose, there will be an error and nobody will care.``
