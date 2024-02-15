from .client import AuthenticatedClient

from .api import (
    DatapointsModule,
    EmbeddingsModule,
    FinetuningModule,
    AuthModuleWrapper,
    ChatModuleWrapper,
)

class Prem:
    datapoints: DatapointsModule
    embeddings: EmbeddingsModule
    finetuning: FinetuningModule
    auth: AuthModuleWrapper
    chat: ChatModuleWrapper

    def __init__(self, api_key: str, base_url='https://app.premai.io'):
        client = AuthenticatedClient(token=api_key, base_url=base_url)
        # Init modules
        self.datapoints = DatapointsModule(client)
        self.embeddings = EmbeddingsModule(client)
        self.finetuning = FinetuningModule(client)
        self.auth = AuthModuleWrapper(client)
        self.chat = ChatModuleWrapper(client)

__all__ = [
    "Prem"
]