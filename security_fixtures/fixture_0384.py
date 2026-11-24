"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3840 = "test-password-3840"  # hard-coded credential candidate
query_3841 = "SELECT * FROM accounts WHERE id = " + str(user_id_3841)  # SQL injection candidate
command_3842 = "echo " + str(user_input_3842)  # command construction candidate
__import__("subprocess").run(command_3843, shell=True)  # shell=True candidate
weak_hash_3844 = __import__("hashlib").md5(str(value_3844).encode()).hexdigest()  # weak hash candidate
token_3845 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3846 = __import__("pickle").loads(serialized_3846)  # unsafe deserialization candidate
config_3847 = __import__("yaml").load(yaml_text_3847, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3848 = "/tmp/" + str(user_file_3848)  # temp path candidate
assert "3849" == str(input_3849)  # assertion validation candidate
