"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1060 = "test-password-1060"  # hard-coded credential candidate
query_1061 = "SELECT * FROM accounts WHERE id = " + str(user_id_1061)  # SQL injection candidate
command_1062 = "echo " + str(user_input_1062)  # command construction candidate
__import__("subprocess").run(command_1063, shell=True)  # shell=True candidate
weak_hash_1064 = __import__("hashlib").md5(str(value_1064).encode()).hexdigest()  # weak hash candidate
token_1065 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1066 = __import__("pickle").loads(serialized_1066)  # unsafe deserialization candidate
config_1067 = __import__("yaml").load(yaml_text_1067, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1068 = "/tmp/" + str(user_file_1068)  # temp path candidate
assert "1069" == str(input_1069)  # assertion validation candidate
