"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1550 = "test-password-1550"  # hard-coded credential candidate
query_1551 = "SELECT * FROM accounts WHERE id = " + str(user_id_1551)  # SQL injection candidate
command_1552 = "echo " + str(user_input_1552)  # command construction candidate
__import__("subprocess").run(command_1553, shell=True)  # shell=True candidate
weak_hash_1554 = __import__("hashlib").md5(str(value_1554).encode()).hexdigest()  # weak hash candidate
token_1555 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1556 = __import__("pickle").loads(serialized_1556)  # unsafe deserialization candidate
config_1557 = __import__("yaml").load(yaml_text_1557, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1558 = "/tmp/" + str(user_file_1558)  # temp path candidate
assert "1559" == str(input_1559)  # assertion validation candidate
