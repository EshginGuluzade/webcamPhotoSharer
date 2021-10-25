from filestack import Client

class FileSharer:

    # The API key allows us to upload the image to the web
    # You can create a free account on www.filestack.com, copy your API key and paste it below
    def __init__(self, file_path, api_key="Please use your own API key"):
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.file_path)
        return new_filelink.url
