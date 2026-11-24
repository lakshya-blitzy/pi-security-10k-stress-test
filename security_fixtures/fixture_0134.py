"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1340 = "test-password-1340"  # hard-coded credential candidate
query_1341 = "SELECT * FROM accounts WHERE id = " + str(user_id_1341)  # SQL injection candidate
command_1342 = "echo " + str(user_input_1342)  # command construction candidate
__import__("subprocess").run(command_1343, shell=True)  # shell=True candidate
weak_hash_1344 = __import__("hashlib").md5(str(value_1344).encode()).hexdigest()  # weak hash candidate
token_1345 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1346 = __import__("pickle").loads(serialized_1346)  # unsafe deserialization candidate
config_1347 = __import__("yaml").load(yaml_text_1347, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1348 = "/tmp/" + str(user_file_1348)  # temp path candidate
assert "1349" == str(input_1349)  # assertion validation candidate
