from abc import ABC, abstractmethod

#---------------------------------------------Hello Welcome to Question No 3--------------------------------------


print("Question No 3")

class Document(ABC):
    def __init__(self, file_name, file_size, content):                                    
        self.file_name = file_name                              
        self.file_size = file_size                
        self.content = content                     

                                           

    @abstractmethod
    def open_document(self):
        pass
    
#--------------------------------------------------------------------------------------------

    @abstractmethod
    def read_document(self):
        pass
    
#---------------------------------------------------------------------------------------------

    @abstractmethod
    def save_document(self):
        pass


#---------------------------------------------------------------------------------------------







class Worddocument(Document):


    def open_document(self):
        print("Opening Word document:", self.file_name)
    

    def read_document(self):
        print("Reading Word document:", self.file_name)
    

    def save_document(self):
        print("Saving Word document:", self.file_name)

#--------------------------------------------------------------------------------------------

class Pdfdocument(Document):

    def open_document(self):
        print("Opening the pdf document:", self.file_name)
    

    def read_document(self):
        print("Reading the pdf document:", self.file_name)
    

    def save_document(self):
        print("Saving the pdf document:", self.file_name)

#----------------------------------------------------------------------------------------------

class Exceldocument(Document):
    def open_document(self):
        print("Opening Excel document:", self.file_name)
    
    def read_document(self):
        print("Reading Excel document:", self.file_name)
    
    def save_document(self):
        print("Saving Excel document:", self.file_name)

#------------------------------------------------------------------------------------------------

class DocumentFactory:
    @staticmethod
    def create_document(doc_type, file_name, file_size, content):
        if doc_type == "word":
            return Worddocument(file_name, file_size, content)
        elif doc_type == "pdf":
            return Pdfdocument(file_name, file_size, content)
        elif doc_type == "excel":
            return Exceldocument(file_name, file_size, content)
        else:
            raise ValueError("Wrong document type")



#-------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    word_doc = DocumentFactory.create_document("word", "waleed.docx", 256, "Course Outline Programming 101 Sec E  ")

    word_doc.open_document()

    word_doc.read_document()

    word_doc.save_document()


#--------------------------------------------------------------------------------------------------

    pdf_doc = DocumentFactory.create_document("pdf", "waleed.pdf", 128, "Notes Of P2 Section E")

    pdf_doc.open_document()

    pdf_doc.read_document()

    pdf_doc.save_document()
#------------------------------------------------------------------------------------------------------------

    excel_doc = DocumentFactory.create_document("excel", "waleed.xlsx", 512, "FInal Project Marksheeet")

    excel_doc.open_document()

    excel_doc.read_document()

    excel_doc.save_document()


#---------------------------------------------------------The End--------------------------------------------------
