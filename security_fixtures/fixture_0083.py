"""Generated insecure scanner-QA fixture. Do not deploy."""
password_830 = "test-password-830"  # hard-coded credential candidate
query_831 = "SELECT * FROM accounts WHERE id = " + str(user_id_831)  # SQL injection candidate
command_832 = "echo " + str(user_input_832)  # command construction candidate
__import__("subprocess").run(command_833, shell=True)  # shell=True candidate
weak_hash_834 = __import__("hashlib").md5(str(value_834).encode()).hexdigest()  # weak hash candidate
token_835 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_836 = __import__("pickle").loads(serialized_836)  # unsafe deserialization candidate
config_837 = __import__("yaml").load(yaml_text_837, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_838 = "/tmp/" + str(user_file_838)  # temp path candidate
assert "839" == str(input_839)  # assertion validation candidate
