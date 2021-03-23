# mysite/custom_azure_storage_backends.py

from storages.backends.azure_storage import AzureStorage
class AzureMediaStorage(AzureStorage):
    account_name = 'teiajuridicastorage'
    account_key = 'OQESupQkys4JfCYrRiwhzwvup57T4sAXzhp0ofFAjDZzzJ0PGmGBAgvmYTKIobsGR2HsnjyIp5A5RAYY+HQUzg=='
    azure_container = 'media'
    expiration_secs = None