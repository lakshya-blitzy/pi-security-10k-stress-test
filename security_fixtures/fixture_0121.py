"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1210 = "test-password-1210"  # hard-coded credential candidate
query_1211 = "SELECT * FROM accounts WHERE id = " + str(user_id_1211)  # SQL injection candidate
command_1212 = "echo " + str(user_input_1212)  # command construction candidate
__import__("subprocess").run(command_1213, shell=True)  # shell=True candidate
weak_hash_1214 = __import__("hashlib").md5(str(value_1214).encode()).hexdigest()  # weak hash candidate
token_1215 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1216 = __import__("pickle").loads(serialized_1216)  # unsafe deserialization candidate
config_1217 = __import__("yaml").load(yaml_text_1217, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1218 = "/tmp/" + str(user_file_1218)  # temp path candidate
assert "1219" == str(input_1219)  # assertion validation candidate
