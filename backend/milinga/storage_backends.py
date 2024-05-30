from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
    location = 'private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False

# Dateien später im Model öffentlich oder privat speichern:
# from milinga.storage_backends import PublicMediaStorage, PrivateMediaStorage
# file = models.FileField(storage=PublicMediaStorage())
# file = models.FileField(storage=PrivateMediaStorage())
