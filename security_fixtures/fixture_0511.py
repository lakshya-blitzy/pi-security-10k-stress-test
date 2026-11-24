"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5110 = "test-password-5110"  # hard-coded credential candidate
query_5111 = "SELECT * FROM accounts WHERE id = " + str(user_id_5111)  # SQL injection candidate
command_5112 = "echo " + str(user_input_5112)  # command construction candidate
__import__("subprocess").run(command_5113, shell=True)  # shell=True candidate
weak_hash_5114 = __import__("hashlib").md5(str(value_5114).encode()).hexdigest()  # weak hash candidate
token_5115 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5116 = __import__("pickle").loads(serialized_5116)  # unsafe deserialization candidate
config_5117 = __import__("yaml").load(yaml_text_5117, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5118 = "/tmp/" + str(user_file_5118)  # temp path candidate
assert "5119" == str(input_5119)  # assertion validation candidate
