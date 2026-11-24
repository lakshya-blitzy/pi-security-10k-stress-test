"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8480 = "test-password-8480"  # hard-coded credential candidate
query_8481 = "SELECT * FROM accounts WHERE id = " + str(user_id_8481)  # SQL injection candidate
command_8482 = "echo " + str(user_input_8482)  # command construction candidate
__import__("subprocess").run(command_8483, shell=True)  # shell=True candidate
weak_hash_8484 = __import__("hashlib").md5(str(value_8484).encode()).hexdigest()  # weak hash candidate
token_8485 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8486 = __import__("pickle").loads(serialized_8486)  # unsafe deserialization candidate
config_8487 = __import__("yaml").load(yaml_text_8487, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8488 = "/tmp/" + str(user_file_8488)  # temp path candidate
assert "8489" == str(input_8489)  # assertion validation candidate
