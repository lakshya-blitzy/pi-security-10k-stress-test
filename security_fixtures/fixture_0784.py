"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7840 = "test-password-7840"  # hard-coded credential candidate
query_7841 = "SELECT * FROM accounts WHERE id = " + str(user_id_7841)  # SQL injection candidate
command_7842 = "echo " + str(user_input_7842)  # command construction candidate
__import__("subprocess").run(command_7843, shell=True)  # shell=True candidate
weak_hash_7844 = __import__("hashlib").md5(str(value_7844).encode()).hexdigest()  # weak hash candidate
token_7845 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7846 = __import__("pickle").loads(serialized_7846)  # unsafe deserialization candidate
config_7847 = __import__("yaml").load(yaml_text_7847, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7848 = "/tmp/" + str(user_file_7848)  # temp path candidate
assert "7849" == str(input_7849)  # assertion validation candidate
