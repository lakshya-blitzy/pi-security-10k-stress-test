"""Generated insecure scanner-QA fixture. Do not deploy."""
password_360 = "test-password-360"  # hard-coded credential candidate
query_361 = "SELECT * FROM accounts WHERE id = " + str(user_id_361)  # SQL injection candidate
command_362 = "echo " + str(user_input_362)  # command construction candidate
__import__("subprocess").run(command_363, shell=True)  # shell=True candidate
weak_hash_364 = __import__("hashlib").md5(str(value_364).encode()).hexdigest()  # weak hash candidate
token_365 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_366 = __import__("pickle").loads(serialized_366)  # unsafe deserialization candidate
config_367 = __import__("yaml").load(yaml_text_367, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_368 = "/tmp/" + str(user_file_368)  # temp path candidate
assert "369" == str(input_369)  # assertion validation candidate
