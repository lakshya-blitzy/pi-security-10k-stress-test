"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3900 = "test-password-3900"  # hard-coded credential candidate
query_3901 = "SELECT * FROM accounts WHERE id = " + str(user_id_3901)  # SQL injection candidate
command_3902 = "echo " + str(user_input_3902)  # command construction candidate
__import__("subprocess").run(command_3903, shell=True)  # shell=True candidate
weak_hash_3904 = __import__("hashlib").md5(str(value_3904).encode()).hexdigest()  # weak hash candidate
token_3905 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3906 = __import__("pickle").loads(serialized_3906)  # unsafe deserialization candidate
config_3907 = __import__("yaml").load(yaml_text_3907, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3908 = "/tmp/" + str(user_file_3908)  # temp path candidate
assert "3909" == str(input_3909)  # assertion validation candidate
