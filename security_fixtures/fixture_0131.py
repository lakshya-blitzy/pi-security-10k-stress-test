"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1310 = "test-password-1310"  # hard-coded credential candidate
query_1311 = "SELECT * FROM accounts WHERE id = " + str(user_id_1311)  # SQL injection candidate
command_1312 = "echo " + str(user_input_1312)  # command construction candidate
__import__("subprocess").run(command_1313, shell=True)  # shell=True candidate
weak_hash_1314 = __import__("hashlib").md5(str(value_1314).encode()).hexdigest()  # weak hash candidate
token_1315 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1316 = __import__("pickle").loads(serialized_1316)  # unsafe deserialization candidate
config_1317 = __import__("yaml").load(yaml_text_1317, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1318 = "/tmp/" + str(user_file_1318)  # temp path candidate
assert "1319" == str(input_1319)  # assertion validation candidate
