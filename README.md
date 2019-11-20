---
page_type: sample
languages:
- python
products:
- azure
- azure-storage
description: "A simple sample project to help you get started using Azure Storage with python as the development language."
---

# Quickstart with Azure Storage Blobs SDK for Python

## SDK Versions
In this sample, you will find the following folders:v
* **[storage-blobs-python-quickstart-v3](./storage-blobs-python-quickstart-v3)** - references Storage Blobs SDK v2.1.0
* **[storage-blobs-python-quickstart-v4](./storage-blobs-python-quickstart-v4)** - references Storage Blobs SDK v12.0.0

## Prerequisites
If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.

## Create a Storage Account using the Azure Portal

Step 1 : Create a new general-purpose Storage Account to use for this tutorial. 
 
*  Go to the [Azure Portal](https://portal.azure.com) and log in using your Azure account. 
*  Select **New** > **Storage** > **Storage account**. 
*  Select your Subscription. 
*  For `Resource group`, create a new one and give it a unique name. 
*  Enter a name for your storage Account.
*  Select the `Location` to use for your Storage Account.
*  Set `Account kind` to **StorageV2(general purpose v2)**.
*  Set `Performance` to **Standard**. 
*  Set `Replication` to **Locally-redundant storage (LRS)**.
*  Set `Secure transfer required` to **Disabled**.
*  Check **Review + create** and click **Create** to create your Storage Account. 
 
Step 2 : Copy and save Connection string.

After your Storage Account is created. Click on it to open it. 
Select **Settings** > **Access keys** > **Key1/key**, copy the associated **Connection string** to the clipboard, then paste it into a text editor for later use.

## Put the connection string in an environment variable

This solution requires a connection string be stored in an environment variable securely on the machine running the sample. Follow one of the examples below depending on your operating system to create the environment variable. If using Windows close your open IDE or shell and restart it to be able to read the environment variable.

### Linux

```bash
export AZURE_STORAGE_CONNECTIONSTRING="<yourconnectionstring>"
```

### Windows

```cmd
setx AZURE_STORAGE_CONNECTIONSTRING "<yourconnectionstring>"
```

## This Quickstart shows how to do the following operations of Storage Blobs.
- Create a Storage Account using the Azure Portal.
- Create a container.
- Upload a file to block blob.
- List blobs.
- Download a blob to file.
- Delete a blob.
- Delete the container.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.