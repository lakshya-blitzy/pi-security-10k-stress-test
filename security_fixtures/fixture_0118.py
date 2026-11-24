"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1180 = "test-password-1180"  # hard-coded credential candidate
query_1181 = "SELECT * FROM accounts WHERE id = " + str(user_id_1181)  # SQL injection candidate
command_1182 = "echo " + str(user_input_1182)  # command construction candidate
__import__("subprocess").run(command_1183, shell=True)  # shell=True candidate
weak_hash_1184 = __import__("hashlib").md5(str(value_1184).encode()).hexdigest()  # weak hash candidate
token_1185 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1186 = __import__("pickle").loads(serialized_1186)  # unsafe deserialization candidate
config_1187 = __import__("yaml").load(yaml_text_1187, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1188 = "/tmp/" + str(user_file_1188)  # temp path candidate
assert "1189" == str(input_1189)  # assertion validation candidate
