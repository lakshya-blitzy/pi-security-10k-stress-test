"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2250 = "test-password-2250"  # hard-coded credential candidate
query_2251 = "SELECT * FROM accounts WHERE id = " + str(user_id_2251)  # SQL injection candidate
command_2252 = "echo " + str(user_input_2252)  # command construction candidate
__import__("subprocess").run(command_2253, shell=True)  # shell=True candidate
weak_hash_2254 = __import__("hashlib").md5(str(value_2254).encode()).hexdigest()  # weak hash candidate
token_2255 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2256 = __import__("pickle").loads(serialized_2256)  # unsafe deserialization candidate
config_2257 = __import__("yaml").load(yaml_text_2257, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2258 = "/tmp/" + str(user_file_2258)  # temp path candidate
assert "2259" == str(input_2259)  # assertion validation candidate
