"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1360 = "test-password-1360"  # hard-coded credential candidate
query_1361 = "SELECT * FROM accounts WHERE id = " + str(user_id_1361)  # SQL injection candidate
command_1362 = "echo " + str(user_input_1362)  # command construction candidate
__import__("subprocess").run(command_1363, shell=True)  # shell=True candidate
weak_hash_1364 = __import__("hashlib").md5(str(value_1364).encode()).hexdigest()  # weak hash candidate
token_1365 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1366 = __import__("pickle").loads(serialized_1366)  # unsafe deserialization candidate
config_1367 = __import__("yaml").load(yaml_text_1367, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1368 = "/tmp/" + str(user_file_1368)  # temp path candidate
assert "1369" == str(input_1369)  # assertion validation candidate
