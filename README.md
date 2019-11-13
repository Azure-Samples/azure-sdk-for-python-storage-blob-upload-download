# Quickstart with Azure Storage Blobs SDK for Python

### Prerequisites
If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.

### Create a Storage Account using the Azure Portal

Step 1 : Create a new general-purpose Storage Account to use for this tutorial. 
 
*  Go to the [Azure Portal](https://portal.azure.com) and log in using your Azure account. 
*  Select **New** > **Storage** > **Storage account**. 
*  Select your Subscription. 
*  For `Resource group`, create a new one and give it a unique name. 
*  Enter a name for your storage Account. The name must be between 3 and 24 characters in length and may contain numbers and lowercase letters only. It must also be unique.
*  Select the `Location` to use for your Storage Account.
*  Set `Account kind` to **StorageV2(general purpose v2)**.
*  Set `Performance` to **Standard**. 
*  Set `Replication` to **Locally-redundant storage (LRS)**.
*  Set `Secure transfer required` to **Disabled**.
*  Check **Review + create** and click **Create** to create your Storage Account. 
 
Step 2 : Copy and save Connection string.

After your Storage Account is created. Click on it to open it. 
Select **Settings** > **Access keys** > **Primary Key**, copy the associated **Connection string** to the clipboard, then paste it into a text editor for later use.

### Set credentials in environment variables 

Linux
```
export AZURE_STORAGE_CONNECTIONSTRING="<yourconnectionstring>" 
```

Windows
```
setx AZURE_STORAGE_CONNECTIONSTRING "<yourconnectionstring>" 
```

### Folders Introduction
You will find the following folders: storage-blobs-python-quickstart-v3, which references the 2.1.0 SDK and storage-blobs-python-quickstart-v4, which uses the 12.0.0 version of the SDK.

### This Quickstart shows how to do some basic operations of Storage Blobs.
- Create a Storage Account using the Azure Portal.
- Create a container.
- Upload a file to block blob.
- List blobs.
- Download a blob to file.
- Delete a blob.
- Delete the container.

### Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
