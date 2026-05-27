"""
定义工厂文件去生产模型

工厂方法模式实现，用于创建不同类型的 AI 模型实例

"""
from abc import ABC, abstractmethod
from typing import Optional
from langchain_core.embeddings import Embeddings
from langchain_community.chat_models.tongyi import BaseChatModel
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models.tongyi import ChatTongyi
from utils.config_handler import rag_conf


class BaseModelFactory(ABC):
    """
    定义抽象方法：返回嵌入模型|聊天模型
    """
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        pass

# 定义子类去实现父类
class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return ChatTongyi(model=rag_conf["chat_model_name"])


class EmbeddingsFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return DashScopeEmbeddings(model=rag_conf["embedding_model_name"])


chat_model = ChatModelFactory().generator()
embed_model = EmbeddingsFactory().generator()
