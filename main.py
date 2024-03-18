from gofile import GoFileClient

if __name__ == "__main__":
    base_url = "https://api.gofile.io"
    token = "4aBC39u08louNTvzW2P82yIudyannz0z"
    gofile_client = GoFileClient(base_url, token)

    servers = gofile_client.get_account_id()
    print(servers)
