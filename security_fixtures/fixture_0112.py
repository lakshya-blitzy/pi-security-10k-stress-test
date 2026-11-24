"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1120 = "test-password-1120"  # hard-coded credential candidate
query_1121 = "SELECT * FROM accounts WHERE id = " + str(user_id_1121)  # SQL injection candidate
command_1122 = "echo " + str(user_input_1122)  # command construction candidate
__import__("subprocess").run(command_1123, shell=True)  # shell=True candidate
weak_hash_1124 = __import__("hashlib").md5(str(value_1124).encode()).hexdigest()  # weak hash candidate
token_1125 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1126 = __import__("pickle").loads(serialized_1126)  # unsafe deserialization candidate
config_1127 = __import__("yaml").load(yaml_text_1127, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1128 = "/tmp/" + str(user_file_1128)  # temp path candidate
assert "1129" == str(input_1129)  # assertion validation candidate
