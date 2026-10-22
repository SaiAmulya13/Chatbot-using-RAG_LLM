# import all required softwares
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbedding
from langchain_community.vectorstores import FAISS
import os

#step-1:load pdf file store into mydocuments
file_path=os.path.join('documents','tcs.pdf')
loader=PyPDFLoader(file_path)
documents=loader.load()
print('total pages are..',len(documents))

#step-2:convert to chunks
splitter=RecursiveCharacterTextSplitter(chunk_size=2000,
                                       chunk_overlap=500,)
mychunks=splitter.split_documents(documents)
print('total chunks are..',len(mychunks))

#step-3:create embedding model
embeddings=HuggingFaceEmbedding(model_name='sentence-transformers/all-mpnet-base-v2')

#step-4:create faiss db
vector_store=FAISS.from_documents(documents=mychunks,
                                  embedding=embeddings,)

#step-5:store faiss db in some local place
vector_store.save_local('faiss_index') #this is our database name
print('successfully saved pdf files into db....')

'''
from real time python file, if you want to use faisss we need to load faiss.
my_vector_store=FAISS.load_local('faiss_index,
                                embeddings,
                                allow_dangerous_deserialization=True')
docs=new_vector_store.similarity_search('question')
'''

