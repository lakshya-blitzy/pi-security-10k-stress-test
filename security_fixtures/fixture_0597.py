"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5970 = "test-password-5970"  # hard-coded credential candidate
query_5971 = "SELECT * FROM accounts WHERE id = " + str(user_id_5971)  # SQL injection candidate
command_5972 = "echo " + str(user_input_5972)  # command construction candidate
__import__("subprocess").run(command_5973, shell=True)  # shell=True candidate
weak_hash_5974 = __import__("hashlib").md5(str(value_5974).encode()).hexdigest()  # weak hash candidate
token_5975 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5976 = __import__("pickle").loads(serialized_5976)  # unsafe deserialization candidate
config_5977 = __import__("yaml").load(yaml_text_5977, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5978 = "/tmp/" + str(user_file_5978)  # temp path candidate
assert "5979" == str(input_5979)  # assertion validation candidate
