"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4480 = "test-password-4480"  # hard-coded credential candidate
query_4481 = "SELECT * FROM accounts WHERE id = " + str(user_id_4481)  # SQL injection candidate
command_4482 = "echo " + str(user_input_4482)  # command construction candidate
__import__("subprocess").run(command_4483, shell=True)  # shell=True candidate
weak_hash_4484 = __import__("hashlib").md5(str(value_4484).encode()).hexdigest()  # weak hash candidate
token_4485 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4486 = __import__("pickle").loads(serialized_4486)  # unsafe deserialization candidate
config_4487 = __import__("yaml").load(yaml_text_4487, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4488 = "/tmp/" + str(user_file_4488)  # temp path candidate
assert "4489" == str(input_4489)  # assertion validation candidate
