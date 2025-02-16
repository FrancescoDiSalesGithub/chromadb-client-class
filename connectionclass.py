import sys
import chromadb

class connectionClass:
    def __init__(self,host,port,ssl):
        self.host=host
        self.port=port
        self.ssl=ssl

    def host_connect(self):
        return chromadb.HttpClient(host=self.host,port=self.port,ssl=self.ssl)    
    
    def create_collection(self,name):
        chromadb.HttpClient(host=self.host,port=self.port,ssl=self.ssl).create_collection(name)




class documentationClass(connectionClass):
    def __init__(self,collection,host,port,ssl,documents,metadata,ids,embeddings):
        self.collection=connectionClass.host_connect(connectionClass.__init__(host,port,ssl))
        self.documents=documents
        self.metadata=metadata
        self.ids=ids
        self.embeddings=embeddings

    def add_normal(self):
        self.collection.add(documents=self.documents,metadatas=self.metadata,ids=self.ids) 

    def add_super(self):
        self.collection.add(documents=self.documents,metadatas=self.metadata,ids=self.ids,embeddings=self.embeddings)       


