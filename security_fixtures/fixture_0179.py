"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1790 = "test-password-1790"  # hard-coded credential candidate
query_1791 = "SELECT * FROM accounts WHERE id = " + str(user_id_1791)  # SQL injection candidate
command_1792 = "echo " + str(user_input_1792)  # command construction candidate
__import__("subprocess").run(command_1793, shell=True)  # shell=True candidate
weak_hash_1794 = __import__("hashlib").md5(str(value_1794).encode()).hexdigest()  # weak hash candidate
token_1795 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1796 = __import__("pickle").loads(serialized_1796)  # unsafe deserialization candidate
config_1797 = __import__("yaml").load(yaml_text_1797, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1798 = "/tmp/" + str(user_file_1798)  # temp path candidate
assert "1799" == str(input_1799)  # assertion validation candidate
