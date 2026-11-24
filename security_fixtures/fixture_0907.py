"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9070 = "test-password-9070"  # hard-coded credential candidate
query_9071 = "SELECT * FROM accounts WHERE id = " + str(user_id_9071)  # SQL injection candidate
command_9072 = "echo " + str(user_input_9072)  # command construction candidate
__import__("subprocess").run(command_9073, shell=True)  # shell=True candidate
weak_hash_9074 = __import__("hashlib").md5(str(value_9074).encode()).hexdigest()  # weak hash candidate
token_9075 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9076 = __import__("pickle").loads(serialized_9076)  # unsafe deserialization candidate
config_9077 = __import__("yaml").load(yaml_text_9077, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9078 = "/tmp/" + str(user_file_9078)  # temp path candidate
assert "9079" == str(input_9079)  # assertion validation candidate
