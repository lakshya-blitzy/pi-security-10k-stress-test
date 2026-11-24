"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8900 = "test-password-8900"  # hard-coded credential candidate
query_8901 = "SELECT * FROM accounts WHERE id = " + str(user_id_8901)  # SQL injection candidate
command_8902 = "echo " + str(user_input_8902)  # command construction candidate
__import__("subprocess").run(command_8903, shell=True)  # shell=True candidate
weak_hash_8904 = __import__("hashlib").md5(str(value_8904).encode()).hexdigest()  # weak hash candidate
token_8905 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8906 = __import__("pickle").loads(serialized_8906)  # unsafe deserialization candidate
config_8907 = __import__("yaml").load(yaml_text_8907, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8908 = "/tmp/" + str(user_file_8908)  # temp path candidate
assert "8909" == str(input_8909)  # assertion validation candidate
