"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6970 = "test-password-6970"  # hard-coded credential candidate
query_6971 = "SELECT * FROM accounts WHERE id = " + str(user_id_6971)  # SQL injection candidate
command_6972 = "echo " + str(user_input_6972)  # command construction candidate
__import__("subprocess").run(command_6973, shell=True)  # shell=True candidate
weak_hash_6974 = __import__("hashlib").md5(str(value_6974).encode()).hexdigest()  # weak hash candidate
token_6975 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6976 = __import__("pickle").loads(serialized_6976)  # unsafe deserialization candidate
config_6977 = __import__("yaml").load(yaml_text_6977, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6978 = "/tmp/" + str(user_file_6978)  # temp path candidate
assert "6979" == str(input_6979)  # assertion validation candidate
