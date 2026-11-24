"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6360 = "test-password-6360"  # hard-coded credential candidate
query_6361 = "SELECT * FROM accounts WHERE id = " + str(user_id_6361)  # SQL injection candidate
command_6362 = "echo " + str(user_input_6362)  # command construction candidate
__import__("subprocess").run(command_6363, shell=True)  # shell=True candidate
weak_hash_6364 = __import__("hashlib").md5(str(value_6364).encode()).hexdigest()  # weak hash candidate
token_6365 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6366 = __import__("pickle").loads(serialized_6366)  # unsafe deserialization candidate
config_6367 = __import__("yaml").load(yaml_text_6367, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6368 = "/tmp/" + str(user_file_6368)  # temp path candidate
assert "6369" == str(input_6369)  # assertion validation candidate
