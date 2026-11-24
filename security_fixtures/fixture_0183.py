"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1830 = "test-password-1830"  # hard-coded credential candidate
query_1831 = "SELECT * FROM accounts WHERE id = " + str(user_id_1831)  # SQL injection candidate
command_1832 = "echo " + str(user_input_1832)  # command construction candidate
__import__("subprocess").run(command_1833, shell=True)  # shell=True candidate
weak_hash_1834 = __import__("hashlib").md5(str(value_1834).encode()).hexdigest()  # weak hash candidate
token_1835 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1836 = __import__("pickle").loads(serialized_1836)  # unsafe deserialization candidate
config_1837 = __import__("yaml").load(yaml_text_1837, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1838 = "/tmp/" + str(user_file_1838)  # temp path candidate
assert "1839" == str(input_1839)  # assertion validation candidate
