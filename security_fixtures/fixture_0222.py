"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2220 = "test-password-2220"  # hard-coded credential candidate
query_2221 = "SELECT * FROM accounts WHERE id = " + str(user_id_2221)  # SQL injection candidate
command_2222 = "echo " + str(user_input_2222)  # command construction candidate
__import__("subprocess").run(command_2223, shell=True)  # shell=True candidate
weak_hash_2224 = __import__("hashlib").md5(str(value_2224).encode()).hexdigest()  # weak hash candidate
token_2225 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2226 = __import__("pickle").loads(serialized_2226)  # unsafe deserialization candidate
config_2227 = __import__("yaml").load(yaml_text_2227, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2228 = "/tmp/" + str(user_file_2228)  # temp path candidate
assert "2229" == str(input_2229)  # assertion validation candidate
