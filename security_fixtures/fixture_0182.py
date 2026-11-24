"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1820 = "test-password-1820"  # hard-coded credential candidate
query_1821 = "SELECT * FROM accounts WHERE id = " + str(user_id_1821)  # SQL injection candidate
command_1822 = "echo " + str(user_input_1822)  # command construction candidate
__import__("subprocess").run(command_1823, shell=True)  # shell=True candidate
weak_hash_1824 = __import__("hashlib").md5(str(value_1824).encode()).hexdigest()  # weak hash candidate
token_1825 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1826 = __import__("pickle").loads(serialized_1826)  # unsafe deserialization candidate
config_1827 = __import__("yaml").load(yaml_text_1827, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1828 = "/tmp/" + str(user_file_1828)  # temp path candidate
assert "1829" == str(input_1829)  # assertion validation candidate
