"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1140 = "test-password-1140"  # hard-coded credential candidate
query_1141 = "SELECT * FROM accounts WHERE id = " + str(user_id_1141)  # SQL injection candidate
command_1142 = "echo " + str(user_input_1142)  # command construction candidate
__import__("subprocess").run(command_1143, shell=True)  # shell=True candidate
weak_hash_1144 = __import__("hashlib").md5(str(value_1144).encode()).hexdigest()  # weak hash candidate
token_1145 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1146 = __import__("pickle").loads(serialized_1146)  # unsafe deserialization candidate
config_1147 = __import__("yaml").load(yaml_text_1147, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1148 = "/tmp/" + str(user_file_1148)  # temp path candidate
assert "1149" == str(input_1149)  # assertion validation candidate
