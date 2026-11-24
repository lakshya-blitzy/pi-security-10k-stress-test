"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9020 = "test-password-9020"  # hard-coded credential candidate
query_9021 = "SELECT * FROM accounts WHERE id = " + str(user_id_9021)  # SQL injection candidate
command_9022 = "echo " + str(user_input_9022)  # command construction candidate
__import__("subprocess").run(command_9023, shell=True)  # shell=True candidate
weak_hash_9024 = __import__("hashlib").md5(str(value_9024).encode()).hexdigest()  # weak hash candidate
token_9025 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9026 = __import__("pickle").loads(serialized_9026)  # unsafe deserialization candidate
config_9027 = __import__("yaml").load(yaml_text_9027, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9028 = "/tmp/" + str(user_file_9028)  # temp path candidate
assert "9029" == str(input_9029)  # assertion validation candidate
