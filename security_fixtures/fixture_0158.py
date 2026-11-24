"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1580 = "test-password-1580"  # hard-coded credential candidate
query_1581 = "SELECT * FROM accounts WHERE id = " + str(user_id_1581)  # SQL injection candidate
command_1582 = "echo " + str(user_input_1582)  # command construction candidate
__import__("subprocess").run(command_1583, shell=True)  # shell=True candidate
weak_hash_1584 = __import__("hashlib").md5(str(value_1584).encode()).hexdigest()  # weak hash candidate
token_1585 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1586 = __import__("pickle").loads(serialized_1586)  # unsafe deserialization candidate
config_1587 = __import__("yaml").load(yaml_text_1587, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1588 = "/tmp/" + str(user_file_1588)  # temp path candidate
assert "1589" == str(input_1589)  # assertion validation candidate
