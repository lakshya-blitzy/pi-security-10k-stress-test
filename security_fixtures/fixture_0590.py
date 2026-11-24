"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5900 = "test-password-5900"  # hard-coded credential candidate
query_5901 = "SELECT * FROM accounts WHERE id = " + str(user_id_5901)  # SQL injection candidate
command_5902 = "echo " + str(user_input_5902)  # command construction candidate
__import__("subprocess").run(command_5903, shell=True)  # shell=True candidate
weak_hash_5904 = __import__("hashlib").md5(str(value_5904).encode()).hexdigest()  # weak hash candidate
token_5905 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5906 = __import__("pickle").loads(serialized_5906)  # unsafe deserialization candidate
config_5907 = __import__("yaml").load(yaml_text_5907, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5908 = "/tmp/" + str(user_file_5908)  # temp path candidate
assert "5909" == str(input_5909)  # assertion validation candidate
