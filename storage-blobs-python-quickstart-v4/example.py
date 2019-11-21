# ----------------------------------------------------------------------------------
# MIT License
#
# Copyright(c) Microsoft Corporation. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# ----------------------------------------------------------------------------------
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



import os, uuid, sys
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, PublicAccess

# ---------------------------------------------------------------------------------------------------------
# Method that creates a test file in the 'Documents' folder.
# This sample application creates a test file, uploads the test file to the Blob storage,
# lists the blobs in the container, and downloads the file with a new name.
# ---------------------------------------------------------------------------------------------------------
# Documentation References:
# Associated Article - https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
# What is a Storage Account - http://azure.microsoft.com/en-us/documentation/articles/storage-whatis-account/
# Getting Started with Blobs - https://docs.microsoft.com/en-us/azure/storage/blobs/storage-python-how-to-use-blob-storage
# Blob Service Concepts - http://msdn.microsoft.com/en-us/library/dd179376.aspx
# Blob Service REST API - http://msdn.microsoft.com/en-us/library/dd135733.aspx
# ----------------------------------------------------------------------------------------------------------


def run_sample():
    try:
        # Create the BlobServiceClient that is used to call the Blob service for the storage account
        conn_str = os.environ['AZURE_STORAGE_CONNECTIONSTRING']
        blob_service_client = BlobServiceClient.from_connection_string(conn_str=conn_str)

        # Create a container called 'quickstartblobs' and Set the permission so the blobs are public.
        container_name = 'quickstartblobs'
        blob_service_client.create_container(container_name, public_access=PublicAccess.Container)

        # Create Sample folder if it not exists, and create a file in folder Sample to test the upload and download.
        local_path = os.path.expanduser("~/Sample")
        if not os.path.exists(local_path):
            os.makedirs(os.path.expanduser("~/Sample"))
        local_file_name ="QuickStart_" + str(uuid.uuid4()) + ".txt"
        full_path_to_file = os.path.join(local_path, local_file_name)

        # Write text to the file.
        file = open(full_path_to_file,  'w')
        file.write("Hello, World!")
        file.close()

        print("Temp file = " + full_path_to_file)
        print("\nUploading to Blob storage as blob" + local_file_name)

        # Upload the created file, use local_file_name for the blob name
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
        with open(full_path_to_file, "rb") as data:
            blob_client.upload_blob(data)

        # List the blobs in the container
        print("\nList blobs in the container")
        container = blob_service_client.get_container_client(container=container_name)
        generator = container.list_blobs()
        for blob in generator:
            print("\t Blob name: " + blob.name)

        # Download the blob(s).
        # Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
        full_path_to_file2 = os.path.join(local_path, str.replace(local_file_name ,'.txt', '_DOWNLOADED.txt'))
        print("\nDownloading blob to " + full_path_to_file2)
        with open(full_path_to_file2, "wb") as my_blob:
            my_blob.writelines([blob_client.download_blob().readall()]) 

        sys.stdout.write("Sample finished running. When you hit <any key>, the sample will be deleted and the sample "
                         "application will exit.")
        sys.stdout.flush()
        input()

        # Clean up resources. This includes the container and the temp files
        blob_service_client.delete_container(container_name)
        os.remove(full_path_to_file)
        os.remove(full_path_to_file2)
    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    run_sample()



