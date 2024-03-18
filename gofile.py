import requests


class GoFileClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def _send_request(self, method, url, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = {}
        kwargs["headers"]["Authorization"] = f"Bearer {self.token}"
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()

    def get_servers(self):
        return self._send_request("GET", f"{self.base_url}/servers")

    def upload_file(self, server, file_path, folder_id=None):
        url = f"https://{server}.gofile.io/contents/uploadfile"
        files = {"file": open(file_path, "rb")}
        data = {"folderId": folder_id} if folder_id else {}
        return self._send_request("POST", url, files=files, data=data)

    def create_folder(self, parent_folder_id, folder_name):
        data = {
            "parentFolderId": parent_folder_id,
            "folderName": folder_name,
        }
        return self._send_request("POST", f"{self.base_url}/contents/createFolder", json=data)

    def delete_content(self, contents_id):
        data = {"contentsId": contents_id}
        return self._send_request("DELETE", f"{self.base_url}/contents", json=data)

    def get_content(self, content_id):
        return self._send_request("GET", f"{self.base_url}/contents/{content_id}")

    def create_direct_link(self, content_id):
        return self._send_request("POST", f"{self.base_url}/contents/{content_id}/directlinks")

    def update_direct_link(self, content_id, direct_link_id, expire_time):
        data = {"expireTime": expire_time}
        return self._send_request("PUT", f"{self.base_url}/contents/{content_id}/directlinks/{direct_link_id}",
                                  json=data)

    def delete_direct_link(self, content_id, direct_link_id):
        return self._send_request("DELETE", f"{self.base_url}/contents/{content_id}/directlinks/{direct_link_id}")

    def copy_content(self, contents_id, folder_id):
        data = {
            "contentsId": contents_id,
            "folderId": folder_id
        }
        return self._send_request("POST", f"{self.base_url}/contents/copy", json=data)

    def move_content(self, contents_id, folder_id):
        data = {
            "contentsId": contents_id,
            "folderId": folder_id
        }
        return self._send_request("PUT", f"{self.base_url}/contents/move", json=data)

    def get_account_id(self):
        return self._send_request("GET", f"{self.base_url}/accounts/getid")

    def reset_token(self, account_id):
        return self._send_request("POST", f"{self.base_url}/accounts/{account_id}/resettoken")
