import dropbox
import os
class TransferData:

    def __init__(self,access_token):
        self.access_token=access_token
        
    def upload_file(self,file_from,file_to):
        self.dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            reletive_path = 
        
def main():
    access_token='sl.A8wGoPqOfxFuy8wGgCyj9E0gcKb66hhHQbvdUeNdXS4gOUVeWMvvrIphiT9XSj9T9EDvx62Cp13odLZt6Z5_o8b6T9uWBO3sZv1RAeH1S_VhP_xzGjLxkiOXSQ6VSD8ZzSSQhkM'
    transferData=TransferData(access_token)

    file_from=input("Enter The File Path To Transfer: ")
    file_to=input("Enter The File Path To Upload")

    transferData.upload_file(file_from, file_to)
    print("File Has Been Moved")
main()