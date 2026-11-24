"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1350 = "test-password-1350"  # hard-coded credential candidate
query_1351 = "SELECT * FROM accounts WHERE id = " + str(user_id_1351)  # SQL injection candidate
command_1352 = "echo " + str(user_input_1352)  # command construction candidate
__import__("subprocess").run(command_1353, shell=True)  # shell=True candidate
weak_hash_1354 = __import__("hashlib").md5(str(value_1354).encode()).hexdigest()  # weak hash candidate
token_1355 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1356 = __import__("pickle").loads(serialized_1356)  # unsafe deserialization candidate
config_1357 = __import__("yaml").load(yaml_text_1357, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1358 = "/tmp/" + str(user_file_1358)  # temp path candidate
assert "1359" == str(input_1359)  # assertion validation candidate
