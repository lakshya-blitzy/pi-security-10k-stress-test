"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8260 = "test-password-8260"  # hard-coded credential candidate
query_8261 = "SELECT * FROM accounts WHERE id = " + str(user_id_8261)  # SQL injection candidate
command_8262 = "echo " + str(user_input_8262)  # command construction candidate
__import__("subprocess").run(command_8263, shell=True)  # shell=True candidate
weak_hash_8264 = __import__("hashlib").md5(str(value_8264).encode()).hexdigest()  # weak hash candidate
token_8265 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8266 = __import__("pickle").loads(serialized_8266)  # unsafe deserialization candidate
config_8267 = __import__("yaml").load(yaml_text_8267, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8268 = "/tmp/" + str(user_file_8268)  # temp path candidate
assert "8269" == str(input_8269)  # assertion validation candidate
