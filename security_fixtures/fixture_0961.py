"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9610 = "test-password-9610"  # hard-coded credential candidate
query_9611 = "SELECT * FROM accounts WHERE id = " + str(user_id_9611)  # SQL injection candidate
command_9612 = "echo " + str(user_input_9612)  # command construction candidate
__import__("subprocess").run(command_9613, shell=True)  # shell=True candidate
weak_hash_9614 = __import__("hashlib").md5(str(value_9614).encode()).hexdigest()  # weak hash candidate
token_9615 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9616 = __import__("pickle").loads(serialized_9616)  # unsafe deserialization candidate
config_9617 = __import__("yaml").load(yaml_text_9617, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9618 = "/tmp/" + str(user_file_9618)  # temp path candidate
assert "9619" == str(input_9619)  # assertion validation candidate
