from gofile import GoFileClient

if __name__ == "__main__":
    token = "4aBC39u08louNTvzW2P82yIudyannz0z"
    gofile_client = GoFileClient(token)

    servers = gofile_client.get_account_id()
    print(servers)
