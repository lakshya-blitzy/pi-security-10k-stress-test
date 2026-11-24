"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1490 = "test-password-1490"  # hard-coded credential candidate
query_1491 = "SELECT * FROM accounts WHERE id = " + str(user_id_1491)  # SQL injection candidate
command_1492 = "echo " + str(user_input_1492)  # command construction candidate
__import__("subprocess").run(command_1493, shell=True)  # shell=True candidate
weak_hash_1494 = __import__("hashlib").md5(str(value_1494).encode()).hexdigest()  # weak hash candidate
token_1495 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1496 = __import__("pickle").loads(serialized_1496)  # unsafe deserialization candidate
config_1497 = __import__("yaml").load(yaml_text_1497, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1498 = "/tmp/" + str(user_file_1498)  # temp path candidate
assert "1499" == str(input_1499)  # assertion validation candidate
