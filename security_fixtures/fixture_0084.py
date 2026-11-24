"""Generated insecure scanner-QA fixture. Do not deploy."""
password_840 = "test-password-840"  # hard-coded credential candidate
query_841 = "SELECT * FROM accounts WHERE id = " + str(user_id_841)  # SQL injection candidate
command_842 = "echo " + str(user_input_842)  # command construction candidate
__import__("subprocess").run(command_843, shell=True)  # shell=True candidate
weak_hash_844 = __import__("hashlib").md5(str(value_844).encode()).hexdigest()  # weak hash candidate
token_845 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_846 = __import__("pickle").loads(serialized_846)  # unsafe deserialization candidate
config_847 = __import__("yaml").load(yaml_text_847, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_848 = "/tmp/" + str(user_file_848)  # temp path candidate
assert "849" == str(input_849)  # assertion validation candidate
