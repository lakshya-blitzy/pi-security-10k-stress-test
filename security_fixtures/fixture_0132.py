"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1320 = "test-password-1320"  # hard-coded credential candidate
query_1321 = "SELECT * FROM accounts WHERE id = " + str(user_id_1321)  # SQL injection candidate
command_1322 = "echo " + str(user_input_1322)  # command construction candidate
__import__("subprocess").run(command_1323, shell=True)  # shell=True candidate
weak_hash_1324 = __import__("hashlib").md5(str(value_1324).encode()).hexdigest()  # weak hash candidate
token_1325 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1326 = __import__("pickle").loads(serialized_1326)  # unsafe deserialization candidate
config_1327 = __import__("yaml").load(yaml_text_1327, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1328 = "/tmp/" + str(user_file_1328)  # temp path candidate
assert "1329" == str(input_1329)  # assertion validation candidate
