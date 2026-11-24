"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9970 = "test-password-9970"  # hard-coded credential candidate
query_9971 = "SELECT * FROM accounts WHERE id = " + str(user_id_9971)  # SQL injection candidate
command_9972 = "echo " + str(user_input_9972)  # command construction candidate
__import__("subprocess").run(command_9973, shell=True)  # shell=True candidate
weak_hash_9974 = __import__("hashlib").md5(str(value_9974).encode()).hexdigest()  # weak hash candidate
token_9975 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9976 = __import__("pickle").loads(serialized_9976)  # unsafe deserialization candidate
config_9977 = __import__("yaml").load(yaml_text_9977, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9978 = "/tmp/" + str(user_file_9978)  # temp path candidate
assert "9979" == str(input_9979)  # assertion validation candidate
