import requests
def a():
    
    zip_file_path = "1.apk"

    # Define your BrowserStack username and access key
    username = "emadhassan_K6LGzr"
    accessKey = "nkX6qyHhaGkMWbCx2bi3"

    # URL for uploading the ZIP file to BrowserStack
    upload_url = "https://api-cloud.browserstack.com/app-automate/upload-app"
    #upload_url = 'https://api-cloud.browserstack.com/app-automate/upload'
    #upload_url = 'https://api-cloud.browserstack.com/app-automate/upload-media'
    #upload_url = 'https://api-cloud.browserstack.com/app-automate/earlgrey/app-dir'
    # Create authentication header
    auth_header = (username, accessKey)

    # Open the ZIP file in binary mode
    with open(zip_file_path, 'rb') as file:
        # Prepare the files to be uploaded
        files = {'file': file, 'custom_id': 'Images'}

        # Send the POST request with authentication headers and files
        response = requests.post(upload_url, files=files, auth=auth_header)
    print(response.text)
    # Check if the request was successful
    if response.status_code == 200:
        print("Upload successful!")
    else:
        print(f"Upload failed with status code: {response.status_code}")
def s():

    username = "bsuser_nbks9r"
    access_key = "pwQ6HmKdgxT9u71Tja5n"

    app_url = ""    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    auth = (username, access_key)

    payload = {
        "url": app_url
    }

    response = requests.post("https://api-cloud.browserstack.com/app-automate/upload", auth=auth, headers=headers, json=payload)

    print(response.json())


s()
