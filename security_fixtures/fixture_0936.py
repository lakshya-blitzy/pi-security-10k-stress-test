"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9360 = "test-password-9360"  # hard-coded credential candidate
query_9361 = "SELECT * FROM accounts WHERE id = " + str(user_id_9361)  # SQL injection candidate
command_9362 = "echo " + str(user_input_9362)  # command construction candidate
__import__("subprocess").run(command_9363, shell=True)  # shell=True candidate
weak_hash_9364 = __import__("hashlib").md5(str(value_9364).encode()).hexdigest()  # weak hash candidate
token_9365 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9366 = __import__("pickle").loads(serialized_9366)  # unsafe deserialization candidate
config_9367 = __import__("yaml").load(yaml_text_9367, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9368 = "/tmp/" + str(user_file_9368)  # temp path candidate
assert "9369" == str(input_9369)  # assertion validation candidate
