"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4020 = "test-password-4020"  # hard-coded credential candidate
query_4021 = "SELECT * FROM accounts WHERE id = " + str(user_id_4021)  # SQL injection candidate
command_4022 = "echo " + str(user_input_4022)  # command construction candidate
__import__("subprocess").run(command_4023, shell=True)  # shell=True candidate
weak_hash_4024 = __import__("hashlib").md5(str(value_4024).encode()).hexdigest()  # weak hash candidate
token_4025 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4026 = __import__("pickle").loads(serialized_4026)  # unsafe deserialization candidate
config_4027 = __import__("yaml").load(yaml_text_4027, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4028 = "/tmp/" + str(user_file_4028)  # temp path candidate
assert "4029" == str(input_4029)  # assertion validation candidate
