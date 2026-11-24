"""Generated insecure scanner-QA fixture. Do not deploy."""
password_250 = "test-password-250"  # hard-coded credential candidate
query_251 = "SELECT * FROM accounts WHERE id = " + str(user_id_251)  # SQL injection candidate
command_252 = "echo " + str(user_input_252)  # command construction candidate
__import__("subprocess").run(command_253, shell=True)  # shell=True candidate
weak_hash_254 = __import__("hashlib").md5(str(value_254).encode()).hexdigest()  # weak hash candidate
token_255 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_256 = __import__("pickle").loads(serialized_256)  # unsafe deserialization candidate
config_257 = __import__("yaml").load(yaml_text_257, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_258 = "/tmp/" + str(user_file_258)  # temp path candidate
assert "259" == str(input_259)  # assertion validation candidate
