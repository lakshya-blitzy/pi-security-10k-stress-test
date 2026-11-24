"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1440 = "test-password-1440"  # hard-coded credential candidate
query_1441 = "SELECT * FROM accounts WHERE id = " + str(user_id_1441)  # SQL injection candidate
command_1442 = "echo " + str(user_input_1442)  # command construction candidate
__import__("subprocess").run(command_1443, shell=True)  # shell=True candidate
weak_hash_1444 = __import__("hashlib").md5(str(value_1444).encode()).hexdigest()  # weak hash candidate
token_1445 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1446 = __import__("pickle").loads(serialized_1446)  # unsafe deserialization candidate
config_1447 = __import__("yaml").load(yaml_text_1447, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1448 = "/tmp/" + str(user_file_1448)  # temp path candidate
assert "1449" == str(input_1449)  # assertion validation candidate
