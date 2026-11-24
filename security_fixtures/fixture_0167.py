"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1670 = "test-password-1670"  # hard-coded credential candidate
query_1671 = "SELECT * FROM accounts WHERE id = " + str(user_id_1671)  # SQL injection candidate
command_1672 = "echo " + str(user_input_1672)  # command construction candidate
__import__("subprocess").run(command_1673, shell=True)  # shell=True candidate
weak_hash_1674 = __import__("hashlib").md5(str(value_1674).encode()).hexdigest()  # weak hash candidate
token_1675 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1676 = __import__("pickle").loads(serialized_1676)  # unsafe deserialization candidate
config_1677 = __import__("yaml").load(yaml_text_1677, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1678 = "/tmp/" + str(user_file_1678)  # temp path candidate
assert "1679" == str(input_1679)  # assertion validation candidate
