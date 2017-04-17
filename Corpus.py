import os

class Corpus:
    def __init__(self, rootDirectory, toLowercase=False, filters=[]):
        self.documents = {}
        self.loadRootDirectory(rootDirectory, toLowercase, filters)


    def loadDocument(self, fileName, filePath, toLowercase=False, filters=[]):
        """Read the content of a file and add it to the corpus' documents.
        """
        text = ""
        with open(filePath, "r", encoding="utf-8") as file:
            text = file.read()

        if toLowercase:
            text = text.lower()
        for filterString in filters:
            text = text.replace(filterString, " ")

        self.documents[fileName] = text


    def loadRootDirectory(self, rootDirectory, toLowercase=False, filters=[]):
        """Recursively walk through all subfolders to find (only) text files.
        These text files are loaded as individual documents.
        """
        for subdirectory, directories, files in os.walk(rootDirectory):
            for file in files:
                if file.endswith(".txt"):
                    # Skip the extension in the filename definition.
                    self.loadDocument(file[:-4], os.path.join(subdirectory, file),
                                      toLowercase, filters)
