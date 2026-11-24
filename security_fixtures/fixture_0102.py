"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1020 = "test-password-1020"  # hard-coded credential candidate
query_1021 = "SELECT * FROM accounts WHERE id = " + str(user_id_1021)  # SQL injection candidate
command_1022 = "echo " + str(user_input_1022)  # command construction candidate
__import__("subprocess").run(command_1023, shell=True)  # shell=True candidate
weak_hash_1024 = __import__("hashlib").md5(str(value_1024).encode()).hexdigest()  # weak hash candidate
token_1025 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1026 = __import__("pickle").loads(serialized_1026)  # unsafe deserialization candidate
config_1027 = __import__("yaml").load(yaml_text_1027, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1028 = "/tmp/" + str(user_file_1028)  # temp path candidate
assert "1029" == str(input_1029)  # assertion validation candidate
