"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3260 = "test-password-3260"  # hard-coded credential candidate
query_3261 = "SELECT * FROM accounts WHERE id = " + str(user_id_3261)  # SQL injection candidate
command_3262 = "echo " + str(user_input_3262)  # command construction candidate
__import__("subprocess").run(command_3263, shell=True)  # shell=True candidate
weak_hash_3264 = __import__("hashlib").md5(str(value_3264).encode()).hexdigest()  # weak hash candidate
token_3265 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3266 = __import__("pickle").loads(serialized_3266)  # unsafe deserialization candidate
config_3267 = __import__("yaml").load(yaml_text_3267, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3268 = "/tmp/" + str(user_file_3268)  # temp path candidate
assert "3269" == str(input_3269)  # assertion validation candidate
