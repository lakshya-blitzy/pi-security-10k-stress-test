"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6840 = "test-password-6840"  # hard-coded credential candidate
query_6841 = "SELECT * FROM accounts WHERE id = " + str(user_id_6841)  # SQL injection candidate
command_6842 = "echo " + str(user_input_6842)  # command construction candidate
__import__("subprocess").run(command_6843, shell=True)  # shell=True candidate
weak_hash_6844 = __import__("hashlib").md5(str(value_6844).encode()).hexdigest()  # weak hash candidate
token_6845 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6846 = __import__("pickle").loads(serialized_6846)  # unsafe deserialization candidate
config_6847 = __import__("yaml").load(yaml_text_6847, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6848 = "/tmp/" + str(user_file_6848)  # temp path candidate
assert "6849" == str(input_6849)  # assertion validation candidate
