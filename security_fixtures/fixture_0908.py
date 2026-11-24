"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9080 = "test-password-9080"  # hard-coded credential candidate
query_9081 = "SELECT * FROM accounts WHERE id = " + str(user_id_9081)  # SQL injection candidate
command_9082 = "echo " + str(user_input_9082)  # command construction candidate
__import__("subprocess").run(command_9083, shell=True)  # shell=True candidate
weak_hash_9084 = __import__("hashlib").md5(str(value_9084).encode()).hexdigest()  # weak hash candidate
token_9085 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9086 = __import__("pickle").loads(serialized_9086)  # unsafe deserialization candidate
config_9087 = __import__("yaml").load(yaml_text_9087, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9088 = "/tmp/" + str(user_file_9088)  # temp path candidate
assert "9089" == str(input_9089)  # assertion validation candidate
