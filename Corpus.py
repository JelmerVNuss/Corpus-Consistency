import os

class Corpus():
    def __init__(self, rootDirectory):
        self.documents = {}
        self.loadRootDirectory(rootDirectory)

    def loadDocument(self, fileName, filePath):
        """Read the content of a file and add it to the corpus' documents.
        """
        text = ""
        with open(filePath, "r", encoding="utf-8") as file:
            text = file.read()
        self.documents[fileName] = text

    def loadRootDirectory(self, rootDirectory):
        """Recursively walk through all subfolders to find (only) text files.
        These text files are loaded as individual documents.
        """
        for subdirectory, directories, files in os.walk(rootDirectory):
            for file in files:
                if file.endswith(".txt"):
                    # Skip the extension in the filename definition.
                    self.loadDocument(file[:-4], os.path.join(subdirectory, file))
