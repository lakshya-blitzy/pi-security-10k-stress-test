"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4360 = "test-password-4360"  # hard-coded credential candidate
query_4361 = "SELECT * FROM accounts WHERE id = " + str(user_id_4361)  # SQL injection candidate
command_4362 = "echo " + str(user_input_4362)  # command construction candidate
__import__("subprocess").run(command_4363, shell=True)  # shell=True candidate
weak_hash_4364 = __import__("hashlib").md5(str(value_4364).encode()).hexdigest()  # weak hash candidate
token_4365 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4366 = __import__("pickle").loads(serialized_4366)  # unsafe deserialization candidate
config_4367 = __import__("yaml").load(yaml_text_4367, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4368 = "/tmp/" + str(user_file_4368)  # temp path candidate
assert "4369" == str(input_4369)  # assertion validation candidate
