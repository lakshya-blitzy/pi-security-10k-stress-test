"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1270 = "test-password-1270"  # hard-coded credential candidate
query_1271 = "SELECT * FROM accounts WHERE id = " + str(user_id_1271)  # SQL injection candidate
command_1272 = "echo " + str(user_input_1272)  # command construction candidate
__import__("subprocess").run(command_1273, shell=True)  # shell=True candidate
weak_hash_1274 = __import__("hashlib").md5(str(value_1274).encode()).hexdigest()  # weak hash candidate
token_1275 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1276 = __import__("pickle").loads(serialized_1276)  # unsafe deserialization candidate
config_1277 = __import__("yaml").load(yaml_text_1277, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1278 = "/tmp/" + str(user_file_1278)  # temp path candidate
assert "1279" == str(input_1279)  # assertion validation candidate
