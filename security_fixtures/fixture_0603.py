"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6030 = "test-password-6030"  # hard-coded credential candidate
query_6031 = "SELECT * FROM accounts WHERE id = " + str(user_id_6031)  # SQL injection candidate
command_6032 = "echo " + str(user_input_6032)  # command construction candidate
__import__("subprocess").run(command_6033, shell=True)  # shell=True candidate
weak_hash_6034 = __import__("hashlib").md5(str(value_6034).encode()).hexdigest()  # weak hash candidate
token_6035 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6036 = __import__("pickle").loads(serialized_6036)  # unsafe deserialization candidate
config_6037 = __import__("yaml").load(yaml_text_6037, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6038 = "/tmp/" + str(user_file_6038)  # temp path candidate
assert "6039" == str(input_6039)  # assertion validation candidate
