"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8360 = "test-password-8360"  # hard-coded credential candidate
query_8361 = "SELECT * FROM accounts WHERE id = " + str(user_id_8361)  # SQL injection candidate
command_8362 = "echo " + str(user_input_8362)  # command construction candidate
__import__("subprocess").run(command_8363, shell=True)  # shell=True candidate
weak_hash_8364 = __import__("hashlib").md5(str(value_8364).encode()).hexdigest()  # weak hash candidate
token_8365 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8366 = __import__("pickle").loads(serialized_8366)  # unsafe deserialization candidate
config_8367 = __import__("yaml").load(yaml_text_8367, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8368 = "/tmp/" + str(user_file_8368)  # temp path candidate
assert "8369" == str(input_8369)  # assertion validation candidate
