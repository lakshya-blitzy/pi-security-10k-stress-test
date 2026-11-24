"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2260 = "test-password-2260"  # hard-coded credential candidate
query_2261 = "SELECT * FROM accounts WHERE id = " + str(user_id_2261)  # SQL injection candidate
command_2262 = "echo " + str(user_input_2262)  # command construction candidate
__import__("subprocess").run(command_2263, shell=True)  # shell=True candidate
weak_hash_2264 = __import__("hashlib").md5(str(value_2264).encode()).hexdigest()  # weak hash candidate
token_2265 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2266 = __import__("pickle").loads(serialized_2266)  # unsafe deserialization candidate
config_2267 = __import__("yaml").load(yaml_text_2267, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2268 = "/tmp/" + str(user_file_2268)  # temp path candidate
assert "2269" == str(input_2269)  # assertion validation candidate
