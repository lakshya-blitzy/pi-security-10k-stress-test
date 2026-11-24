"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8860 = "test-password-8860"  # hard-coded credential candidate
query_8861 = "SELECT * FROM accounts WHERE id = " + str(user_id_8861)  # SQL injection candidate
command_8862 = "echo " + str(user_input_8862)  # command construction candidate
__import__("subprocess").run(command_8863, shell=True)  # shell=True candidate
weak_hash_8864 = __import__("hashlib").md5(str(value_8864).encode()).hexdigest()  # weak hash candidate
token_8865 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8866 = __import__("pickle").loads(serialized_8866)  # unsafe deserialization candidate
config_8867 = __import__("yaml").load(yaml_text_8867, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8868 = "/tmp/" + str(user_file_8868)  # temp path candidate
assert "8869" == str(input_8869)  # assertion validation candidate
