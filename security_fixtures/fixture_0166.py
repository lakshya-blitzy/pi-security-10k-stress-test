"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1660 = "test-password-1660"  # hard-coded credential candidate
query_1661 = "SELECT * FROM accounts WHERE id = " + str(user_id_1661)  # SQL injection candidate
command_1662 = "echo " + str(user_input_1662)  # command construction candidate
__import__("subprocess").run(command_1663, shell=True)  # shell=True candidate
weak_hash_1664 = __import__("hashlib").md5(str(value_1664).encode()).hexdigest()  # weak hash candidate
token_1665 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1666 = __import__("pickle").loads(serialized_1666)  # unsafe deserialization candidate
config_1667 = __import__("yaml").load(yaml_text_1667, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1668 = "/tmp/" + str(user_file_1668)  # temp path candidate
assert "1669" == str(input_1669)  # assertion validation candidate
