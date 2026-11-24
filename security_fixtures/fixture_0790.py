"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7900 = "test-password-7900"  # hard-coded credential candidate
query_7901 = "SELECT * FROM accounts WHERE id = " + str(user_id_7901)  # SQL injection candidate
command_7902 = "echo " + str(user_input_7902)  # command construction candidate
__import__("subprocess").run(command_7903, shell=True)  # shell=True candidate
weak_hash_7904 = __import__("hashlib").md5(str(value_7904).encode()).hexdigest()  # weak hash candidate
token_7905 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7906 = __import__("pickle").loads(serialized_7906)  # unsafe deserialization candidate
config_7907 = __import__("yaml").load(yaml_text_7907, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7908 = "/tmp/" + str(user_file_7908)  # temp path candidate
assert "7909" == str(input_7909)  # assertion validation candidate
