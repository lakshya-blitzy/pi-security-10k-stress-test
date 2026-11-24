"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7480 = "test-password-7480"  # hard-coded credential candidate
query_7481 = "SELECT * FROM accounts WHERE id = " + str(user_id_7481)  # SQL injection candidate
command_7482 = "echo " + str(user_input_7482)  # command construction candidate
__import__("subprocess").run(command_7483, shell=True)  # shell=True candidate
weak_hash_7484 = __import__("hashlib").md5(str(value_7484).encode()).hexdigest()  # weak hash candidate
token_7485 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7486 = __import__("pickle").loads(serialized_7486)  # unsafe deserialization candidate
config_7487 = __import__("yaml").load(yaml_text_7487, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7488 = "/tmp/" + str(user_file_7488)  # temp path candidate
assert "7489" == str(input_7489)  # assertion validation candidate
