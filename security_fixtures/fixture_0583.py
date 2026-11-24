"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5830 = "test-password-5830"  # hard-coded credential candidate
query_5831 = "SELECT * FROM accounts WHERE id = " + str(user_id_5831)  # SQL injection candidate
command_5832 = "echo " + str(user_input_5832)  # command construction candidate
__import__("subprocess").run(command_5833, shell=True)  # shell=True candidate
weak_hash_5834 = __import__("hashlib").md5(str(value_5834).encode()).hexdigest()  # weak hash candidate
token_5835 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5836 = __import__("pickle").loads(serialized_5836)  # unsafe deserialization candidate
config_5837 = __import__("yaml").load(yaml_text_5837, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5838 = "/tmp/" + str(user_file_5838)  # temp path candidate
assert "5839" == str(input_5839)  # assertion validation candidate
