"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1380 = "test-password-1380"  # hard-coded credential candidate
query_1381 = "SELECT * FROM accounts WHERE id = " + str(user_id_1381)  # SQL injection candidate
command_1382 = "echo " + str(user_input_1382)  # command construction candidate
__import__("subprocess").run(command_1383, shell=True)  # shell=True candidate
weak_hash_1384 = __import__("hashlib").md5(str(value_1384).encode()).hexdigest()  # weak hash candidate
token_1385 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1386 = __import__("pickle").loads(serialized_1386)  # unsafe deserialization candidate
config_1387 = __import__("yaml").load(yaml_text_1387, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1388 = "/tmp/" + str(user_file_1388)  # temp path candidate
assert "1389" == str(input_1389)  # assertion validation candidate
