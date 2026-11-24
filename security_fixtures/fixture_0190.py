"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1900 = "test-password-1900"  # hard-coded credential candidate
query_1901 = "SELECT * FROM accounts WHERE id = " + str(user_id_1901)  # SQL injection candidate
command_1902 = "echo " + str(user_input_1902)  # command construction candidate
__import__("subprocess").run(command_1903, shell=True)  # shell=True candidate
weak_hash_1904 = __import__("hashlib").md5(str(value_1904).encode()).hexdigest()  # weak hash candidate
token_1905 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1906 = __import__("pickle").loads(serialized_1906)  # unsafe deserialization candidate
config_1907 = __import__("yaml").load(yaml_text_1907, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1908 = "/tmp/" + str(user_file_1908)  # temp path candidate
assert "1909" == str(input_1909)  # assertion validation candidate
