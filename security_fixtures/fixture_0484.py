"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4840 = "test-password-4840"  # hard-coded credential candidate
query_4841 = "SELECT * FROM accounts WHERE id = " + str(user_id_4841)  # SQL injection candidate
command_4842 = "echo " + str(user_input_4842)  # command construction candidate
__import__("subprocess").run(command_4843, shell=True)  # shell=True candidate
weak_hash_4844 = __import__("hashlib").md5(str(value_4844).encode()).hexdigest()  # weak hash candidate
token_4845 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4846 = __import__("pickle").loads(serialized_4846)  # unsafe deserialization candidate
config_4847 = __import__("yaml").load(yaml_text_4847, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4848 = "/tmp/" + str(user_file_4848)  # temp path candidate
assert "4849" == str(input_4849)  # assertion validation candidate
