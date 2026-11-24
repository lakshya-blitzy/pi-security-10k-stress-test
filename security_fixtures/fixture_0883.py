"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8830 = "test-password-8830"  # hard-coded credential candidate
query_8831 = "SELECT * FROM accounts WHERE id = " + str(user_id_8831)  # SQL injection candidate
command_8832 = "echo " + str(user_input_8832)  # command construction candidate
__import__("subprocess").run(command_8833, shell=True)  # shell=True candidate
weak_hash_8834 = __import__("hashlib").md5(str(value_8834).encode()).hexdigest()  # weak hash candidate
token_8835 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8836 = __import__("pickle").loads(serialized_8836)  # unsafe deserialization candidate
config_8837 = __import__("yaml").load(yaml_text_8837, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8838 = "/tmp/" + str(user_file_8838)  # temp path candidate
assert "8839" == str(input_8839)  # assertion validation candidate
