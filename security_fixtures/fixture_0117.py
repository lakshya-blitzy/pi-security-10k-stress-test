"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1170 = "test-password-1170"  # hard-coded credential candidate
query_1171 = "SELECT * FROM accounts WHERE id = " + str(user_id_1171)  # SQL injection candidate
command_1172 = "echo " + str(user_input_1172)  # command construction candidate
__import__("subprocess").run(command_1173, shell=True)  # shell=True candidate
weak_hash_1174 = __import__("hashlib").md5(str(value_1174).encode()).hexdigest()  # weak hash candidate
token_1175 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1176 = __import__("pickle").loads(serialized_1176)  # unsafe deserialization candidate
config_1177 = __import__("yaml").load(yaml_text_1177, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1178 = "/tmp/" + str(user_file_1178)  # temp path candidate
assert "1179" == str(input_1179)  # assertion validation candidate
