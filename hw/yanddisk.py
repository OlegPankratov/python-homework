import requests


class YaUploader:
    def __init__(self, token: str):
        self.headers = {'Authorization': token}
        self.base_url = "https://cloud-api.yandex.net"

    def get_upload_link(self):
        url = self.base_url + "/v1/disk/resources/upload"
        params = {'path': 'text.txt', 'overwrite': 'true'}
        response = requests.get(url, headers=self.headers, params=params)
        upload_url = response.json()['href']
        return upload_url

    def upload(self, file_path: str):
        upload_url = self.get_upload_link()
        upload_response = requests.put(upload_url, data=open(file_path, "rb"), headers=self.headers)
        return upload_response


if __name__ == '__main__':
    path_to_file = 'yandex_files/test.txt'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
