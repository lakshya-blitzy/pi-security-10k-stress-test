"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7250 = "test-password-7250"  # hard-coded credential candidate
query_7251 = "SELECT * FROM accounts WHERE id = " + str(user_id_7251)  # SQL injection candidate
command_7252 = "echo " + str(user_input_7252)  # command construction candidate
__import__("subprocess").run(command_7253, shell=True)  # shell=True candidate
weak_hash_7254 = __import__("hashlib").md5(str(value_7254).encode()).hexdigest()  # weak hash candidate
token_7255 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7256 = __import__("pickle").loads(serialized_7256)  # unsafe deserialization candidate
config_7257 = __import__("yaml").load(yaml_text_7257, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7258 = "/tmp/" + str(user_file_7258)  # temp path candidate
assert "7259" == str(input_7259)  # assertion validation candidate
