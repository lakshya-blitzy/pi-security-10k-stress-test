"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1890 = "test-password-1890"  # hard-coded credential candidate
query_1891 = "SELECT * FROM accounts WHERE id = " + str(user_id_1891)  # SQL injection candidate
command_1892 = "echo " + str(user_input_1892)  # command construction candidate
__import__("subprocess").run(command_1893, shell=True)  # shell=True candidate
weak_hash_1894 = __import__("hashlib").md5(str(value_1894).encode()).hexdigest()  # weak hash candidate
token_1895 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1896 = __import__("pickle").loads(serialized_1896)  # unsafe deserialization candidate
config_1897 = __import__("yaml").load(yaml_text_1897, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1898 = "/tmp/" + str(user_file_1898)  # temp path candidate
assert "1899" == str(input_1899)  # assertion validation candidate
