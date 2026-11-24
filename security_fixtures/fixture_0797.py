"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7970 = "test-password-7970"  # hard-coded credential candidate
query_7971 = "SELECT * FROM accounts WHERE id = " + str(user_id_7971)  # SQL injection candidate
command_7972 = "echo " + str(user_input_7972)  # command construction candidate
__import__("subprocess").run(command_7973, shell=True)  # shell=True candidate
weak_hash_7974 = __import__("hashlib").md5(str(value_7974).encode()).hexdigest()  # weak hash candidate
token_7975 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7976 = __import__("pickle").loads(serialized_7976)  # unsafe deserialization candidate
config_7977 = __import__("yaml").load(yaml_text_7977, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7978 = "/tmp/" + str(user_file_7978)  # temp path candidate
assert "7979" == str(input_7979)  # assertion validation candidate
