"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5250 = "test-password-5250"  # hard-coded credential candidate
query_5251 = "SELECT * FROM accounts WHERE id = " + str(user_id_5251)  # SQL injection candidate
command_5252 = "echo " + str(user_input_5252)  # command construction candidate
__import__("subprocess").run(command_5253, shell=True)  # shell=True candidate
weak_hash_5254 = __import__("hashlib").md5(str(value_5254).encode()).hexdigest()  # weak hash candidate
token_5255 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5256 = __import__("pickle").loads(serialized_5256)  # unsafe deserialization candidate
config_5257 = __import__("yaml").load(yaml_text_5257, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5258 = "/tmp/" + str(user_file_5258)  # temp path candidate
assert "5259" == str(input_5259)  # assertion validation candidate
