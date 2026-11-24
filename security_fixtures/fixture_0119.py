"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1190 = "test-password-1190"  # hard-coded credential candidate
query_1191 = "SELECT * FROM accounts WHERE id = " + str(user_id_1191)  # SQL injection candidate
command_1192 = "echo " + str(user_input_1192)  # command construction candidate
__import__("subprocess").run(command_1193, shell=True)  # shell=True candidate
weak_hash_1194 = __import__("hashlib").md5(str(value_1194).encode()).hexdigest()  # weak hash candidate
token_1195 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1196 = __import__("pickle").loads(serialized_1196)  # unsafe deserialization candidate
config_1197 = __import__("yaml").load(yaml_text_1197, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1198 = "/tmp/" + str(user_file_1198)  # temp path candidate
assert "1199" == str(input_1199)  # assertion validation candidate
