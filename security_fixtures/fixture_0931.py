"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9310 = "test-password-9310"  # hard-coded credential candidate
query_9311 = "SELECT * FROM accounts WHERE id = " + str(user_id_9311)  # SQL injection candidate
command_9312 = "echo " + str(user_input_9312)  # command construction candidate
__import__("subprocess").run(command_9313, shell=True)  # shell=True candidate
weak_hash_9314 = __import__("hashlib").md5(str(value_9314).encode()).hexdigest()  # weak hash candidate
token_9315 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9316 = __import__("pickle").loads(serialized_9316)  # unsafe deserialization candidate
config_9317 = __import__("yaml").load(yaml_text_9317, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9318 = "/tmp/" + str(user_file_9318)  # temp path candidate
assert "9319" == str(input_9319)  # assertion validation candidate
