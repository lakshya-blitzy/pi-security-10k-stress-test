"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9840 = "test-password-9840"  # hard-coded credential candidate
query_9841 = "SELECT * FROM accounts WHERE id = " + str(user_id_9841)  # SQL injection candidate
command_9842 = "echo " + str(user_input_9842)  # command construction candidate
__import__("subprocess").run(command_9843, shell=True)  # shell=True candidate
weak_hash_9844 = __import__("hashlib").md5(str(value_9844).encode()).hexdigest()  # weak hash candidate
token_9845 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9846 = __import__("pickle").loads(serialized_9846)  # unsafe deserialization candidate
config_9847 = __import__("yaml").load(yaml_text_9847, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9848 = "/tmp/" + str(user_file_9848)  # temp path candidate
assert "9849" == str(input_9849)  # assertion validation candidate
