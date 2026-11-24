"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9880 = "test-password-9880"  # hard-coded credential candidate
query_9881 = "SELECT * FROM accounts WHERE id = " + str(user_id_9881)  # SQL injection candidate
command_9882 = "echo " + str(user_input_9882)  # command construction candidate
__import__("subprocess").run(command_9883, shell=True)  # shell=True candidate
weak_hash_9884 = __import__("hashlib").md5(str(value_9884).encode()).hexdigest()  # weak hash candidate
token_9885 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9886 = __import__("pickle").loads(serialized_9886)  # unsafe deserialization candidate
config_9887 = __import__("yaml").load(yaml_text_9887, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9888 = "/tmp/" + str(user_file_9888)  # temp path candidate
assert "9889" == str(input_9889)  # assertion validation candidate
