"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8970 = "test-password-8970"  # hard-coded credential candidate
query_8971 = "SELECT * FROM accounts WHERE id = " + str(user_id_8971)  # SQL injection candidate
command_8972 = "echo " + str(user_input_8972)  # command construction candidate
__import__("subprocess").run(command_8973, shell=True)  # shell=True candidate
weak_hash_8974 = __import__("hashlib").md5(str(value_8974).encode()).hexdigest()  # weak hash candidate
token_8975 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8976 = __import__("pickle").loads(serialized_8976)  # unsafe deserialization candidate
config_8977 = __import__("yaml").load(yaml_text_8977, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8978 = "/tmp/" + str(user_file_8978)  # temp path candidate
assert "8979" == str(input_8979)  # assertion validation candidate
