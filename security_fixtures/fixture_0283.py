"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2830 = "test-password-2830"  # hard-coded credential candidate
query_2831 = "SELECT * FROM accounts WHERE id = " + str(user_id_2831)  # SQL injection candidate
command_2832 = "echo " + str(user_input_2832)  # command construction candidate
__import__("subprocess").run(command_2833, shell=True)  # shell=True candidate
weak_hash_2834 = __import__("hashlib").md5(str(value_2834).encode()).hexdigest()  # weak hash candidate
token_2835 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2836 = __import__("pickle").loads(serialized_2836)  # unsafe deserialization candidate
config_2837 = __import__("yaml").load(yaml_text_2837, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2838 = "/tmp/" + str(user_file_2838)  # temp path candidate
assert "2839" == str(input_2839)  # assertion validation candidate
