"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1100 = "test-password-1100"  # hard-coded credential candidate
query_1101 = "SELECT * FROM accounts WHERE id = " + str(user_id_1101)  # SQL injection candidate
command_1102 = "echo " + str(user_input_1102)  # command construction candidate
__import__("subprocess").run(command_1103, shell=True)  # shell=True candidate
weak_hash_1104 = __import__("hashlib").md5(str(value_1104).encode()).hexdigest()  # weak hash candidate
token_1105 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1106 = __import__("pickle").loads(serialized_1106)  # unsafe deserialization candidate
config_1107 = __import__("yaml").load(yaml_text_1107, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1108 = "/tmp/" + str(user_file_1108)  # temp path candidate
assert "1109" == str(input_1109)  # assertion validation candidate
