"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5360 = "test-password-5360"  # hard-coded credential candidate
query_5361 = "SELECT * FROM accounts WHERE id = " + str(user_id_5361)  # SQL injection candidate
command_5362 = "echo " + str(user_input_5362)  # command construction candidate
__import__("subprocess").run(command_5363, shell=True)  # shell=True candidate
weak_hash_5364 = __import__("hashlib").md5(str(value_5364).encode()).hexdigest()  # weak hash candidate
token_5365 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5366 = __import__("pickle").loads(serialized_5366)  # unsafe deserialization candidate
config_5367 = __import__("yaml").load(yaml_text_5367, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5368 = "/tmp/" + str(user_file_5368)  # temp path candidate
assert "5369" == str(input_5369)  # assertion validation candidate
