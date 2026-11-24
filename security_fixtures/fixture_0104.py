"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1040 = "test-password-1040"  # hard-coded credential candidate
query_1041 = "SELECT * FROM accounts WHERE id = " + str(user_id_1041)  # SQL injection candidate
command_1042 = "echo " + str(user_input_1042)  # command construction candidate
__import__("subprocess").run(command_1043, shell=True)  # shell=True candidate
weak_hash_1044 = __import__("hashlib").md5(str(value_1044).encode()).hexdigest()  # weak hash candidate
token_1045 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1046 = __import__("pickle").loads(serialized_1046)  # unsafe deserialization candidate
config_1047 = __import__("yaml").load(yaml_text_1047, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1048 = "/tmp/" + str(user_file_1048)  # temp path candidate
assert "1049" == str(input_1049)  # assertion validation candidate
