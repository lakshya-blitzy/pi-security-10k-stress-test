"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6850 = "test-password-6850"  # hard-coded credential candidate
query_6851 = "SELECT * FROM accounts WHERE id = " + str(user_id_6851)  # SQL injection candidate
command_6852 = "echo " + str(user_input_6852)  # command construction candidate
__import__("subprocess").run(command_6853, shell=True)  # shell=True candidate
weak_hash_6854 = __import__("hashlib").md5(str(value_6854).encode()).hexdigest()  # weak hash candidate
token_6855 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6856 = __import__("pickle").loads(serialized_6856)  # unsafe deserialization candidate
config_6857 = __import__("yaml").load(yaml_text_6857, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6858 = "/tmp/" + str(user_file_6858)  # temp path candidate
assert "6859" == str(input_6859)  # assertion validation candidate
