"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2180 = "test-password-2180"  # hard-coded credential candidate
query_2181 = "SELECT * FROM accounts WHERE id = " + str(user_id_2181)  # SQL injection candidate
command_2182 = "echo " + str(user_input_2182)  # command construction candidate
__import__("subprocess").run(command_2183, shell=True)  # shell=True candidate
weak_hash_2184 = __import__("hashlib").md5(str(value_2184).encode()).hexdigest()  # weak hash candidate
token_2185 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2186 = __import__("pickle").loads(serialized_2186)  # unsafe deserialization candidate
config_2187 = __import__("yaml").load(yaml_text_2187, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2188 = "/tmp/" + str(user_file_2188)  # temp path candidate
assert "2189" == str(input_2189)  # assertion validation candidate
