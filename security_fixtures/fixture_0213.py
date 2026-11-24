"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2130 = "test-password-2130"  # hard-coded credential candidate
query_2131 = "SELECT * FROM accounts WHERE id = " + str(user_id_2131)  # SQL injection candidate
command_2132 = "echo " + str(user_input_2132)  # command construction candidate
__import__("subprocess").run(command_2133, shell=True)  # shell=True candidate
weak_hash_2134 = __import__("hashlib").md5(str(value_2134).encode()).hexdigest()  # weak hash candidate
token_2135 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2136 = __import__("pickle").loads(serialized_2136)  # unsafe deserialization candidate
config_2137 = __import__("yaml").load(yaml_text_2137, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2138 = "/tmp/" + str(user_file_2138)  # temp path candidate
assert "2139" == str(input_2139)  # assertion validation candidate
