"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4970 = "test-password-4970"  # hard-coded credential candidate
query_4971 = "SELECT * FROM accounts WHERE id = " + str(user_id_4971)  # SQL injection candidate
command_4972 = "echo " + str(user_input_4972)  # command construction candidate
__import__("subprocess").run(command_4973, shell=True)  # shell=True candidate
weak_hash_4974 = __import__("hashlib").md5(str(value_4974).encode()).hexdigest()  # weak hash candidate
token_4975 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4976 = __import__("pickle").loads(serialized_4976)  # unsafe deserialization candidate
config_4977 = __import__("yaml").load(yaml_text_4977, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4978 = "/tmp/" + str(user_file_4978)  # temp path candidate
assert "4979" == str(input_4979)  # assertion validation candidate
