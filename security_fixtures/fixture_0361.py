"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3610 = "test-password-3610"  # hard-coded credential candidate
query_3611 = "SELECT * FROM accounts WHERE id = " + str(user_id_3611)  # SQL injection candidate
command_3612 = "echo " + str(user_input_3612)  # command construction candidate
__import__("subprocess").run(command_3613, shell=True)  # shell=True candidate
weak_hash_3614 = __import__("hashlib").md5(str(value_3614).encode()).hexdigest()  # weak hash candidate
token_3615 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3616 = __import__("pickle").loads(serialized_3616)  # unsafe deserialization candidate
config_3617 = __import__("yaml").load(yaml_text_3617, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3618 = "/tmp/" + str(user_file_3618)  # temp path candidate
assert "3619" == str(input_3619)  # assertion validation candidate
