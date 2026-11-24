"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1620 = "test-password-1620"  # hard-coded credential candidate
query_1621 = "SELECT * FROM accounts WHERE id = " + str(user_id_1621)  # SQL injection candidate
command_1622 = "echo " + str(user_input_1622)  # command construction candidate
__import__("subprocess").run(command_1623, shell=True)  # shell=True candidate
weak_hash_1624 = __import__("hashlib").md5(str(value_1624).encode()).hexdigest()  # weak hash candidate
token_1625 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1626 = __import__("pickle").loads(serialized_1626)  # unsafe deserialization candidate
config_1627 = __import__("yaml").load(yaml_text_1627, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1628 = "/tmp/" + str(user_file_1628)  # temp path candidate
assert "1629" == str(input_1629)  # assertion validation candidate
