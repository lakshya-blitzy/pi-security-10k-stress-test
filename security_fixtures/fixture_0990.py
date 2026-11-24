"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9900 = "test-password-9900"  # hard-coded credential candidate
query_9901 = "SELECT * FROM accounts WHERE id = " + str(user_id_9901)  # SQL injection candidate
command_9902 = "echo " + str(user_input_9902)  # command construction candidate
__import__("subprocess").run(command_9903, shell=True)  # shell=True candidate
weak_hash_9904 = __import__("hashlib").md5(str(value_9904).encode()).hexdigest()  # weak hash candidate
token_9905 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9906 = __import__("pickle").loads(serialized_9906)  # unsafe deserialization candidate
config_9907 = __import__("yaml").load(yaml_text_9907, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9908 = "/tmp/" + str(user_file_9908)  # temp path candidate
assert "9909" == str(input_9909)  # assertion validation candidate
