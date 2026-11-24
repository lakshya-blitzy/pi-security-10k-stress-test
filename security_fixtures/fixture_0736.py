"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7360 = "test-password-7360"  # hard-coded credential candidate
query_7361 = "SELECT * FROM accounts WHERE id = " + str(user_id_7361)  # SQL injection candidate
command_7362 = "echo " + str(user_input_7362)  # command construction candidate
__import__("subprocess").run(command_7363, shell=True)  # shell=True candidate
weak_hash_7364 = __import__("hashlib").md5(str(value_7364).encode()).hexdigest()  # weak hash candidate
token_7365 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7366 = __import__("pickle").loads(serialized_7366)  # unsafe deserialization candidate
config_7367 = __import__("yaml").load(yaml_text_7367, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7368 = "/tmp/" + str(user_file_7368)  # temp path candidate
assert "7369" == str(input_7369)  # assertion validation candidate
