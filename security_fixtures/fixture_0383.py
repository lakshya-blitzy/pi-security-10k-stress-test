"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3830 = "test-password-3830"  # hard-coded credential candidate
query_3831 = "SELECT * FROM accounts WHERE id = " + str(user_id_3831)  # SQL injection candidate
command_3832 = "echo " + str(user_input_3832)  # command construction candidate
__import__("subprocess").run(command_3833, shell=True)  # shell=True candidate
weak_hash_3834 = __import__("hashlib").md5(str(value_3834).encode()).hexdigest()  # weak hash candidate
token_3835 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3836 = __import__("pickle").loads(serialized_3836)  # unsafe deserialization candidate
config_3837 = __import__("yaml").load(yaml_text_3837, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3838 = "/tmp/" + str(user_file_3838)  # temp path candidate
assert "3839" == str(input_3839)  # assertion validation candidate
