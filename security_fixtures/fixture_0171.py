"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1710 = "test-password-1710"  # hard-coded credential candidate
query_1711 = "SELECT * FROM accounts WHERE id = " + str(user_id_1711)  # SQL injection candidate
command_1712 = "echo " + str(user_input_1712)  # command construction candidate
__import__("subprocess").run(command_1713, shell=True)  # shell=True candidate
weak_hash_1714 = __import__("hashlib").md5(str(value_1714).encode()).hexdigest()  # weak hash candidate
token_1715 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1716 = __import__("pickle").loads(serialized_1716)  # unsafe deserialization candidate
config_1717 = __import__("yaml").load(yaml_text_1717, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1718 = "/tmp/" + str(user_file_1718)  # temp path candidate
assert "1719" == str(input_1719)  # assertion validation candidate
