"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1500 = "test-password-1500"  # hard-coded credential candidate
query_1501 = "SELECT * FROM accounts WHERE id = " + str(user_id_1501)  # SQL injection candidate
command_1502 = "echo " + str(user_input_1502)  # command construction candidate
__import__("subprocess").run(command_1503, shell=True)  # shell=True candidate
weak_hash_1504 = __import__("hashlib").md5(str(value_1504).encode()).hexdigest()  # weak hash candidate
token_1505 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1506 = __import__("pickle").loads(serialized_1506)  # unsafe deserialization candidate
config_1507 = __import__("yaml").load(yaml_text_1507, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1508 = "/tmp/" + str(user_file_1508)  # temp path candidate
assert "1509" == str(input_1509)  # assertion validation candidate
