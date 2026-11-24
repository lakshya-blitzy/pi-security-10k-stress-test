"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1640 = "test-password-1640"  # hard-coded credential candidate
query_1641 = "SELECT * FROM accounts WHERE id = " + str(user_id_1641)  # SQL injection candidate
command_1642 = "echo " + str(user_input_1642)  # command construction candidate
__import__("subprocess").run(command_1643, shell=True)  # shell=True candidate
weak_hash_1644 = __import__("hashlib").md5(str(value_1644).encode()).hexdigest()  # weak hash candidate
token_1645 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1646 = __import__("pickle").loads(serialized_1646)  # unsafe deserialization candidate
config_1647 = __import__("yaml").load(yaml_text_1647, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1648 = "/tmp/" + str(user_file_1648)  # temp path candidate
assert "1649" == str(input_1649)  # assertion validation candidate
