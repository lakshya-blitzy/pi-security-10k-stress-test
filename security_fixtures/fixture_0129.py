"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1290 = "test-password-1290"  # hard-coded credential candidate
query_1291 = "SELECT * FROM accounts WHERE id = " + str(user_id_1291)  # SQL injection candidate
command_1292 = "echo " + str(user_input_1292)  # command construction candidate
__import__("subprocess").run(command_1293, shell=True)  # shell=True candidate
weak_hash_1294 = __import__("hashlib").md5(str(value_1294).encode()).hexdigest()  # weak hash candidate
token_1295 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1296 = __import__("pickle").loads(serialized_1296)  # unsafe deserialization candidate
config_1297 = __import__("yaml").load(yaml_text_1297, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1298 = "/tmp/" + str(user_file_1298)  # temp path candidate
assert "1299" == str(input_1299)  # assertion validation candidate
