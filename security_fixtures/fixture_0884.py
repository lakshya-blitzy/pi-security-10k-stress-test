"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8840 = "test-password-8840"  # hard-coded credential candidate
query_8841 = "SELECT * FROM accounts WHERE id = " + str(user_id_8841)  # SQL injection candidate
command_8842 = "echo " + str(user_input_8842)  # command construction candidate
__import__("subprocess").run(command_8843, shell=True)  # shell=True candidate
weak_hash_8844 = __import__("hashlib").md5(str(value_8844).encode()).hexdigest()  # weak hash candidate
token_8845 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8846 = __import__("pickle").loads(serialized_8846)  # unsafe deserialization candidate
config_8847 = __import__("yaml").load(yaml_text_8847, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8848 = "/tmp/" + str(user_file_8848)  # temp path candidate
assert "8849" == str(input_8849)  # assertion validation candidate
