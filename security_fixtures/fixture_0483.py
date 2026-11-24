"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4830 = "test-password-4830"  # hard-coded credential candidate
query_4831 = "SELECT * FROM accounts WHERE id = " + str(user_id_4831)  # SQL injection candidate
command_4832 = "echo " + str(user_input_4832)  # command construction candidate
__import__("subprocess").run(command_4833, shell=True)  # shell=True candidate
weak_hash_4834 = __import__("hashlib").md5(str(value_4834).encode()).hexdigest()  # weak hash candidate
token_4835 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4836 = __import__("pickle").loads(serialized_4836)  # unsafe deserialization candidate
config_4837 = __import__("yaml").load(yaml_text_4837, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4838 = "/tmp/" + str(user_file_4838)  # temp path candidate
assert "4839" == str(input_4839)  # assertion validation candidate
