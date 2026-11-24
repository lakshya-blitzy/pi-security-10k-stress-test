"""Generated insecure scanner-QA fixture. Do not deploy."""
password_860 = "test-password-860"  # hard-coded credential candidate
query_861 = "SELECT * FROM accounts WHERE id = " + str(user_id_861)  # SQL injection candidate
command_862 = "echo " + str(user_input_862)  # command construction candidate
__import__("subprocess").run(command_863, shell=True)  # shell=True candidate
weak_hash_864 = __import__("hashlib").md5(str(value_864).encode()).hexdigest()  # weak hash candidate
token_865 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_866 = __import__("pickle").loads(serialized_866)  # unsafe deserialization candidate
config_867 = __import__("yaml").load(yaml_text_867, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_868 = "/tmp/" + str(user_file_868)  # temp path candidate
assert "869" == str(input_869)  # assertion validation candidate
