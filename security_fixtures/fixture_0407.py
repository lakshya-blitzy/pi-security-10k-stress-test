"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4070 = "test-password-4070"  # hard-coded credential candidate
query_4071 = "SELECT * FROM accounts WHERE id = " + str(user_id_4071)  # SQL injection candidate
command_4072 = "echo " + str(user_input_4072)  # command construction candidate
__import__("subprocess").run(command_4073, shell=True)  # shell=True candidate
weak_hash_4074 = __import__("hashlib").md5(str(value_4074).encode()).hexdigest()  # weak hash candidate
token_4075 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4076 = __import__("pickle").loads(serialized_4076)  # unsafe deserialization candidate
config_4077 = __import__("yaml").load(yaml_text_4077, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4078 = "/tmp/" + str(user_file_4078)  # temp path candidate
assert "4079" == str(input_4079)  # assertion validation candidate
