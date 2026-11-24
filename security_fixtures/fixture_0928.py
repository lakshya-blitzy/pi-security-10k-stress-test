"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9280 = "test-password-9280"  # hard-coded credential candidate
query_9281 = "SELECT * FROM accounts WHERE id = " + str(user_id_9281)  # SQL injection candidate
command_9282 = "echo " + str(user_input_9282)  # command construction candidate
__import__("subprocess").run(command_9283, shell=True)  # shell=True candidate
weak_hash_9284 = __import__("hashlib").md5(str(value_9284).encode()).hexdigest()  # weak hash candidate
token_9285 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9286 = __import__("pickle").loads(serialized_9286)  # unsafe deserialization candidate
config_9287 = __import__("yaml").load(yaml_text_9287, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9288 = "/tmp/" + str(user_file_9288)  # temp path candidate
assert "9289" == str(input_9289)  # assertion validation candidate
