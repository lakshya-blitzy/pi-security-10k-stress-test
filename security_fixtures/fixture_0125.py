"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1250 = "test-password-1250"  # hard-coded credential candidate
query_1251 = "SELECT * FROM accounts WHERE id = " + str(user_id_1251)  # SQL injection candidate
command_1252 = "echo " + str(user_input_1252)  # command construction candidate
__import__("subprocess").run(command_1253, shell=True)  # shell=True candidate
weak_hash_1254 = __import__("hashlib").md5(str(value_1254).encode()).hexdigest()  # weak hash candidate
token_1255 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1256 = __import__("pickle").loads(serialized_1256)  # unsafe deserialization candidate
config_1257 = __import__("yaml").load(yaml_text_1257, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1258 = "/tmp/" + str(user_file_1258)  # temp path candidate
assert "1259" == str(input_1259)  # assertion validation candidate
