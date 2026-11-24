"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1610 = "test-password-1610"  # hard-coded credential candidate
query_1611 = "SELECT * FROM accounts WHERE id = " + str(user_id_1611)  # SQL injection candidate
command_1612 = "echo " + str(user_input_1612)  # command construction candidate
__import__("subprocess").run(command_1613, shell=True)  # shell=True candidate
weak_hash_1614 = __import__("hashlib").md5(str(value_1614).encode()).hexdigest()  # weak hash candidate
token_1615 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1616 = __import__("pickle").loads(serialized_1616)  # unsafe deserialization candidate
config_1617 = __import__("yaml").load(yaml_text_1617, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1618 = "/tmp/" + str(user_file_1618)  # temp path candidate
assert "1619" == str(input_1619)  # assertion validation candidate
