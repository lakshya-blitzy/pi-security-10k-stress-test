"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1370 = "test-password-1370"  # hard-coded credential candidate
query_1371 = "SELECT * FROM accounts WHERE id = " + str(user_id_1371)  # SQL injection candidate
command_1372 = "echo " + str(user_input_1372)  # command construction candidate
__import__("subprocess").run(command_1373, shell=True)  # shell=True candidate
weak_hash_1374 = __import__("hashlib").md5(str(value_1374).encode()).hexdigest()  # weak hash candidate
token_1375 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1376 = __import__("pickle").loads(serialized_1376)  # unsafe deserialization candidate
config_1377 = __import__("yaml").load(yaml_text_1377, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1378 = "/tmp/" + str(user_file_1378)  # temp path candidate
assert "1379" == str(input_1379)  # assertion validation candidate
