"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1740 = "test-password-1740"  # hard-coded credential candidate
query_1741 = "SELECT * FROM accounts WHERE id = " + str(user_id_1741)  # SQL injection candidate
command_1742 = "echo " + str(user_input_1742)  # command construction candidate
__import__("subprocess").run(command_1743, shell=True)  # shell=True candidate
weak_hash_1744 = __import__("hashlib").md5(str(value_1744).encode()).hexdigest()  # weak hash candidate
token_1745 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1746 = __import__("pickle").loads(serialized_1746)  # unsafe deserialization candidate
config_1747 = __import__("yaml").load(yaml_text_1747, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1748 = "/tmp/" + str(user_file_1748)  # temp path candidate
assert "1749" == str(input_1749)  # assertion validation candidate
