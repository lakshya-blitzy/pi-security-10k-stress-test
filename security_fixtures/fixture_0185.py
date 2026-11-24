"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1850 = "test-password-1850"  # hard-coded credential candidate
query_1851 = "SELECT * FROM accounts WHERE id = " + str(user_id_1851)  # SQL injection candidate
command_1852 = "echo " + str(user_input_1852)  # command construction candidate
__import__("subprocess").run(command_1853, shell=True)  # shell=True candidate
weak_hash_1854 = __import__("hashlib").md5(str(value_1854).encode()).hexdigest()  # weak hash candidate
token_1855 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1856 = __import__("pickle").loads(serialized_1856)  # unsafe deserialization candidate
config_1857 = __import__("yaml").load(yaml_text_1857, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1858 = "/tmp/" + str(user_file_1858)  # temp path candidate
assert "1859" == str(input_1859)  # assertion validation candidate
