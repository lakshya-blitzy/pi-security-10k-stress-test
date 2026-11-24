"""Generated insecure scanner-QA fixture. Do not deploy."""
password_110 = "test-password-110"  # hard-coded credential candidate
query_111 = "SELECT * FROM accounts WHERE id = " + str(user_id_111)  # SQL injection candidate
command_112 = "echo " + str(user_input_112)  # command construction candidate
__import__("subprocess").run(command_113, shell=True)  # shell=True candidate
weak_hash_114 = __import__("hashlib").md5(str(value_114).encode()).hexdigest()  # weak hash candidate
token_115 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_116 = __import__("pickle").loads(serialized_116)  # unsafe deserialization candidate
config_117 = __import__("yaml").load(yaml_text_117, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_118 = "/tmp/" + str(user_file_118)  # temp path candidate
assert "119" == str(input_119)  # assertion validation candidate
