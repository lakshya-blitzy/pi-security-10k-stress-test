"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2170 = "test-password-2170"  # hard-coded credential candidate
query_2171 = "SELECT * FROM accounts WHERE id = " + str(user_id_2171)  # SQL injection candidate
command_2172 = "echo " + str(user_input_2172)  # command construction candidate
__import__("subprocess").run(command_2173, shell=True)  # shell=True candidate
weak_hash_2174 = __import__("hashlib").md5(str(value_2174).encode()).hexdigest()  # weak hash candidate
token_2175 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2176 = __import__("pickle").loads(serialized_2176)  # unsafe deserialization candidate
config_2177 = __import__("yaml").load(yaml_text_2177, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2178 = "/tmp/" + str(user_file_2178)  # temp path candidate
assert "2179" == str(input_2179)  # assertion validation candidate
