Just One of those things
------------------------

Django's default storage backend has some pretty annoying behaviour.
When uploading the same file for the second time, you get a second file on disk
with some kind of crazy hash value added at the end.

There are 2 kinds of people that are not happy with that.

1. The person that has to pay for disk space
2. The SEO people your customer has hired.

This storage backend stores files named after their hash value and adds a symlink
with the original name. No duplication and you SEO your heart out.

Usage
=====

You can use the storage backend on a global level by adding the following to
your django settings::

    DEFAULT_FILE_STORAGE = 'seo.ville.slugger.SEOStorage'
