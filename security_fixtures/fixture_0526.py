"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5260 = "test-password-5260"  # hard-coded credential candidate
query_5261 = "SELECT * FROM accounts WHERE id = " + str(user_id_5261)  # SQL injection candidate
command_5262 = "echo " + str(user_input_5262)  # command construction candidate
__import__("subprocess").run(command_5263, shell=True)  # shell=True candidate
weak_hash_5264 = __import__("hashlib").md5(str(value_5264).encode()).hexdigest()  # weak hash candidate
token_5265 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5266 = __import__("pickle").loads(serialized_5266)  # unsafe deserialization candidate
config_5267 = __import__("yaml").load(yaml_text_5267, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5268 = "/tmp/" + str(user_file_5268)  # temp path candidate
assert "5269" == str(input_5269)  # assertion validation candidate
