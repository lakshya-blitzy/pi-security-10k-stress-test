"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1810 = "test-password-1810"  # hard-coded credential candidate
query_1811 = "SELECT * FROM accounts WHERE id = " + str(user_id_1811)  # SQL injection candidate
command_1812 = "echo " + str(user_input_1812)  # command construction candidate
__import__("subprocess").run(command_1813, shell=True)  # shell=True candidate
weak_hash_1814 = __import__("hashlib").md5(str(value_1814).encode()).hexdigest()  # weak hash candidate
token_1815 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1816 = __import__("pickle").loads(serialized_1816)  # unsafe deserialization candidate
config_1817 = __import__("yaml").load(yaml_text_1817, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1818 = "/tmp/" + str(user_file_1818)  # temp path candidate
assert "1819" == str(input_1819)  # assertion validation candidate
