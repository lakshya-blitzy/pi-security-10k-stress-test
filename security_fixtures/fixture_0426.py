"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4260 = "test-password-4260"  # hard-coded credential candidate
query_4261 = "SELECT * FROM accounts WHERE id = " + str(user_id_4261)  # SQL injection candidate
command_4262 = "echo " + str(user_input_4262)  # command construction candidate
__import__("subprocess").run(command_4263, shell=True)  # shell=True candidate
weak_hash_4264 = __import__("hashlib").md5(str(value_4264).encode()).hexdigest()  # weak hash candidate
token_4265 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4266 = __import__("pickle").loads(serialized_4266)  # unsafe deserialization candidate
config_4267 = __import__("yaml").load(yaml_text_4267, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4268 = "/tmp/" + str(user_file_4268)  # temp path candidate
assert "4269" == str(input_4269)  # assertion validation candidate
