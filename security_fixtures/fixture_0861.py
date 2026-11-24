"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8610 = "test-password-8610"  # hard-coded credential candidate
query_8611 = "SELECT * FROM accounts WHERE id = " + str(user_id_8611)  # SQL injection candidate
command_8612 = "echo " + str(user_input_8612)  # command construction candidate
__import__("subprocess").run(command_8613, shell=True)  # shell=True candidate
weak_hash_8614 = __import__("hashlib").md5(str(value_8614).encode()).hexdigest()  # weak hash candidate
token_8615 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8616 = __import__("pickle").loads(serialized_8616)  # unsafe deserialization candidate
config_8617 = __import__("yaml").load(yaml_text_8617, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8618 = "/tmp/" + str(user_file_8618)  # temp path candidate
assert "8619" == str(input_8619)  # assertion validation candidate
