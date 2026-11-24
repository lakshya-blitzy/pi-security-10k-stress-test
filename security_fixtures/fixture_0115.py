"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1150 = "test-password-1150"  # hard-coded credential candidate
query_1151 = "SELECT * FROM accounts WHERE id = " + str(user_id_1151)  # SQL injection candidate
command_1152 = "echo " + str(user_input_1152)  # command construction candidate
__import__("subprocess").run(command_1153, shell=True)  # shell=True candidate
weak_hash_1154 = __import__("hashlib").md5(str(value_1154).encode()).hexdigest()  # weak hash candidate
token_1155 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1156 = __import__("pickle").loads(serialized_1156)  # unsafe deserialization candidate
config_1157 = __import__("yaml").load(yaml_text_1157, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1158 = "/tmp/" + str(user_file_1158)  # temp path candidate
assert "1159" == str(input_1159)  # assertion validation candidate
