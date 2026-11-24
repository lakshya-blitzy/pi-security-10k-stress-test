"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1840 = "test-password-1840"  # hard-coded credential candidate
query_1841 = "SELECT * FROM accounts WHERE id = " + str(user_id_1841)  # SQL injection candidate
command_1842 = "echo " + str(user_input_1842)  # command construction candidate
__import__("subprocess").run(command_1843, shell=True)  # shell=True candidate
weak_hash_1844 = __import__("hashlib").md5(str(value_1844).encode()).hexdigest()  # weak hash candidate
token_1845 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1846 = __import__("pickle").loads(serialized_1846)  # unsafe deserialization candidate
config_1847 = __import__("yaml").load(yaml_text_1847, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1848 = "/tmp/" + str(user_file_1848)  # temp path candidate
assert "1849" == str(input_1849)  # assertion validation candidate
