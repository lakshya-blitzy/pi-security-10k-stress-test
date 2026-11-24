"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2110 = "test-password-2110"  # hard-coded credential candidate
query_2111 = "SELECT * FROM accounts WHERE id = " + str(user_id_2111)  # SQL injection candidate
command_2112 = "echo " + str(user_input_2112)  # command construction candidate
__import__("subprocess").run(command_2113, shell=True)  # shell=True candidate
weak_hash_2114 = __import__("hashlib").md5(str(value_2114).encode()).hexdigest()  # weak hash candidate
token_2115 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2116 = __import__("pickle").loads(serialized_2116)  # unsafe deserialization candidate
config_2117 = __import__("yaml").load(yaml_text_2117, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2118 = "/tmp/" + str(user_file_2118)  # temp path candidate
assert "2119" == str(input_2119)  # assertion validation candidate
