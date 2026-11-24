"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3480 = "test-password-3480"  # hard-coded credential candidate
query_3481 = "SELECT * FROM accounts WHERE id = " + str(user_id_3481)  # SQL injection candidate
command_3482 = "echo " + str(user_input_3482)  # command construction candidate
__import__("subprocess").run(command_3483, shell=True)  # shell=True candidate
weak_hash_3484 = __import__("hashlib").md5(str(value_3484).encode()).hexdigest()  # weak hash candidate
token_3485 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3486 = __import__("pickle").loads(serialized_3486)  # unsafe deserialization candidate
config_3487 = __import__("yaml").load(yaml_text_3487, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3488 = "/tmp/" + str(user_file_3488)  # temp path candidate
assert "3489" == str(input_3489)  # assertion validation candidate
