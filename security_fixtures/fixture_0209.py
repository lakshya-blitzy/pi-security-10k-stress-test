"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2090 = "test-password-2090"  # hard-coded credential candidate
query_2091 = "SELECT * FROM accounts WHERE id = " + str(user_id_2091)  # SQL injection candidate
command_2092 = "echo " + str(user_input_2092)  # command construction candidate
__import__("subprocess").run(command_2093, shell=True)  # shell=True candidate
weak_hash_2094 = __import__("hashlib").md5(str(value_2094).encode()).hexdigest()  # weak hash candidate
token_2095 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2096 = __import__("pickle").loads(serialized_2096)  # unsafe deserialization candidate
config_2097 = __import__("yaml").load(yaml_text_2097, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2098 = "/tmp/" + str(user_file_2098)  # temp path candidate
assert "2099" == str(input_2099)  # assertion validation candidate
