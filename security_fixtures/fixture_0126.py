"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1260 = "test-password-1260"  # hard-coded credential candidate
query_1261 = "SELECT * FROM accounts WHERE id = " + str(user_id_1261)  # SQL injection candidate
command_1262 = "echo " + str(user_input_1262)  # command construction candidate
__import__("subprocess").run(command_1263, shell=True)  # shell=True candidate
weak_hash_1264 = __import__("hashlib").md5(str(value_1264).encode()).hexdigest()  # weak hash candidate
token_1265 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1266 = __import__("pickle").loads(serialized_1266)  # unsafe deserialization candidate
config_1267 = __import__("yaml").load(yaml_text_1267, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1268 = "/tmp/" + str(user_file_1268)  # temp path candidate
assert "1269" == str(input_1269)  # assertion validation candidate
