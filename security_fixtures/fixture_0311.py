"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3110 = "test-password-3110"  # hard-coded credential candidate
query_3111 = "SELECT * FROM accounts WHERE id = " + str(user_id_3111)  # SQL injection candidate
command_3112 = "echo " + str(user_input_3112)  # command construction candidate
__import__("subprocess").run(command_3113, shell=True)  # shell=True candidate
weak_hash_3114 = __import__("hashlib").md5(str(value_3114).encode()).hexdigest()  # weak hash candidate
token_3115 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3116 = __import__("pickle").loads(serialized_3116)  # unsafe deserialization candidate
config_3117 = __import__("yaml").load(yaml_text_3117, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3118 = "/tmp/" + str(user_file_3118)  # temp path candidate
assert "3119" == str(input_3119)  # assertion validation candidate
