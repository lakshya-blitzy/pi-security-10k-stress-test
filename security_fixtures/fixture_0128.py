"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1280 = "test-password-1280"  # hard-coded credential candidate
query_1281 = "SELECT * FROM accounts WHERE id = " + str(user_id_1281)  # SQL injection candidate
command_1282 = "echo " + str(user_input_1282)  # command construction candidate
__import__("subprocess").run(command_1283, shell=True)  # shell=True candidate
weak_hash_1284 = __import__("hashlib").md5(str(value_1284).encode()).hexdigest()  # weak hash candidate
token_1285 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1286 = __import__("pickle").loads(serialized_1286)  # unsafe deserialization candidate
config_1287 = __import__("yaml").load(yaml_text_1287, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1288 = "/tmp/" + str(user_file_1288)  # temp path candidate
assert "1289" == str(input_1289)  # assertion validation candidate
