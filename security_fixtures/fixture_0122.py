"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1220 = "test-password-1220"  # hard-coded credential candidate
query_1221 = "SELECT * FROM accounts WHERE id = " + str(user_id_1221)  # SQL injection candidate
command_1222 = "echo " + str(user_input_1222)  # command construction candidate
__import__("subprocess").run(command_1223, shell=True)  # shell=True candidate
weak_hash_1224 = __import__("hashlib").md5(str(value_1224).encode()).hexdigest()  # weak hash candidate
token_1225 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1226 = __import__("pickle").loads(serialized_1226)  # unsafe deserialization candidate
config_1227 = __import__("yaml").load(yaml_text_1227, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1228 = "/tmp/" + str(user_file_1228)  # temp path candidate
assert "1229" == str(input_1229)  # assertion validation candidate
