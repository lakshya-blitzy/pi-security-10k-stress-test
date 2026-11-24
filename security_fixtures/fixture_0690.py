"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6900 = "test-password-6900"  # hard-coded credential candidate
query_6901 = "SELECT * FROM accounts WHERE id = " + str(user_id_6901)  # SQL injection candidate
command_6902 = "echo " + str(user_input_6902)  # command construction candidate
__import__("subprocess").run(command_6903, shell=True)  # shell=True candidate
weak_hash_6904 = __import__("hashlib").md5(str(value_6904).encode()).hexdigest()  # weak hash candidate
token_6905 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6906 = __import__("pickle").loads(serialized_6906)  # unsafe deserialization candidate
config_6907 = __import__("yaml").load(yaml_text_6907, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6908 = "/tmp/" + str(user_file_6908)  # temp path candidate
assert "6909" == str(input_6909)  # assertion validation candidate
