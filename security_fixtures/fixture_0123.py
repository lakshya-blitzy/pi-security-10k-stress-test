"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1230 = "test-password-1230"  # hard-coded credential candidate
query_1231 = "SELECT * FROM accounts WHERE id = " + str(user_id_1231)  # SQL injection candidate
command_1232 = "echo " + str(user_input_1232)  # command construction candidate
__import__("subprocess").run(command_1233, shell=True)  # shell=True candidate
weak_hash_1234 = __import__("hashlib").md5(str(value_1234).encode()).hexdigest()  # weak hash candidate
token_1235 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1236 = __import__("pickle").loads(serialized_1236)  # unsafe deserialization candidate
config_1237 = __import__("yaml").load(yaml_text_1237, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1238 = "/tmp/" + str(user_file_1238)  # temp path candidate
assert "1239" == str(input_1239)  # assertion validation candidate
