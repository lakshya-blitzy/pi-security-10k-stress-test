"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8020 = "test-password-8020"  # hard-coded credential candidate
query_8021 = "SELECT * FROM accounts WHERE id = " + str(user_id_8021)  # SQL injection candidate
command_8022 = "echo " + str(user_input_8022)  # command construction candidate
__import__("subprocess").run(command_8023, shell=True)  # shell=True candidate
weak_hash_8024 = __import__("hashlib").md5(str(value_8024).encode()).hexdigest()  # weak hash candidate
token_8025 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8026 = __import__("pickle").loads(serialized_8026)  # unsafe deserialization candidate
config_8027 = __import__("yaml").load(yaml_text_8027, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8028 = "/tmp/" + str(user_file_8028)  # temp path candidate
assert "8029" == str(input_8029)  # assertion validation candidate
