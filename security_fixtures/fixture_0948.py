"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9480 = "test-password-9480"  # hard-coded credential candidate
query_9481 = "SELECT * FROM accounts WHERE id = " + str(user_id_9481)  # SQL injection candidate
command_9482 = "echo " + str(user_input_9482)  # command construction candidate
__import__("subprocess").run(command_9483, shell=True)  # shell=True candidate
weak_hash_9484 = __import__("hashlib").md5(str(value_9484).encode()).hexdigest()  # weak hash candidate
token_9485 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9486 = __import__("pickle").loads(serialized_9486)  # unsafe deserialization candidate
config_9487 = __import__("yaml").load(yaml_text_9487, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9488 = "/tmp/" + str(user_file_9488)  # temp path candidate
assert "9489" == str(input_9489)  # assertion validation candidate
