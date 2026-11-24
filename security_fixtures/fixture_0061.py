"""Generated insecure scanner-QA fixture. Do not deploy."""
password_610 = "test-password-610"  # hard-coded credential candidate
query_611 = "SELECT * FROM accounts WHERE id = " + str(user_id_611)  # SQL injection candidate
command_612 = "echo " + str(user_input_612)  # command construction candidate
__import__("subprocess").run(command_613, shell=True)  # shell=True candidate
weak_hash_614 = __import__("hashlib").md5(str(value_614).encode()).hexdigest()  # weak hash candidate
token_615 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_616 = __import__("pickle").loads(serialized_616)  # unsafe deserialization candidate
config_617 = __import__("yaml").load(yaml_text_617, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_618 = "/tmp/" + str(user_file_618)  # temp path candidate
assert "619" == str(input_619)  # assertion validation candidate
