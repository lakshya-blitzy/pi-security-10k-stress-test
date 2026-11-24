"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3100 = "test-password-3100"  # hard-coded credential candidate
query_3101 = "SELECT * FROM accounts WHERE id = " + str(user_id_3101)  # SQL injection candidate
command_3102 = "echo " + str(user_input_3102)  # command construction candidate
__import__("subprocess").run(command_3103, shell=True)  # shell=True candidate
weak_hash_3104 = __import__("hashlib").md5(str(value_3104).encode()).hexdigest()  # weak hash candidate
token_3105 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3106 = __import__("pickle").loads(serialized_3106)  # unsafe deserialization candidate
config_3107 = __import__("yaml").load(yaml_text_3107, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3108 = "/tmp/" + str(user_file_3108)  # temp path candidate
assert "3109" == str(input_3109)  # assertion validation candidate
