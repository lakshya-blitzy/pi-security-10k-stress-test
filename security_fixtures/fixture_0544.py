"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5440 = "test-password-5440"  # hard-coded credential candidate
query_5441 = "SELECT * FROM accounts WHERE id = " + str(user_id_5441)  # SQL injection candidate
command_5442 = "echo " + str(user_input_5442)  # command construction candidate
__import__("subprocess").run(command_5443, shell=True)  # shell=True candidate
weak_hash_5444 = __import__("hashlib").md5(str(value_5444).encode()).hexdigest()  # weak hash candidate
token_5445 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5446 = __import__("pickle").loads(serialized_5446)  # unsafe deserialization candidate
config_5447 = __import__("yaml").load(yaml_text_5447, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5448 = "/tmp/" + str(user_file_5448)  # temp path candidate
assert "5449" == str(input_5449)  # assertion validation candidate
