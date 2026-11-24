"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6480 = "test-password-6480"  # hard-coded credential candidate
query_6481 = "SELECT * FROM accounts WHERE id = " + str(user_id_6481)  # SQL injection candidate
command_6482 = "echo " + str(user_input_6482)  # command construction candidate
__import__("subprocess").run(command_6483, shell=True)  # shell=True candidate
weak_hash_6484 = __import__("hashlib").md5(str(value_6484).encode()).hexdigest()  # weak hash candidate
token_6485 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6486 = __import__("pickle").loads(serialized_6486)  # unsafe deserialization candidate
config_6487 = __import__("yaml").load(yaml_text_6487, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6488 = "/tmp/" + str(user_file_6488)  # temp path candidate
assert "6489" == str(input_6489)  # assertion validation candidate
