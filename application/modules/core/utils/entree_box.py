import dropbox
import os
from random import *

from ..exc.failed import InvalidCredentialsError
from ..exc.failed import DuplicateResourceError
from ..exc.failed import InternalServerError
from ..exc.failed import FileNotFound


class EntreeStorage(object):

    """
        Entree Drop Box library. Storage for entree videos.
    """


    def __init__(self):

        """
            class instantiated with a dropbox token
            raise authentication error if token doesnt exist
        """
        try:
            self.access_token = os.environ['DROPBOX_TOKEN']
            self.dropbox= dropbox.Dropbox(self.access_token)

        except Exception as e:
            raise InvalidCredentialsError(e)

    def create_folder(self, folder_name):
        """
            Organisation is key. All tutorial should be 
            properly organised in their various folder
        """
        folder_path = '/'+folder_name

        #check entreebox if the folder already exist
        check_if_folder_exist = self.dropbox.files_search(path='', query=self.folder_name)
        if check_if_folder_exist.matches:
            raise DuplicateResourceError('Folder name already exist')

        #create folder
        self.dropbox.files_create_folder(folder_path)

    def create_preview(self, folder, file):

        """
            Allows saving of a preview file. file sent to 
            this function are renamed to preview and saved in t
            he folder root.

            :params
                folder(str): name of the folder.
                file(obj): file obj. The file intended to be saved
            :raises
                InternalServerError. When an exception occurs
        """

        try:

            with open(file, 'rb') as file:
                path = folder + '/preview'
                self.dropbox.files_upload(file.read(), path , mute=True)
                new_share = self.dropbox.sharing_create_shared_link_with_settings(path)

                return new_share.url, return_data.id

        except Exception as e:
            raise InternalServerError(e)

    def delete_file(self, url, folder):
        """
            deletes file from drop box
            :params
                url(str): saved url of the file to be deleted
                folder(str): folder name where the file is located
            :raises
                FileNotFound and encapsulated as InternalServerError
        """
        try: 

            get_filename = self.dropbox.sharing_get_shared_link_metadata(url)
            filename = get_filename.name
            foldername = '/' +folder+ '/' +filename

            response = self.dropbox.files_delete(folder_name)
            if response.id:
                return True
            else:
                raise FileNotFound()

        except Exception as e:
            raise InternalServerError(e)

    def upload_file(self, folder, file, filename):
        """
            Does the same thing with create_preview. 
            creates new file in a folder on dropbox
            gives option of renaming the file if a 
            filename is given
        """
        with open(file, 'rb') as vid:
            if not filename:
                filename = file

            pth = folder_name + '/' + file_rename
            self.dropbox.files_upload(vid.read(), file_path , mute=True)
            new_share = self.drop.sharing_create_shared_link_with_settings(path)

            return new_share.url, return_data.id







